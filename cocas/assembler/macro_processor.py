import codecs
import antlr4
import itertools
import re
from base64 import b64encode
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable, Optional

from antlr4 import CommonTokenStream, InputStream
from antlr4.TokenStreamRewriter import TokenStreamRewriter

from cocas.object_module import CodeLocation

from .exceptions import AntlrErrorListener, AssemblerException, AssemblerExceptionTag, CdmTempException
from .generated import MacroLexer, MacroParser, MacroVisitor


def unique(params: list[str], macro_stack: list[str]):
    register_available = [True] * 4
    var_params = []
    for param in params:
        param_match = re.fullmatch(r'r(\d)', param)
        if param_match:
            register_number = int(param_match.group(1))
            if not register_available[register_number]:
                raise CdmTempException(f'unique: {param} appears multiple times')
            register_available[register_number] = False
        else:
            var_params.append(param)

    i = 0
    defined_vars = dict()
    for param in var_params:
        while not register_available[i]:
            i += 1
            if i == 4:
                raise CdmTempException('unique: not enough registers')
        register_available[i] = False
        defined_vars[param] = f'r{i}'
    return defined_vars

def mpush(params: list[str], macro_stack: list[str]):
    for param in params:
        macro_stack.append(param)

    return dict()

def mpop(params: list[str], macro_stack: list[str]):
    defined_vars = dict()
    for param in params:
        if not macro_stack:
            raise CdmTempException('mpop: macro stack is empty')

        defined_vars[param] = macro_stack.pop()

    return defined_vars	


macro_instructions = {
    'unique': unique,
    'mpush': mpush,
    'mpop': mpop,
}


@dataclass
class MacroParameter:
    n: int


@dataclass
class MacroNonce:
    pass


@dataclass
class MacroVariable:
    name_pieces: list


def not_ws(x):
    return not isinstance(x, str) or not x.isspace()


def iter_eq(a, b):
    if isinstance(a, str) or isinstance(b, str) or not isinstance(a, Iterable) or not isinstance(b, Iterable):
        return a == b
    else:
        return all(iter_eq(x, y) for x, y in itertools.zip_longest(a, b))


@dataclass
class MacroLine:
    label_pieces: list
    instruction_pieces: list
    parameter_pieces: list[list]

    def __eq__(self, other):
        return (iter_eq(filter(not_ws, self.label_pieces), filter(not_ws, other.label_pieces)) and
                iter_eq(filter(not_ws, self.instruction_pieces), filter(not_ws, other.instruction_pieces)) and
                iter_eq(
                    map(lambda x: filter(not_ws, x), self.parameter_pieces),
                    map(lambda x: filter(not_ws, x), other.parameter_pieces)
                ))


@dataclass
class MacroDefinition:
    name: str
    arity: int
    lines: list[MacroLine]
    location: CodeLocation

    def __eq__(self, other):
        return self.name == other.name and self.arity == other.arity and self.lines == other.lines


def substitute_piece(piece, params: list[str], nonce: str, variables: dict[str, str]):
    if isinstance(piece, MacroParameter):
        return params[piece.n - 1]
    elif isinstance(piece, MacroNonce):
        return nonce
    elif isinstance(piece, MacroVariable):
        def sub(p):
            return substitute_piece(p, params, nonce, variables)

        var_name = ''.join(map(sub, piece.name_pieces))
        return variables[var_name]
    else:
        return piece


def substitute_pieces_in_line(line: MacroLine, params: list[str], nonce: str, variables: dict[str, str]):
    def sub(p):
        return substitute_piece(p, params, nonce, variables)

    def sub_all(ps):
        return ''.join(map(sub, ps))

    label_part = sub_all(line.label_pieces)
    instruction_part = sub_all(line.instruction_pieces)
    parameter_parts = list(map(sub_all, line.parameter_pieces))
    return label_part, instruction_part, parameter_parts


