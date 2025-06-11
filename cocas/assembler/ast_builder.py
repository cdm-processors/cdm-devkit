import codecs
import warnings
from base64 import b64decode
from collections.abc import Mapping, MutableSequence
from pathlib import Path
from typing import cast

from antlr4 import CommonTokenStream, InputStream

from cocas.assembler.constants import DBG_LOC_INST, DBG_SOURCE_INST
from cocas.object_module import CodeLocation

from .ast_nodes import (
    AbsoluteSectionNode,
    BreakStatementNode,
    ConditionalStatementNode,
    ConditionNode,
    ContinueStatementNode,
    InstructionNode,
    LabelDeclarationNode,
    LabelNode,
    LocatableNode,
    Node,
    ProgramNode,
    RegisterNode,
    RelocatableExpressionNode,
    RelocatableSectionNode,
    SectionNode,
    TemplateSectionNode,
    UntilLoopNode,
    WhileLoopNode,
)
from .exceptions import AntlrErrorListener, AssemblerException, AssemblerExceptionTag
from .generated import AsmLexer, AsmParser, AsmParserVisitor


# noinspection PyPep8Naming
class BuildAstVisitor(AsmParserVisitor):
    allowed_top_instructions = [DBG_SOURCE_INST]

    def __init__(self, filepath: str):
        super().__init__()
        self.line_offset = 0
        # self.line_offset = 0
        self.source_path = filepath
        self.line_offset = 0
        self.in_macro = False
        self.current_macro_file = ""
        self.current_macro_line = 0
        self.generated: bool = False

    def _ctx_location(self, ctx) -> CodeLocation:
        if self.generated:
            return CodeLocation()
        if self.in_macro:
            return CodeLocation(self.current_macro_file, self.current_macro_line)
        return CodeLocation(self.source_path, ctx.start.line - self.line_offset)

    def visitProgram(self, ctx: AsmParser.ProgramContext) -> ProgramNode:
        ret = ProgramNode([], [], [])
        for child in ctx.children:
            if isinstance(child, AsmParser.AbsoluteSectionContext):
                ret.absolute_sections.append(self.visitAbsoluteSection(child))
            elif isinstance(child, AsmParser.RelocatableSectionContext):
                ret.relocatable_sections.append(self.visitRelocatableSection(child))
            elif isinstance(child, AsmParser.TemplateSectionContext):
                ret.template_sections.append(self.visitTemplateSection(child))
            elif isinstance(child, AsmParser.Line_markContext):
                self.visitLine_mark(child)
            elif isinstance(child, AsmParser.Top_lineContext):
                shared, top = self.visitTop_line(child)
                ret.shared_externals.extend(shared)
                ret.top_instructions.extend(top)
        return ret

    def visitTop_line(self, ctx: AsmParser.Top_lineContext) -> tuple[list[LabelNode], list[InstructionNode]]:
        shared_externals = []
        top_instructions = []
        for child in ctx.children:
            if isinstance(child, AsmParser.InstructionLineContext):
                nodes = self.visitInstructionLine(child)
                loc = self._ctx_location(ctx)
                for i in nodes:
                    if isinstance(i, InstructionNode):
                        if i.mnemonic not in self.allowed_top_instructions:
                            raise AssemblerException(AssemblerExceptionTag.ASM, loc.file, loc.line,
                                                     f"Instruction {i.mnemonic} not allowed at the top of a file")
                        else:
                            top_instructions.append(i)
                    elif isinstance(i, LabelDeclarationNode):
                        self.check_label_is_ext(i)
                        shared_externals.append(i.label)
                    else:
                        raise Exception(f"Unexpected node from top line: {i}")
            elif isinstance(child, AsmParser.StandaloneLabelsContext):
                labels = self.visitStandaloneLabels(child)
                for i in labels:
                    self.check_label_is_ext(i)
                    shared_externals.append(i.label)
        return shared_externals, top_instructions

    @staticmethod
    def check_label_is_ext(label: LabelDeclarationNode):
        if not label.external:
            raise AssemblerException(AssemblerExceptionTag.ASM, label.location.file, label.location.line,
                                     "Only external labels are allowed at the top of a file")

    def visitAbsoluteSection(self, ctx: AsmParser.AbsoluteSectionContext) -> AbsoluteSectionNode:
        header = ctx.asect_header()
        lines = self.visitSection_body(ctx.section_body())
        address = self.visitNumber(header.number())
        return AbsoluteSectionNode(lines, address)

    def visitRelocatableSection(self, ctx: AsmParser.RelocatableSectionContext) -> RelocatableSectionNode:
        header = ctx.rsect_header()
        lines = self.visitSection_body(ctx.section_body())
        name = header.name().getText()
        return RelocatableSectionNode(lines, name)

    def visitTemplateSection(self, ctx: AsmParser.TemplateSectionContext) -> TemplateSectionNode:
        header = ctx.tplate_header()
        lines = self.visitSection_body(ctx.section_body())
        name = header.name().getText()
        return TemplateSectionNode(lines, name)

    def visitLine_mark(self, ctx: AsmParser.Line_markContext):
        # TODO: use already parsed values
        value = int(ctx.line_number().getText())
        filepath = b64decode(ctx.filepath().getText()[3:]).decode()
        self.source_path = filepath
        self.line_offset = ctx.start.line - value + 1

        info = ctx.WORD()
        if info is not None:
            info = info.getText()
            if info == 'mstart':
                self.current_macro_line = value
                self.current_macro_file = self.source_path
                self.in_macro = True
            elif info == 'mstop':
                self.in_macro = False

    def visitNumber(self, ctx: AsmParser.NumberContext) -> int:
        return int(ctx.getText(), base=0)

    def visitSection_body(self, ctx: AsmParser.Section_bodyContext) -> list:
        return self.visitCode_block(ctx.code_block(), return_locations=False)

    def visitConditional(self, ctx: AsmParser.ConditionalContext):
        ctx_conditions = ctx.conditions()
        conditions = self.visitConditions(ctx_conditions)
        then_lines = self.visitCode_block(ctx.code_block())
        if ctx.else_clause():
            else_lines = self.visitElse_clause(ctx.else_clause())
            else_location = self._ctx_location(ctx.else_clause())
            return ConditionalStatementNode(conditions, then_lines, else_lines, else_location)
        return ConditionalStatementNode(conditions, then_lines, [], None)

    def visitConditions(self, ctx: AsmParser.ConditionsContext):
        conditions = []
        for cond in ctx.connective_condition():
            conditions.append(self.visitConnective_condition(cond))
        conditions.append(self.visitCondition(ctx.condition()))
        return conditions

    def visitConnective_condition(self, ctx: AsmParser.Connective_conditionContext):
        cond = self.visitCondition(ctx.condition())
        cond.conjunction = ctx.conjunction().getText()
        if cond.conjunction != 'and' and cond.conjunction != 'or':
            raise AssemblerException(AssemblerExceptionTag.ASM, self.source_path, ctx.start.line - self.line_offset,
                                     'Expected "and" or "or" in compound condition')
        return cond

    def visitCondition(self, ctx: AsmParser.ConditionContext):
        lines = self.visitCode_block(ctx.code_block())
        location = self._ctx_location(ctx.branch_mnemonic())
        return ConditionNode(lines, ctx.branch_mnemonic().getText(), None, location)

    def visitElse_clause(self, ctx: AsmParser.Else_clauseContext):
        return self.visitCode_block(ctx.code_block())

    def visitWhile_loop(self, ctx: AsmParser.While_loopContext):
        while_loc = self._ctx_location(ctx)
        condition_lines = self.visitWhile_condition(ctx.while_condition())
        mnem_loc = self._ctx_location(ctx.branch_mnemonic())
        lines = self.visitCode_block(ctx.code_block())
        return WhileLoopNode(condition_lines, ctx.branch_mnemonic().getText(), lines, while_loc, mnem_loc)

    def visitWhile_condition(self, ctx: AsmParser.While_conditionContext):
        return self.visitCode_block(ctx.code_block())

    def visitUntil_loop(self, ctx: AsmParser.Until_loopContext):
        lines = self.visitCode_block(ctx.code_block())
        mnemonic = ctx.branch_mnemonic()
        return UntilLoopNode(lines, mnemonic.getText(), self._ctx_location(mnemonic))

    def visitCode_block(self, ctx: AsmParser.Code_blockContext, return_locations=False):
        if ctx.children is None:
            if return_locations:
                return [], []
            else:
                return []

        locations = []
        ret = []
        for c in ctx.children:
            nodes = []
            if isinstance(c, AsmParser.StandaloneLabelsContext):
                for i in self.visitStandaloneLabels(c):
                    nodes.append(i)
            elif isinstance(c, AsmParser.InstructionLineContext):
                nodes += self.visitInstructionLine(c)
            elif isinstance(c, AsmParser.ConditionalContext):
                nodes.append(self.visitConditional(c))
            elif isinstance(c, AsmParser.While_loopContext):
                nodes.append(self.visitWhile_loop(c))
            elif isinstance(c, AsmParser.Until_loopContext):
                nodes.append(self.visitUntil_loop(c))
            elif isinstance(c, AsmParser.Break_statementContext):
                nodes.append(BreakStatementNode())
            elif isinstance(c, AsmParser.Continue_statementContext):
                nodes.append(ContinueStatementNode())
            elif isinstance(c, AsmParser.Line_markContext):
                self.visit(c)  # visitLine_mark
            for node in nodes:
                if isinstance(node, LocatableNode):
                    node.location = self._ctx_location(c)
            ret += nodes
            while len(locations) < len(ret):
                locations.append(self._ctx_location(c))
        if return_locations:
            return ret, locations
        else:
            return ret

    def visitByte_expr(self, ctx: AsmParser.Byte_exprContext):
        expr = self.visitAddr_expr(ctx.addr_expr())
        expr.byte_specifier = ctx.byte_specifier().getText()
        return expr

    def visitAddr_expr(self, ctx: AsmParser.Addr_exprContext):
        add_terms = []
        sub_terms = []
        const_term = 0
        for c in ctx.children:
            term = self.visitTerm(c.term())
            if c.MINUS() is not None:
                if isinstance(term, int):
                    const_term -= term
                else:
                    sub_terms.append(term)
            else:
                if isinstance(term, int):
                    const_term += term
                else:
                    add_terms.append(term)
        return RelocatableExpressionNode(None, add_terms, sub_terms, const_term)

    def visitStandaloneLabels(self, ctx: AsmParser.StandaloneLabelsContext) -> list[LabelDeclarationNode]:
        label_decl = self.visitLabels_declaration(ctx.labels_declaration())
        for i in label_decl:
            i.external = ctx.Ext() is not None
            if i.entry and i.external:
                raise AssemblerException(AssemblerExceptionTag.ASM, self.source_path, ctx.start.line - self.line_offset,
                                         f'Label {i.label.name} cannot be both external and entry')
        return label_decl

    def visitLabels_declaration(self, ctx: AsmParser.Labels_declarationContext) -> list[LabelDeclarationNode]:
        is_entry = ctx.ANGLE_BRACKET() is not None
        return [LabelDeclarationNode(i, is_entry, False) for i in self.visitLabels(ctx.labels())]

    def visitLabels(self, ctx: AsmParser.LabelsContext):
        return [self.visitLabel(i) for i in ctx.label()]

    def visitLabel(self, ctx: AsmParser.LabelContext) -> LabelNode:
        return LabelNode(ctx.getText())

    def visitString(self, ctx: AsmParser.StringContext):
        s = ctx.getText()[1:-1]
        if '\\' in s:
            return self.handle_esc_seq(s, self._ctx_location(ctx))
        else:
            return s

    def visitCharacter(self, ctx: AsmParser.CharacterContext) -> str:
        loc = self._ctx_location(ctx)
        s = self.handle_esc_seq(ctx.getText()[1:-1], loc)
        if len(s) < 1:
            raise AssemblerException(AssemblerExceptionTag.ASM, loc.file, loc.line,
                                     "Empty character constant")
        elif len(s) > 1:
            raise AssemblerException(AssemblerExceptionTag.ASM, loc.file, loc.line,
                                     "Multi-character character constant")
        return s

    @staticmethod
    def handle_esc_seq(s: str, loc: CodeLocation):
        x: str
        warnings.filterwarnings("error")
        try:
            x = codecs.unicode_escape_decode(s)[0]
        except DeprecationWarning as e:
            raise AssemblerException(AssemblerExceptionTag.ASM, loc.file, loc.line, str(e))
        except UnicodeDecodeError as e:
            raise AssemblerException(AssemblerExceptionTag.ASM, loc.file, loc.line, str(e))
        warnings.resetwarnings()
        return x

    def visitRegister(self, ctx: AsmParser.RegisterContext):
        return RegisterNode(int(ctx.getText()[1:]))

    def visitInstructionLine(self, ctx: AsmParser.InstructionLineContext) -> list[Node]:
        ret = []
        if ctx.labels_declaration() is not None:
            ret += self.visitLabels_declaration(ctx.labels_declaration())
        op = ctx.instruction().getText()
        self.generated |= op == DBG_SOURCE_INST
        args = self.visitArguments(ctx.arguments()) if ctx.arguments() is not None else []
        ret.append(InstructionNode(op, args))
        return ret

    def visitArguments(self, ctx: AsmParser.ArgumentsContext):
        return [self.visitArgument(i) for i in ctx.children if isinstance(i, AsmParser.ArgumentContext)]


