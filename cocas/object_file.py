import bisect

from antlr4 import CommonTokenStream, InputStream

from cocas.abstract_params import TargetParamsInterface
from cocas.error import AntlrErrorListener, CdmException, CdmExceptionTag
from cocas.external_entry import ExternalEntry
from cocas.generated.ObjectFileLexer import ObjectFileLexer
from cocas.generated.ObjectFileParser import ObjectFileParser
from cocas.generated.ObjectFileVisitor import ObjectFileVisitor
from cocas.object_module import ObjectModule, ObjectSectionRecord


class ImportObjectFileVisitor(ObjectFileVisitor):
    def __init__(self, filepath, target_params: TargetParamsInterface):
        super().__init__()
        self.file = filepath
        self.target_params = target_params

    def visitObject_file(self, ctx: ObjectFileParser.Object_fileContext):
        asects, asect_addr = self.visitAsect_block(ctx.asect_block())
        rsects = {}
        for block in ctx.rsect_block():
            name, rsect = self.visitRsect_block(block)
            if name in rsects:
                raise CdmException(CdmExceptionTag.OBJ, self.file, block.start.line,
                                   f'Repeating section: {name}')
            rsects[name] = rsect

        i: ObjectFileParser.Xtrn_recordContext
        for i in ctx.xtrn_record():
            label, entries = self.visitXtrn_record(i)
            for sect, entry in entries:
                if sect == '$abs':
                    if not asects:
                        raise CdmException(CdmExceptionTag.OBJ, self.file, i.start.line,
                                           'No absolute sections found')
                    ind = max(bisect.bisect_right(asect_addr, entry.offset) - 1, 0)
                    asects[asect_addr[ind]].external[label].append(entry)
                elif sect in rsects:
                    rsects[sect].external[label].append(entry)
                else:
                    raise CdmException(CdmExceptionTag.OBJ, self.file, i.start.line,
                                       f'Section not found: {sect}')
        om = ObjectModule()
        om.asects = list(asects.values())
        om.rsects = list(rsects.values())
        return om

    def visitAsect_block(self, ctx: ObjectFileParser.Asect_blockContext):
        asects = {}
        for addr, record in map(self.visitAbs_record, ctx.abs_record()):
            asects[addr] = record
        if not asects and ctx.ntry_record():
            asects[0] = ObjectSectionRecord('$abs', 0, bytearray(), {}, [], {}, 1)
        asect_addr = sorted(asects.keys())
        for label, addr in map(self.visitNtry_record, ctx.ntry_record()):
            ind = max(bisect.bisect_right(asect_addr, addr) - 1, 0)
            asects[asect_addr[ind]].entries[label] = addr
        return asects, asect_addr

    def visitRsect_block(self, ctx: ObjectFileParser.Rsect_blockContext):
        name = self.visitName_record(ctx.name_record())
        if ctx.alig_record():
            align = self.visitAlig_record(ctx.alig_record())
        else:
            align = self.target_params.default_alignment()
        data = self.visitData_record(ctx.data_record())
        rel = self.visitRel_record(ctx.rel_record())
        entries = {}
        for label, address in map(self.visitNtry_record, ctx.ntry_record()):
            entries[label] = address
        return name, ObjectSectionRecord(name, 0, data, entries, rel, {}, align)

    def visitAbs_record(self, ctx: ObjectFileParser.Abs_recordContext):
        addr = self.visitNumber(ctx.number())
        data = self.visitData(ctx.data())
        return addr, ObjectSectionRecord('$abs', addr, data, {}, [], {})

    def visitNtry_record(self, ctx: ObjectFileParser.Ntry_recordContext):
        label = self.visitLabel(ctx.label())
        address = self.visitNumber(ctx.number())
        return label, address

    def visitName_record(self, ctx: ObjectFileParser.Name_recordContext):
        return self.visitName(ctx.name())

    def visitAlig_record(self, ctx: ObjectFileParser.Alig_recordContext):
        return self.visitNumber(ctx.number())

    def visitData_record(self, ctx: ObjectFileParser.Data_recordContext):
        return self.visitData(ctx.data())

    def visitRel_record(self, ctx: ObjectFileParser.Rel_recordContext):
        return [self.visitEntry_usage(eu) for eu in ctx.entry_usage()]

    def visitXtrn_record(self, ctx: ObjectFileParser.Xtrn_recordContext):
        label = self.visitLabel(ctx.label())
        entries = [(self.visitName(n), self.visitEntry_usage(e))
                   for (n, e) in zip(ctx.name(), ctx.entry_usage())]
        return label, entries

    def visitData(self, ctx: ObjectFileParser.DataContext):
        return bytearray(map(self.visitByte, ctx.byte()))

    def visitNumber(self, ctx: ObjectFileParser.NumberContext):
        try:
            return int(ctx.getText(), 16)
        except ValueError:
            raise CdmException(CdmExceptionTag.OBJ, self.file, ctx.start.line,
                               f'Not a 16-bit number: {ctx.getText()}')

    def visitByte(self, ctx: ObjectFileParser.ByteContext):
        num = self.visitNumber(ctx.number())
        if num > 255:
            raise CdmException(CdmExceptionTag.OBJ, self.file, ctx.start.line,
                               f'Too big number {ctx.getText()}, expected byte')
        return num

    def visitEntry_usage(self, ctx: ObjectFileParser.Entry_usageContext):
        addr = self.visitNumber(ctx.number())
        sign = -1 if ctx.minus() else 1
        if ctx.range_():
            return ExternalEntry(addr, self.visitRange(ctx.range_()), sign, False)
        else:
            entry_size = self.target_params.max_entry_size()
            return ExternalEntry(addr, range(0, entry_size), sign, True)

    def visitRange(self, ctx: ObjectFileParser.RangeContext):
        return range(self.visitNumber(ctx.number(0)), self.visitNumber(ctx.number(1)))

    def visitLabel(self, ctx: ObjectFileParser.LabelContext):
        return ctx.getText()

    def visitName(self, ctx: ObjectFileParser.NameContext):
        return ctx.getText()

    def visitMinus(self, ctx: ObjectFileParser.MinusContext):
        pass


def import_object(input_stream: InputStream, filepath: str,
                  target_params: TargetParamsInterface) -> ObjectModule:
    lexer = ObjectFileLexer(input_stream)
    lexer.removeErrorListeners()
    lexer.addErrorListener(AntlrErrorListener(CdmExceptionTag.OBJ, filepath))
    token_stream = CommonTokenStream(lexer)
    token_stream.fill()
    parser = ObjectFileParser(token_stream)
    parser.removeErrorListeners()
    parser.addErrorListener(AntlrErrorListener(CdmExceptionTag.OBJ, filepath))
    ctx = parser.object_file()
    visitor = ImportObjectFileVisitor(filepath, target_params)
    result = visitor.visit(ctx)
    return result