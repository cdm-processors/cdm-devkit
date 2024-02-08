import bisect
import codecs
from pathlib import Path
from typing import List, Optional, Union

import antlr4
from antlr4 import CommonTokenStream, InputStream

from cocas.object_module import CodeLocation, ExternalEntry, ObjectModule, ObjectSectionRecord

from .exceptions import AntlrErrorListener, CdmObjectFileException
from .generated.ObjectFileLexer import ObjectFileLexer
from .generated.ObjectFileParser import ObjectFileParser
from .generated.ObjectFileParserVisitor import ObjectFileParserVisitor
from .targets import TargetParams, import_target


class ImportObjectFileVisitor(ObjectFileParserVisitor):
    def __init__(self, filepath, target: str):
        super().__init__()
        self.file = filepath
        self.target_params: TargetParams = import_target(target)

    def visitObject_file(self, ctx: ObjectFileParser.Object_fileContext) -> list[ObjectModule]:
        exp_header = self.target_params.header
        target_name = self.target_params.name
        if ctx.targ_record():
            header = self.visitTarg_record(ctx.targ_record())
            if header != exp_header:
                if exp_header:
                    raise CdmObjectFileException(self.file, ctx.start.line,
                                                 f'Wrong target header {header}, expected {exp_header}')
                else:
                    raise CdmObjectFileException(self.file, ctx.start.line,
                                                 f'Expected no header for {target_name} target, got {header}')
        elif exp_header:
            raise CdmObjectFileException(self.file, ctx.start.line,
                                         f'Expected non-empty target header for {target_name}, got empty')

        modules = []
        for i in ctx.object_block():
            modules.append(self.visitObject_block(i))
        return modules

    def visitObject_block(self, ctx: ObjectFileParser.Object_blockContext) -> ObjectModule:
        if ctx.source_record():
            filename = self.visitSource_record(ctx.source_record())
        else:
            filename = None

        if ctx.asect_block():
            asects, asect_addr = self.visitAsect_block(ctx.asect_block())
        else:
            asects, asect_addr = {}, []

        rsects = {}
        for block in ctx.rsect_block():
            name, rsect = self.visitRsect_block(block)
            if name in rsects:
                raise CdmObjectFileException(self.file, block.start.line, f'Repeating section: {name}')
            rsects[name] = rsect

        xtrn: ObjectFileParser.Xtrn_recordContext
        for xtrn in ctx.xtrn_record():
            label, entries = self.visitXtrn_record(xtrn)
            for sect, entry in entries:
                if sect == '$abs':
                    if not asects:
                        raise CdmObjectFileException(self.file, xtrn.start.line,
                                                     'No absolute sections found, but needed for xtrn entry')
                    # what is this?
                    ind = max(bisect.bisect_right(asect_addr, entry.offset) - 1, 0)
                    asects[asect_addr[ind]].external[label].append(entry)
                elif sect in rsects:
                    rsects[sect].external[label].append(entry)
                else:
                    raise CdmObjectFileException(self.file, xtrn.start.line, f'Section not found: {sect}')
        if filename:
            f = Path(filename)
            for i in (asects | rsects).values():
                for j in i.code_locations.values():
                    j.file = f.as_posix()
            om = ObjectModule(list(asects.values()), list(rsects.values()), f)
        else:
            for i in (asects | rsects).values():
                i.code_locations = {}
            om = ObjectModule(list(asects.values()), list(rsects.values()), None)
        return om

    def visitAsect_block(self, ctx: ObjectFileParser.Asect_blockContext):
        asects = {}
        for addr, record in map(self.visitAbs_block, ctx.abs_block()):
            asects[addr] = record
        if not asects and ctx.ntry_record():
            asects[0] = ObjectSectionRecord('$abs', 0, bytearray(), {}, [], {}, 1)
        asect_addr = sorted(asects.keys())
        for label, addr in map(self.visitNtry_record, ctx.ntry_record()):
            ind = max(bisect.bisect_right(asect_addr, addr) - 1, 0)
            asects[asect_addr[ind]].entries[label] = addr
        return asects, asect_addr

    def visitAbs_block(self, ctx: ObjectFileParser.Abs_blockContext):
        addr, asect = self.visitAbs_record(ctx.abs_record())
        for cl in map(self.visitLoc_record, ctx.loc_record()):
            for byte, loc in cl.items():
                asect.code_locations[byte] = loc
        return addr, asect

    def visitRsect_block(self, ctx: ObjectFileParser.Rsect_blockContext):
        name = self.visitName_record(ctx.name_record())
        if ctx.alig_record():
            align = self.visitAlig_record(ctx.alig_record())
        else:
            align = self.target_params.default_alignment
        data = self.visitData_record(ctx.data_record())
        if ctx.rel_record():
            rel = self.visitRel_record(ctx.rel_record())
        else:
            rel = []
        entries = {}
        for label, address in map(self.visitNtry_record, ctx.ntry_record()):
            entries[label] = address
        code_locations = {}
        for cl in map(self.visitLoc_record, ctx.loc_record()):
            code_locations |= cl
        return name, ObjectSectionRecord(name, 0, data, entries, rel, code_locations, align)

    def visitTarg_record(self, ctx: ObjectFileParser.Targ_recordContext):
        return self.visitLabel(ctx.label())

    def visitSource_record(self, ctx: ObjectFileParser.Source_recordContext):
        return self.visitFilepath(ctx.filepath())

    def visitAbs_record(self, ctx: ObjectFileParser.Abs_recordContext):
        addr = self.visitNumber(ctx.abs_address())
        data = self.visitData(ctx.data())
        return addr, ObjectSectionRecord('$abs', addr, data, {}, [], {})

    def visitLoc_record(self, ctx: ObjectFileParser.Loc_recordContext):
        res = {}
        for byte, line, col in map(self.visitLocation, ctx.location()):
            res[byte] = CodeLocation(None, line, col)
        return res

    def visitNtry_record(self, ctx: ObjectFileParser.Ntry_recordContext):
        label = self.visitLabel(ctx.label())
        address = self.visitNumber(ctx.number())
        return label, address

    def visitName_record(self, ctx: ObjectFileParser.Name_recordContext):
        return self.visitSection(ctx.section())

    def visitAlig_record(self, ctx: ObjectFileParser.Alig_recordContext):
        return self.visitNumber(ctx.number())

    def visitData_record(self, ctx: ObjectFileParser.Data_recordContext):
        return self.visitData(ctx.data())

    def visitFilepath(self, ctx: ObjectFileParser.FilepathContext):
        return ctx.getText()

    def visitRel_record(self, ctx: ObjectFileParser.Rel_recordContext):
        return [self.visitEntry_usage(eu) for eu in ctx.entry_usage()]

    def visitXtrn_record(self, ctx: ObjectFileParser.Xtrn_recordContext):
        label = self.visitLabel(ctx.label())
        entries = [(self.visitSection(n), self.visitEntry_usage(e))
                   for (n, e) in zip(ctx.section(), ctx.entry_usage())]
        return label, entries

    def parse_byte(self, byte: str, ctx: ObjectFileParser.DataContext):
        try:
            value = int(byte, 16)
        except ValueError:
            raise CdmObjectFileException(self.file, ctx.start.line, f'Not a hex number: {byte}')
        if not 0 <= value <= 255:
            raise CdmObjectFileException(self.file, ctx.start.line, f'To big hex number: {byte}, expected byte')
        return value

    def visitData(self, ctx: ObjectFileParser.DataContext):
        return bytearray(map(lambda x: self.parse_byte(x, ctx), ctx.getText().split()))

    def visitAbs_address(self, ctx: ObjectFileParser.Abs_addressContext):
        try:
            return int(ctx.getText(), 16)
        except ValueError:
            raise CdmObjectFileException(self.file, ctx.start.line, f'Not a hex number: {ctx.getText()}')

    def visitNumber(self, ctx: ObjectFileParser.NumberContext):
        try:
            return int(ctx.getText(), 16)
        except ValueError:
            raise CdmObjectFileException(self.file, ctx.start.line, f'Not a hex number: {ctx.getText()}')

    def visitEntry_usage(self, ctx: ObjectFileParser.Entry_usageContext):
        addr = self.visitNumber(ctx.number())
        sign = -1 if ctx.minus() else 1
        if ctx.range_():
            return ExternalEntry(addr, self.visitRange(ctx.range_()), sign, False)
        else:
            entry_size = self.target_params.max_entry_size
            return ExternalEntry(addr, range(0, entry_size), sign, True)

    def visitRange(self, ctx: ObjectFileParser.RangeContext):
        return range(self.visitNumber(ctx.number(0)), self.visitNumber(ctx.number(1)))

    def visitLocation(self, ctx: ObjectFileParser.LocationContext):
        return self.visitNumber(ctx.number(0)), self.visitNumber(ctx.number(1)), \
            self.visitNumber(ctx.number(2))

    def visitLabel(self, ctx: ObjectFileParser.LabelContext):
        return ctx.getText()

    def visitSection(self, ctx: ObjectFileParser.SectionContext):
        return ctx.getText()

    def visitMinus(self, ctx: ObjectFileParser.MinusContext):
        pass


