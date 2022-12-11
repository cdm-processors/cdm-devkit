# Generated from /home/ilya/work/cdm8e/ORiGinalASM/cocas/AsmParser.g4 by ANTLR 4.10.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from cocas.generated.AsmParser import AsmParser
else:
    from AsmParser import AsmParser

from base64 import b64decode


# This class defines a complete listener for a parse tree produced by AsmParser.
class AsmParserListener(ParseTreeListener):

    # Enter a parse tree produced by AsmParser#program.
    def enterProgram(self, ctx:AsmParser.ProgramContext):
        pass

    # Exit a parse tree produced by AsmParser#program.
    def exitProgram(self, ctx:AsmParser.ProgramContext):
        pass


    # Enter a parse tree produced by AsmParser#absoluteSection.
    def enterAbsoluteSection(self, ctx:AsmParser.AbsoluteSectionContext):
        pass

    # Exit a parse tree produced by AsmParser#absoluteSection.
    def exitAbsoluteSection(self, ctx:AsmParser.AbsoluteSectionContext):
        pass


    # Enter a parse tree produced by AsmParser#relocatableSection.
    def enterRelocatableSection(self, ctx:AsmParser.RelocatableSectionContext):
        pass

    # Exit a parse tree produced by AsmParser#relocatableSection.
    def exitRelocatableSection(self, ctx:AsmParser.RelocatableSectionContext):
        pass


    # Enter a parse tree produced by AsmParser#templateSection.
    def enterTemplateSection(self, ctx:AsmParser.TemplateSectionContext):
        pass

    # Exit a parse tree produced by AsmParser#templateSection.
    def exitTemplateSection(self, ctx:AsmParser.TemplateSectionContext):
        pass


    # Enter a parse tree produced by AsmParser#asect_header.
    def enterAsect_header(self, ctx:AsmParser.Asect_headerContext):
        pass

    # Exit a parse tree produced by AsmParser#asect_header.
    def exitAsect_header(self, ctx:AsmParser.Asect_headerContext):
        pass


    # Enter a parse tree produced by AsmParser#rsect_header.
    def enterRsect_header(self, ctx:AsmParser.Rsect_headerContext):
        pass

    # Exit a parse tree produced by AsmParser#rsect_header.
    def exitRsect_header(self, ctx:AsmParser.Rsect_headerContext):
        pass


    # Enter a parse tree produced by AsmParser#tplate_header.
    def enterTplate_header(self, ctx:AsmParser.Tplate_headerContext):
        pass

    # Exit a parse tree produced by AsmParser#tplate_header.
    def exitTplate_header(self, ctx:AsmParser.Tplate_headerContext):
        pass


    # Enter a parse tree produced by AsmParser#section_body.
    def enterSection_body(self, ctx:AsmParser.Section_bodyContext):
        pass

    # Exit a parse tree produced by AsmParser#section_body.
    def exitSection_body(self, ctx:AsmParser.Section_bodyContext):
        pass


    # Enter a parse tree produced by AsmParser#code_block.
    def enterCode_block(self, ctx:AsmParser.Code_blockContext):
        pass

    # Exit a parse tree produced by AsmParser#code_block.
    def exitCode_block(self, ctx:AsmParser.Code_blockContext):
        pass


    # Enter a parse tree produced by AsmParser#line_mark.
    def enterLine_mark(self, ctx:AsmParser.Line_markContext):
        pass

    # Exit a parse tree produced by AsmParser#line_mark.
    def exitLine_mark(self, ctx:AsmParser.Line_markContext):
        pass


    # Enter a parse tree produced by AsmParser#line_number.
    def enterLine_number(self, ctx:AsmParser.Line_numberContext):
        pass

    # Exit a parse tree produced by AsmParser#line_number.
    def exitLine_number(self, ctx:AsmParser.Line_numberContext):
        pass


    # Enter a parse tree produced by AsmParser#filepath.
    def enterFilepath(self, ctx:AsmParser.FilepathContext):
        pass

    # Exit a parse tree produced by AsmParser#filepath.
    def exitFilepath(self, ctx:AsmParser.FilepathContext):
        pass


    # Enter a parse tree produced by AsmParser#break_statement.
    def enterBreak_statement(self, ctx:AsmParser.Break_statementContext):
        pass

    # Exit a parse tree produced by AsmParser#break_statement.
    def exitBreak_statement(self, ctx:AsmParser.Break_statementContext):
        pass


    # Enter a parse tree produced by AsmParser#continue_statement.
    def enterContinue_statement(self, ctx:AsmParser.Continue_statementContext):
        pass

    # Exit a parse tree produced by AsmParser#continue_statement.
    def exitContinue_statement(self, ctx:AsmParser.Continue_statementContext):
        pass


    # Enter a parse tree produced by AsmParser#standaloneLabel.
    def enterStandaloneLabel(self, ctx:AsmParser.StandaloneLabelContext):
        pass

    # Exit a parse tree produced by AsmParser#standaloneLabel.
    def exitStandaloneLabel(self, ctx:AsmParser.StandaloneLabelContext):
        pass


    # Enter a parse tree produced by AsmParser#instructionLine.
    def enterInstructionLine(self, ctx:AsmParser.InstructionLineContext):
        pass

    # Exit a parse tree produced by AsmParser#instructionLine.
    def exitInstructionLine(self, ctx:AsmParser.InstructionLineContext):
        pass


    # Enter a parse tree produced by AsmParser#label_declaration.
    def enterLabel_declaration(self, ctx:AsmParser.Label_declarationContext):
        pass

    # Exit a parse tree produced by AsmParser#label_declaration.
    def exitLabel_declaration(self, ctx:AsmParser.Label_declarationContext):
        pass


    # Enter a parse tree produced by AsmParser#arguments.
    def enterArguments(self, ctx:AsmParser.ArgumentsContext):
        pass

    # Exit a parse tree produced by AsmParser#arguments.
    def exitArguments(self, ctx:AsmParser.ArgumentsContext):
        pass


    # Enter a parse tree produced by AsmParser#conditional.
    def enterConditional(self, ctx:AsmParser.ConditionalContext):
        pass

    # Exit a parse tree produced by AsmParser#conditional.
    def exitConditional(self, ctx:AsmParser.ConditionalContext):
        pass


    # Enter a parse tree produced by AsmParser#conditions.
    def enterConditions(self, ctx:AsmParser.ConditionsContext):
        pass

    # Exit a parse tree produced by AsmParser#conditions.
    def exitConditions(self, ctx:AsmParser.ConditionsContext):
        pass


    # Enter a parse tree produced by AsmParser#connective_condition.
    def enterConnective_condition(self, ctx:AsmParser.Connective_conditionContext):
        pass

    # Exit a parse tree produced by AsmParser#connective_condition.
    def exitConnective_condition(self, ctx:AsmParser.Connective_conditionContext):
        pass


    # Enter a parse tree produced by AsmParser#condition.
    def enterCondition(self, ctx:AsmParser.ConditionContext):
        pass

    # Exit a parse tree produced by AsmParser#condition.
    def exitCondition(self, ctx:AsmParser.ConditionContext):
        pass


    # Enter a parse tree produced by AsmParser#else_clause.
    def enterElse_clause(self, ctx:AsmParser.Else_clauseContext):
        pass

    # Exit a parse tree produced by AsmParser#else_clause.
    def exitElse_clause(self, ctx:AsmParser.Else_clauseContext):
        pass


    # Enter a parse tree produced by AsmParser#branch_mnemonic.
    def enterBranch_mnemonic(self, ctx:AsmParser.Branch_mnemonicContext):
        pass

    # Exit a parse tree produced by AsmParser#branch_mnemonic.
    def exitBranch_mnemonic(self, ctx:AsmParser.Branch_mnemonicContext):
        pass


    # Enter a parse tree produced by AsmParser#conjunction.
    def enterConjunction(self, ctx:AsmParser.ConjunctionContext):
        pass

    # Exit a parse tree produced by AsmParser#conjunction.
    def exitConjunction(self, ctx:AsmParser.ConjunctionContext):
        pass


    # Enter a parse tree produced by AsmParser#while_loop.
    def enterWhile_loop(self, ctx:AsmParser.While_loopContext):
        pass

    # Exit a parse tree produced by AsmParser#while_loop.
    def exitWhile_loop(self, ctx:AsmParser.While_loopContext):
        pass


    # Enter a parse tree produced by AsmParser#while_condition.
    def enterWhile_condition(self, ctx:AsmParser.While_conditionContext):
        pass

    # Exit a parse tree produced by AsmParser#while_condition.
    def exitWhile_condition(self, ctx:AsmParser.While_conditionContext):
        pass


    # Enter a parse tree produced by AsmParser#until_loop.
    def enterUntil_loop(self, ctx:AsmParser.Until_loopContext):
        pass

    # Exit a parse tree produced by AsmParser#until_loop.
    def exitUntil_loop(self, ctx:AsmParser.Until_loopContext):
        pass


    # Enter a parse tree produced by AsmParser#save_restore_statement.
    def enterSave_restore_statement(self, ctx:AsmParser.Save_restore_statementContext):
        pass

    # Exit a parse tree produced by AsmParser#save_restore_statement.
    def exitSave_restore_statement(self, ctx:AsmParser.Save_restore_statementContext):
        pass


    # Enter a parse tree produced by AsmParser#save_statement.
    def enterSave_statement(self, ctx:AsmParser.Save_statementContext):
        pass

    # Exit a parse tree produced by AsmParser#save_statement.
    def exitSave_statement(self, ctx:AsmParser.Save_statementContext):
        pass


    # Enter a parse tree produced by AsmParser#restore_statement.
    def enterRestore_statement(self, ctx:AsmParser.Restore_statementContext):
        pass

    # Exit a parse tree produced by AsmParser#restore_statement.
    def exitRestore_statement(self, ctx:AsmParser.Restore_statementContext):
        pass


    # Enter a parse tree produced by AsmParser#goto_statement.
    def enterGoto_statement(self, ctx:AsmParser.Goto_statementContext):
        pass

    # Exit a parse tree produced by AsmParser#goto_statement.
    def exitGoto_statement(self, ctx:AsmParser.Goto_statementContext):
        pass


    # Enter a parse tree produced by AsmParser#goto_argument.
    def enterGoto_argument(self, ctx:AsmParser.Goto_argumentContext):
        pass

    # Exit a parse tree produced by AsmParser#goto_argument.
    def exitGoto_argument(self, ctx:AsmParser.Goto_argumentContext):
        pass


    # Enter a parse tree produced by AsmParser#argument.
    def enterArgument(self, ctx:AsmParser.ArgumentContext):
        pass

    # Exit a parse tree produced by AsmParser#argument.
    def exitArgument(self, ctx:AsmParser.ArgumentContext):
        pass


    # Enter a parse tree produced by AsmParser#byte_expr.
    def enterByte_expr(self, ctx:AsmParser.Byte_exprContext):
        pass

    # Exit a parse tree produced by AsmParser#byte_expr.
    def exitByte_expr(self, ctx:AsmParser.Byte_exprContext):
        pass


    # Enter a parse tree produced by AsmParser#addr_expr.
    def enterAddr_expr(self, ctx:AsmParser.Addr_exprContext):
        pass

    # Exit a parse tree produced by AsmParser#addr_expr.
    def exitAddr_expr(self, ctx:AsmParser.Addr_exprContext):
        pass


    # Enter a parse tree produced by AsmParser#first_term.
    def enterFirst_term(self, ctx:AsmParser.First_termContext):
        pass

    # Exit a parse tree produced by AsmParser#first_term.
    def exitFirst_term(self, ctx:AsmParser.First_termContext):
        pass


    # Enter a parse tree produced by AsmParser#add_term.
    def enterAdd_term(self, ctx:AsmParser.Add_termContext):
        pass

    # Exit a parse tree produced by AsmParser#add_term.
    def exitAdd_term(self, ctx:AsmParser.Add_termContext):
        pass


    # Enter a parse tree produced by AsmParser#term.
    def enterTerm(self, ctx:AsmParser.TermContext):
        pass

    # Exit a parse tree produced by AsmParser#term.
    def exitTerm(self, ctx:AsmParser.TermContext):
        pass


    # Enter a parse tree produced by AsmParser#byte_specifier.
    def enterByte_specifier(self, ctx:AsmParser.Byte_specifierContext):
        pass

    # Exit a parse tree produced by AsmParser#byte_specifier.
    def exitByte_specifier(self, ctx:AsmParser.Byte_specifierContext):
        pass


    # Enter a parse tree produced by AsmParser#template_field.
    def enterTemplate_field(self, ctx:AsmParser.Template_fieldContext):
        pass

    # Exit a parse tree produced by AsmParser#template_field.
    def exitTemplate_field(self, ctx:AsmParser.Template_fieldContext):
        pass


    # Enter a parse tree produced by AsmParser#label.
    def enterLabel(self, ctx:AsmParser.LabelContext):
        pass

    # Exit a parse tree produced by AsmParser#label.
    def exitLabel(self, ctx:AsmParser.LabelContext):
        pass


    # Enter a parse tree produced by AsmParser#instruction.
    def enterInstruction(self, ctx:AsmParser.InstructionContext):
        pass

    # Exit a parse tree produced by AsmParser#instruction.
    def exitInstruction(self, ctx:AsmParser.InstructionContext):
        pass


    # Enter a parse tree produced by AsmParser#string.
    def enterString(self, ctx:AsmParser.StringContext):
        pass

    # Exit a parse tree produced by AsmParser#string.
    def exitString(self, ctx:AsmParser.StringContext):
        pass


    # Enter a parse tree produced by AsmParser#register.
    def enterRegister(self, ctx:AsmParser.RegisterContext):
        pass

    # Exit a parse tree produced by AsmParser#register.
    def exitRegister(self, ctx:AsmParser.RegisterContext):
        pass


    # Enter a parse tree produced by AsmParser#character.
    def enterCharacter(self, ctx:AsmParser.CharacterContext):
        pass

    # Exit a parse tree produced by AsmParser#character.
    def exitCharacter(self, ctx:AsmParser.CharacterContext):
        pass


    # Enter a parse tree produced by AsmParser#number.
    def enterNumber(self, ctx:AsmParser.NumberContext):
        pass

    # Exit a parse tree produced by AsmParser#number.
    def exitNumber(self, ctx:AsmParser.NumberContext):
        pass


    # Enter a parse tree produced by AsmParser#name.
    def enterName(self, ctx:AsmParser.NameContext):
        pass

    # Exit a parse tree produced by AsmParser#name.
    def exitName(self, ctx:AsmParser.NameContext):
        pass



del AsmParser