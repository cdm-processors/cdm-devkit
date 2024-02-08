from base64 import b64decode
from pathlib import Path

from antlr4 import CommonTokenStream, InputStream

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
    ProgramNode,
    RegisterNode,
    RelocatableExpressionNode,
    RelocatableSectionNode,
    TemplateFieldNode,
    TemplateSectionNode,
    UntilLoopNode,
    WhileLoopNode,
)
from .exceptions import AntlrErrorListener, AsmExceptionTag, AssemblerException
from .generated import AsmLexer, AsmParser, AsmParserVisitor


# noinspection PyPep8Naming
class BuildAstVisitor(AsmParserVisitor):
    def __init__(self, filepath: str):
        super().__init__()
        self.line_offset = 0
        # self.line_offset = 0
        self.source_path = filepath
        self.line_offset = 0
        self.in_macro = False
        self.current_macro_file = ""
        self.current_macro_line = 0

    def _ctx_location(self, ctx) -> CodeLocation:
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
        return ret

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

    def visitCharacter(self, ctx: AsmParser.CharacterContext) -> int:
        if ctx.getText()[1] == '\\':
            return ord(ctx.getText()[2])
        else:
            return ord(ctx.getText()[1])

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
            raise AssemblerException(AsmExceptionTag.ASM, self.source_path, ctx.start.line - self.line_offset,
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
            if isinstance(c, AsmParser.StandaloneLabelContext):
                nodes.append(self.visitStandaloneLabel(c))
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

    def visitStandaloneLabel(self, ctx: AsmParser.StandaloneLabelContext) -> LabelDeclarationNode:
        label_decl = self.visitLabel_declaration(ctx.label_declaration())
        label_decl.external = ctx.Ext() is not None
        if label_decl.entry and label_decl.external:
            raise AssemblerException(AsmExceptionTag.ASM, self.source_path, ctx.start.line - self.line_offset,
                                        f'Label {label_decl.label.name} cannot be both external and entry')
        return label_decl

    def visitLabel_declaration(self, ctx: AsmParser.Label_declarationContext) -> LabelDeclarationNode:
        is_entry = ctx.ANGLE_BRACKET() is not None
        return LabelDeclarationNode(self.visitLabel(ctx.label()), is_entry, False)

    def visitLabel(self, ctx: AsmParser.LabelContext) -> LabelNode:
        return LabelNode(ctx.getText())

    def visitString(self, ctx: AsmParser.StringContext):
        return ctx.getText()[1:-1]

    def visitRegister(self, ctx: AsmParser.RegisterContext):
        return RegisterNode(int(ctx.getText()[1:]))

    def visitTemplate_field(self, ctx: AsmParser.Template_fieldContext):
        template_name = ctx.name()[0].getText()
        field_name = ctx.name()[1].getText()
        return TemplateFieldNode(template_name, field_name)

    def visitInstructionLine(self, ctx: AsmParser.InstructionLineContext) -> list:
        ret = []
        if ctx.label_declaration() is not None:
            ret.append(self.visitLabel_declaration(ctx.label_declaration()))
        op = ctx.instruction().getText()
        args = self.visitArguments(ctx.arguments()) if ctx.arguments() is not None else []
        ret.append(InstructionNode(op, args))
        return ret

    def visitArguments(self, ctx: AsmParser.ArgumentsContext):
        return [self.visitArgument(i) for i in ctx.children if isinstance(i, AsmParser.ArgumentContext)]


def build_ast(input_stream: InputStream, filepath: Path):
    str_path = filepath.absolute().as_posix()
    lexer = AsmLexer(input_stream)
    lexer.removeErrorListeners()
    lexer.addErrorListener(AntlrErrorListener(AsmExceptionTag.ASM, str_path))
    token_stream = CommonTokenStream(lexer)
    token_stream.fill()
    parser = AsmParser(token_stream)
    parser.removeErrorListeners()
    parser.addErrorListener(AntlrErrorListener(AsmExceptionTag.ASM, str_path))
    cst = parser.program()
    bav = BuildAstVisitor(str_path)
    result = bav.visit(cst)
    return result