def import_object(input_stream: InputStream, filepath: Path,
                  target: str) -> List[ObjectModule]:
    str_path = filepath.absolute().as_posix()
    lexer = ObjectFileLexer(input_stream)
    lexer.removeErrorListeners()
    lexer.addErrorListener(AntlrErrorListener(str_path))
    token_stream = CommonTokenStream(lexer)
    token_stream.fill()
    parser = ObjectFileParser(token_stream)
    parser.removeErrorListeners()
    parser.addErrorListener(AntlrErrorListener(str_path))
    ctx = parser.object_file()
    visitor = ImportObjectFileVisitor(str_path, target)
    result = visitor.visit(ctx)
    return result


def read_object_files(target: str,
                      files: list[Union[str, Path]],
                      debug: bool,
                      relative_path: Optional[Path],
                      absolute_path: Optional[Path],
                      realpath: bool) -> list[tuple[Path, ObjectModule]]:
    """
    :param target: name of processor target
    :param files: list of object files' paths to process
    :param debug: if debug information should be exported
    :param relative_path: if debug paths should be converted to relative to some path
    :param absolute_path: if relative paths should be converted to absolute
    :param realpath: if paths should be converted to canonical
    """
    _ = debug
    objects = []
    for filepath in files:
        with open(filepath, 'rb') as file:
            data = file.read()
        data = codecs.decode(data, 'utf8', 'strict')
        if not data.endswith('\n'):
            data += '\n'

        input_stream = antlr4.InputStream(data)
        for obj in import_object(input_stream, Path(filepath), target):
            if realpath:
                dip = obj.source_file_path
                obj.source_file_path = obj.source_file_path.resolve()
                for i in obj.asects + obj.rsects:
                    for j in i.code_locations.values():
                        f = Path(j.file)
                        if f == dip:
                            j.file = obj.source_file_path.as_posix()
                        else:
                            j.file = Path(j.file).resolve().as_posix()
            if relative_path:
                dip = obj.source_file_path
                if obj.source_file_path.is_absolute():
                    obj.source_file_path = obj.source_file_path.absolute().relative_to(relative_path)
                for i in obj.asects + obj.rsects:
                    for j in i.code_locations.values():
                        f = Path(j.file)
                        if f == dip:
                            j.file = obj.source_file_path.as_posix()
                        else:
                            if f.is_absolute():
                                j.file = f.absolute().relative_to(relative_path).as_posix()
            elif absolute_path:
                obj.source_file_path = absolute_path / obj.source_file_path
                if realpath:
                    obj.source_file_path = obj.source_file_path.resolve()
                for i in obj.asects + obj.rsects:
                    for j in i.code_locations.values():
                        f = absolute_path / Path(j.file)
                        j.file = f.as_posix()
            objects.append((filepath, obj))
    return objects