# noinspection PyPep8Naming
class ExpandMacrosVisitor(MacroVisitor):
    def __init__(self, rewriter: Optional[TokenStreamRewriter], mlb_macros, filepath: str, include_paths: list[Path], nested):
        # rewriter should be None if then will be called .visit(MlbContext)
        # rewriter should be valid if then will be called .visit(ProgramContext)
        self.nested = nested
        self.nonce = 0
        self.macro_stack = []
        self.macros = {name: mlb_macros[name].copy() for name in mlb_macros}
        self.rewriter = rewriter
        self.filepath = filepath
        self.include_paths = include_paths

    @staticmethod
    def _generate_location_line(filepath: str, line: int, info: str = None) -> str:
        if info is not None:
            info = " " + info
        else:
            info = ""
        return f'-| {line} fp-{b64encode(filepath.encode()).decode()} {info}\n'

    def add_macro(self, macro: MacroDefinition):
        if macro.name not in self.macros:
            self.macros[macro.name] = dict()
        if macro.arity in self.macros[macro.name]:
            if self.macros[macro.name][macro.arity] != macro:
                raise CdmTempException(f"Redefinition of macro {macro.name}/{macro.arity} with different body")
        self.macros[macro.name][macro.arity] = macro

    def include_file(self, include_filename: str):
        # Firstly check in directoru where file is
        with Path(self.filepath).parent as path:
            include_filepath = path / include_filename
            if include_filepath.is_file():
                with include_filepath.open('rb') as file:
                    data = file.read()
                data = codecs.decode(data, 'utf8', 'strict')
                if not data.endswith('\n'):
                    data += '\n'
                input_stream = antlr4.InputStream(data)

                return ''.join([chr(i) for i in process_macros(input_stream, dict(), include_filepath, self.include_paths, True, self).data])

        for path in self.include_paths:
            include_filepath = path / include_filename
            if include_filepath.is_file():
                with include_filepath.open('rb') as file:
                    data = file.read()
                data = codecs.decode(data, 'utf8', 'strict')
                if not data.endswith('\n'):
                    data += '\n'
                input_stream = antlr4.InputStream(data)
                return ''.join([chr(i) for i in process_macros(input_stream, dict(), include_filepath, self.include_paths, True, self).data])
		
        # Raise exception if there is no such file in include paths
        raise CdmTempException(f'Include: file {include_filename} not found in any search path')

    # Returns a None for things as asect or empty line.
    # Returns string of macro
    def expand_macro(self, macro_name: str, macro_params: list[str]):
        arity = len(macro_params)
        if macro_name in self.macros and arity in self.macros[macro_name]:
            ret_parts = []
            self.nonce += 1
            macro_nonce = str(self.nonce)
            macro: MacroDefinition = self.macros[macro_name][arity]

            variables = {}

            ret_parts.append(self._generate_location_line(macro.location.file, macro.location.line))

            line_number = 0
            for line in macro.lines:
                label_part, instruction_part, parameter_parts \
                    = substitute_pieces_in_line(line, macro_params, macro_nonce, variables)
                label = label_part.rstrip()
                instruction = instruction_part.strip()
                parameters = list(map(str.strip, parameter_parts))
                if parameters == ['']:
                    parameters = []

                # IMPORTANT:
                # to correctly generate location information
                # each line that does not contain another macro
                # MUST add exactly ONE line to ret_parts
                if instruction in macro_instructions:
                    variables.update(macro_instructions[instruction](parameters, self.macro_stack))
                    if label != '':
                        ret_parts.append(f'{label}\n')
                    else:
                        ret_parts.append('\n')
                else:
                    expanded_text = self.expand_macro(instruction, parameters)
                    if expanded_text is not None:
                        if label != '':
                            ret_parts.append(f'{label}\n')
                        else:
                            ret_parts.append('\n')
                        ret_parts.append(expanded_text)
                        location_line = self._generate_location_line(macro.location.file,
                                                                     macro.location.line + line_number + 1)
                        ret_parts.append(f'\n{location_line}')
                    else:
                        ret_parts.append(f'{label_part}{instruction_part}{",".join(parameter_parts)}\n')
                line_number += 1
            return ''.join(ret_parts)
        return None

    def visitMlb(self, ctx: MacroParser.MlbContext):
        for child in filter(lambda c: isinstance(c, MacroParser.Mlb_macroContext), ctx.children):
            try:
                self.add_macro(self.visitMlb_macro(child))
            except CdmTempException as e:
                raise AssemblerException(AssemblerExceptionTag.MACRO, self.filepath, child.start.line, e.message)
        return self.macros

    def visitProgram(self, ctx: MacroParser.ProgramContext):
        if len(ctx.children) > 0:
            self.rewriter.insertBeforeToken(ctx.children[0].start, self._generate_location_line(self.filepath, 1))
        for child in ctx.children:
            try:
                if isinstance(child, MacroParser.MacroContext):
                    self.add_macro(self.visitMacro(child))
                elif isinstance(child, MacroParser.LineContext):
                    label, instruction, parameters = self.visitLine(child)
                    if instruction == 'include':
                        if len(parameters) != 1:
                            raise CdmTempException('Include: wrong amount of parameters, expected 1 parameter')
                        expanded_text = self.include_file(parameters[0])
                    else:
                        expanded_text = self.expand_macro(instruction, parameters)
                    if expanded_text is not None:
                        if label != '':
                            expanded_text = f'{label}\n{expanded_text}'

                        if self.nested:
                            stop_mark = self._generate_location_line(self.filepath, child.stop.line + 1)
                            expanded_text = f'{expanded_text}{stop_mark}'
                        else:
                            mstart = self._generate_location_line(self.filepath, child.start.line, "mstart")
                            mstop = self._generate_location_line(self.filepath, child.stop.line + 1, "mstop")
                            expanded_text = f'{mstart}{expanded_text}{mstop}'
                        self.rewriter.insertBeforeToken(child.start, expanded_text)
                        self.rewriter.delete(self.rewriter.DEFAULT_PROGRAM_NAME, child.start, child.stop)
            except CdmTempException as e:
                raise AssemblerException(AssemblerExceptionTag.MACRO, self.filepath, child.start.line, e.message)

    def visitMacro(self, ctx: MacroParser.MacroContext):
        header = ctx.macro_header()
        name = header.NAME().getText()
        arity = int(header.DIGIT().getText())
        lines = self.visitMacro_body(ctx.macro_body())
        self.rewriter.delete(self.rewriter.DEFAULT_PROGRAM_NAME, ctx.start, ctx.stop)
        self.rewriter.insertAfterToken(ctx.stop, self._generate_location_line(self.filepath, ctx.stop.line + 1))
        return MacroDefinition(name, arity, lines, CodeLocation(self.filepath, ctx.macro_body().start.line, 0))

    def visitMlb_macro(self, ctx: MacroParser.Mlb_macroContext):
        header = ctx.mlb_header()
        name = header.NAME().getText()
        arity = int(header.DIGIT().getText())
        lines = self.visitMacro_body(ctx.macro_body())
        return MacroDefinition(name, arity, lines, CodeLocation(self.filepath, ctx.macro_body().start.line, 0))

    def visitMacro_body(self, ctx: MacroParser.Macro_bodyContext):
        if ctx.children is None:
            return []

        lines = []
        for child in ctx.line():
            lines.append(self.visitMacroLine(child))
        return lines

    def visitMacroLine(self, ctx: MacroParser.LineContext):
        label_pieces = self.visitLabels(ctx.labels())
        instruction_pieces = self.visitMacro_item(ctx.instruction()) if ctx.instruction() is not None else []
        parameter_pieces = [self.visitFirst_param(ctx.first_param())] if ctx.first_param() is not None else [[]]
        for param in ctx.getChildren(lambda c: isinstance(c, MacroParser.ParamContext)):
            parameter_pieces.append(self.visitMacro_item(param))
        return MacroLine(label_pieces, instruction_pieces, parameter_pieces)

    def visitLine(self, ctx: MacroParser.LineContext):
        label = ctx.labels().getText().rstrip()
        instruction = ctx.instruction().getText().strip() if ctx.instruction() is not None else ''
        parameters = [ctx.first_param().getText().strip()] if ctx.first_param() is not None else ['']
        for param in ctx.getChildren(lambda c: isinstance(c, MacroParser.ParamContext)):
            parameters.append(param.getText().strip())
        if parameters == ['']:
            parameters = []
        return label, instruction, parameters

    def visitLabels(self, ctx: MacroParser.LabelsContext):
        label_pieces = []
        for label in ctx.getChildren(lambda c: isinstance(c, MacroParser.LabelContext)):
            label_pieces.extend(self.visitMacro_item(label))
        if ctx.WS() is not None:
            label_pieces.append(ctx.WS().getText())
        return label_pieces

    def visitFirst_param(self, ctx: MacroParser.First_paramContext):
        param_pieces = self.visitMacro_item(ctx.param()) if ctx.param() is not None else []
        if ctx.WS() is not None:
            param_pieces = [ctx.WS().getText()] + param_pieces
        return param_pieces

    def visitMacro_item(self, ctx):
        item_pieces = []
        for child in ctx.getChildren():
            if isinstance(child, MacroParser.Macro_variableContext):
                item_pieces.append(self.visitMacro_variable(child))
            elif isinstance(child, MacroParser.Macro_pieceContext):
                item_pieces.append(self.visitMacro_piece(child))
            else:
                item_pieces.append(child.getText())
        return item_pieces

    def visitMacro_variable(self, ctx: MacroParser.Macro_variableContext):
        name_pieces = []
        for child in ctx.children[1:]:
            name_pieces.append(self.visitMacro_piece(child))
        return MacroVariable(name_pieces)

    def visitMacro_piece(self, ctx: MacroParser.Macro_pieceContext):
        if ctx.macro_text() is not None:
            return ctx.macro_text().getText()
        elif ctx.macro_param() is not None:
            return MacroParameter(int(ctx.macro_param().DIGIT().getText()))
        elif ctx.macro_nonce() is not None:
            return MacroNonce()


