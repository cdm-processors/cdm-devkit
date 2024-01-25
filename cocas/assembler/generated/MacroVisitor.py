# Generated from assembler/grammar/Macro.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .MacroParser import MacroParser
else:
    from MacroParser import MacroParser

# This class defines a complete generic visitor for a parse tree produced by MacroParser.

class MacroVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by MacroParser#mlb.
    def visitMlb(self, ctx:MacroParser.MlbContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MacroParser#mlb_macro.
    def visitMlb_macro(self, ctx:MacroParser.Mlb_macroContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MacroParser#mlb_header.
    def visitMlb_header(self, ctx:MacroParser.Mlb_headerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MacroParser#program.
    def visitProgram(self, ctx:MacroParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MacroParser#macro.
    def visitMacro(self, ctx:MacroParser.MacroContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MacroParser#macro_header.
    def visitMacro_header(self, ctx:MacroParser.Macro_headerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MacroParser#macro_body.
    def visitMacro_body(self, ctx:MacroParser.Macro_bodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MacroParser#line.
    def visitLine(self, ctx:MacroParser.LineContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MacroParser#labels.
    def visitLabels(self, ctx:MacroParser.LabelsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MacroParser#first_param.
    def visitFirst_param(self, ctx:MacroParser.First_paramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MacroParser#label.
    def visitLabel(self, ctx:MacroParser.LabelContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MacroParser#param.
    def visitParam(self, ctx:MacroParser.ParamContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MacroParser#instruction.
    def visitInstruction(self, ctx:MacroParser.InstructionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MacroParser#l_sep.
    def visitL_sep(self, ctx:MacroParser.L_sepContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MacroParser#p_sep.
    def visitP_sep(self, ctx:MacroParser.P_sepContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MacroParser#macro_piece.
    def visitMacro_piece(self, ctx:MacroParser.Macro_pieceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MacroParser#macro_variable.
    def visitMacro_variable(self, ctx:MacroParser.Macro_variableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MacroParser#macro_text.
    def visitMacro_text(self, ctx:MacroParser.Macro_textContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MacroParser#macro_param.
    def visitMacro_param(self, ctx:MacroParser.Macro_paramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MacroParser#macro_nonce.
    def visitMacro_nonce(self, ctx:MacroParser.Macro_nonceContext):
        return self.visitChildren(ctx)



del MacroParser