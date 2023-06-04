# Generated from ./grammar/ObjectFile.g4 by ANTLR 4.13.0
from antlr4 import *
if "." in __name__:
    from .ObjectFileParser import ObjectFileParser
else:
    from ObjectFileParser import ObjectFileParser

# This class defines a complete generic visitor for a parse tree produced by ObjectFileParser.

class ObjectFileVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by ObjectFileParser#object_file.
    def visitObject_file(self, ctx:ObjectFileParser.Object_fileContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ObjectFileParser#asect_block.
    def visitAsect_block(self, ctx:ObjectFileParser.Asect_blockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ObjectFileParser#rsect_block.
    def visitRsect_block(self, ctx:ObjectFileParser.Rsect_blockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ObjectFileParser#abs_record.
    def visitAbs_record(self, ctx:ObjectFileParser.Abs_recordContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ObjectFileParser#ntry_record.
    def visitNtry_record(self, ctx:ObjectFileParser.Ntry_recordContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ObjectFileParser#name_record.
    def visitName_record(self, ctx:ObjectFileParser.Name_recordContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ObjectFileParser#alig_record.
    def visitAlig_record(self, ctx:ObjectFileParser.Alig_recordContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ObjectFileParser#data_record.
    def visitData_record(self, ctx:ObjectFileParser.Data_recordContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ObjectFileParser#rel_record.
    def visitRel_record(self, ctx:ObjectFileParser.Rel_recordContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ObjectFileParser#xtrn_record.
    def visitXtrn_record(self, ctx:ObjectFileParser.Xtrn_recordContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ObjectFileParser#data.
    def visitData(self, ctx:ObjectFileParser.DataContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ObjectFileParser#entry_usage.
    def visitEntry_usage(self, ctx:ObjectFileParser.Entry_usageContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ObjectFileParser#byte.
    def visitByte(self, ctx:ObjectFileParser.ByteContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ObjectFileParser#range.
    def visitRange(self, ctx:ObjectFileParser.RangeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ObjectFileParser#number.
    def visitNumber(self, ctx:ObjectFileParser.NumberContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ObjectFileParser#label.
    def visitLabel(self, ctx:ObjectFileParser.LabelContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ObjectFileParser#name.
    def visitName(self, ctx:ObjectFileParser.NameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ObjectFileParser#minus.
    def visitMinus(self, ctx:ObjectFileParser.MinusContext):
        return self.visitChildren(ctx)



del ObjectFileParser