def read_mlb(filepath: Path) -> dict[str, dict[int, MacroDefinition]]:
    str_path = filepath.absolute().as_posix()
    with filepath.open('rb') as file:
        data = file.read()
    data = codecs.decode(data, 'utf8', 'strict')
    if not data.endswith('\n'):
        data += '\n'
    input_stream = InputStream(data)
    lexer = MacroLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = MacroParser(token_stream)
    cst = parser.mlb()
    emv = ExpandMacrosVisitor(None, dict(), str_path, [], False)
    return emv.visit(cst)

# Added arguments:
# include_paths - list of include paths
# nested - if file macroprocessed for insertion into another file
# init_ctx - ExpandMacrosVisitor - initial context which used for sharing same macros, nonce value and macro stack with some file, for insertion into which we macroprocessing this file
def process_macros(input_stream: InputStream, library_macros, filepath: Path, include_paths: list[Path], nested, init_ctx: ExpandMacrosVisitor = None):
    str_path = filepath.absolute().as_posix()
    lexer = MacroLexer(input_stream)
    lexer.removeErrorListeners()
    lexer.addErrorListener(AntlrErrorListener(AssemblerExceptionTag.MACRO, str_path))
    token_stream = CommonTokenStream(lexer)

    parser = MacroParser(token_stream)
    parser.removeErrorListeners()
    parser.addErrorListener(AntlrErrorListener(AssemblerExceptionTag.MACRO, str_path))
    cst = parser.program()
    rewriter = TokenStreamRewriter(token_stream)

    emv = ExpandMacrosVisitor(rewriter, library_macros, str_path, include_paths, nested)
    # If init_ctx passed, take its nonce value, macro_stack and macros to emv (all except nonce by reference)
    if init_ctx is not None:
        emv.nonce = init_ctx.nonce
        emv.macro_stack = init_ctx.macro_stack
        emv.macros = init_ctx.macros
    emv.visit(cst)
    new_text = rewriter.getDefaultText()
    # Modify init_ctx nonce
    if init_ctx is not None:
        init_ctx.nonce = emv.nonce
    return InputStream(new_text)