Ren = RelocatableExpressionNode


def resolve_debug_locs(files: Mapping[int, str], sections: MutableSequence[SectionNode]) -> None:
    for section in sections:
        lines_iter = enumerate(iter(section.lines))
        loc_insts: list[int] = []

        for index, line_node in lines_iter:
            if not isinstance(line_node, InstructionNode) or line_node.mnemonic != DBG_LOC_INST:
                continue
            loc_insts.append(index)
            match line_node.arguments:
                case [Ren(_, _, _, file), Ren(_, _, _, line), Ren(_, _, _, column)]:
                    if (path := files.get(file)) is None:
                        raise AssemblerException(AssemblerExceptionTag.ASM, line_node.location.file,
                                                 line_node.location.column,
                                                 f"{DBG_LOC_INST} refers to file with index {file}; where is no {DBG_SOURCE_INST} with such index")
                    current_loc = CodeLocation(path, line, column)
                case _:
                    raise AssemblerException(AssemblerExceptionTag.ASM, line_node.location.file,
                                             line_node.location.column,
                                             f"{DBG_LOC_INST} expects a number and a string, while {line_node.arguments} provided")

            _, next_line_node = next(lines_iter, (None, None))
            if next_line_node is None:
                raise AssemblerException(AssemblerExceptionTag.ASM, line_node.location.file, line_node.location.column,
                                         f"expected an instruction line after {DBG_LOC_INST}, while it's missing")
            if not isinstance(next_line_node, InstructionNode):
                raise AssemblerException(AssemblerExceptionTag.ASM, line_node.location.file, line_node.location.column,
                                         f"expected an instruction line after {DBG_LOC_INST}, while {type(next_line_node)} has been found")
            if next_line_node.mnemonic == DBG_LOC_INST:
                raise AssemblerException(AssemblerExceptionTag.ASM, line_node.location.file, line_node.location.column,
                                         f"there are two consecutive {DBG_LOC_INST} instructions; there is no point to do that")
            next_line_node.location = current_loc

        for index in reversed(loc_insts):
            _ = section.lines.pop(index)


