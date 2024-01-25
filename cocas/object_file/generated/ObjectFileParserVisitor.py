# Generated from object_file/grammar/ObjectFileParser.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .ObjectFileParser import ObjectFileParser
else:
    from ObjectFileParser import ObjectFileParser

# This class defines a complete generic visitor for a parse tree produced by ObjectFileParser.

class ObjectFileParserVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by ObjectFileParser#object_file.
    def visitObject_file(self, ctx:ObjectFileParser.Object_fileContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ObjectFileParser#object_block.
    def visitObject_block(self, ctx:ObjectFileParser.Object_blockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ObjectFileParser#asect_block.
    def visitAsect_block(self, ctx:ObjectFileParser.Asect_blockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ObjectFileParser#abs_block.
    def visitAbs_block(self, ctx:ObjectFileParser.Abs_blockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ObjectFileParser#rsect_block.
    def visitRsect_block(self, ctx:ObjectFileParser.Rsect_blockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ObjectFileParser#targ_record.
    def visitTarg_record(self, ctx:ObjectFileParser.Targ_recordContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ObjectFileParser#source_record.
    def visitSource_record(self, ctx:ObjectFileParser.Source_recordContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ObjectFileParser#abs_record.
    def visitAbs_record(self, ctx:ObjectFileParser.Abs_recordContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ObjectFileParser#loc_record.
    def visitLoc_record(self, ctx:ObjectFileParser.Loc_recordContext):
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


    # Visit a parse tree produced by ObjectFileParser#filepath.
    def visitFilepath(self, ctx:ObjectFileParser.FilepathContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ObjectFileParser#entry_usage.
    def visitEntry_usage(self, ctx:ObjectFileParser.Entry_usageContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ObjectFileParser#range.
    def visitRange(self, ctx:ObjectFileParser.RangeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ObjectFileParser#location.
    def visitLocation(self, ctx:ObjectFileParser.LocationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ObjectFileParser#abs_address.
    def visitAbs_address(self, ctx:ObjectFileParser.Abs_addressContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ObjectFileParser#number.
    def visitNumber(self, ctx:ObjectFileParser.NumberContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ObjectFileParser#label.
    def visitLabel(self, ctx:ObjectFileParser.LabelContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ObjectFileParser#section.
    def visitSection(self, ctx:ObjectFileParser.SectionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ObjectFileParser#minus.
    def visitMinus(self, ctx:ObjectFileParser.MinusContext):
        return self.visitChildren(ctx)



del ObjectFileParser