def resolve_debug_pseudos(pn: ProgramNode) -> None:
    files: dict[int, str] = {}
    source_insts: list[int] = []

    for index, ti in enumerate(pn.top_instructions):
        if ti.mnemonic != DBG_SOURCE_INST:
            continue
        match ti.arguments:
            case [Ren(_, _, _, index), str() as path]:
                if index in files:
                    raise AssemblerException(AssemblerExceptionTag.ASM, ti.location.file, ti.location.column,
                                             f"duplicate {DBG_SOURCE_INST} for index {index}")
                files[index] = path
            case _:
                raise AssemblerException(AssemblerExceptionTag.ASM, ti.location.file, ti.location.column,
                                         f"{DBG_SOURCE_INST} expects a number and a string, while {ti.arguments} provided")
        source_insts.append(index)

    for index in reversed(source_insts):
        _ = pn.top_instructions.pop(index)

    resolve_debug_locs(files, cast(list[SectionNode], pn.absolute_sections))
    resolve_debug_locs(files, cast(list[SectionNode], pn.relocatable_sections))


def build_ast(input_stream: InputStream, filepath: Path) -> ProgramNode:
    str_path = filepath.absolute().as_posix()
    lexer = AsmLexer(input_stream)
    lexer.removeErrorListeners()
    lexer.addErrorListener(AntlrErrorListener(AssemblerExceptionTag.ASM, str_path))
    token_stream = CommonTokenStream(lexer)
    token_stream.fill()
    parser = AsmParser(token_stream)
    parser.removeErrorListeners()
    parser.addErrorListener(AntlrErrorListener(AssemblerExceptionTag.ASM, str_path))
    cst = parser.program()
    bav = BuildAstVisitor(str_path)
    result = bav.visit(cst)
    if not isinstance(result, ProgramNode):
        raise AssemblerException(AssemblerExceptionTag.ASM, str_path, 0,
                                 "failed to build a program AST from provided code")
    resolve_debug_pseudos(result)
    return result
