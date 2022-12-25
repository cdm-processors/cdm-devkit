from typing import Union, Type

from cocas.ast_nodes import *
from cocas.code_block import Section
from cocas.default_code_segments import CodeSegmentsInterface
from cocas.default_instructions import TargetInstructionsInterface
from cocas.error import CdmException, CdmExceptionTag

TAG = CdmExceptionTag.ASM

target_instructions_: Union[Type[TargetInstructionsInterface], None] = None
code_segments_: Union[Type[CodeSegmentsInterface], None] = None

from cocas.targets.cdm8e.code_segments import CodeSegments as c_s

code_segments_ = c_s


def _error(segment: CodeSegmentsInterface.CodeSegment, message: str):
    raise CdmException(TAG, segment.location.file, segment.location.line, message)


@dataclass
class Template:
    def __init__(self, sn: TemplateSectionNode):
        self.name: str = sn.name
        self.labels: dict[str, int] = dict()

        size = 0
        for line in sn.lines:
            if isinstance(line, LabelDeclarationNode):
                label_name = line.label.name
                if label_name in self.labels:
                    raise Exception(f'Duplicate label "{label_name}" declaration')

                if line.external:
                    raise Exception('External labels not allowed in templates')
                elif line.entry:
                    raise Exception('Ents not allowed in templates')
                else:
                    self.labels[label_name] = size

            elif isinstance(line, InstructionNode):
                if line.mnemonic not in target_instructions_.assembly_directives:
                    raise Exception('Only "dc" and "ds" allowed in templates')
                for seg in target_instructions_.assemble_instruction(line, code_segments_):
                    size += seg.size

        self.labels['_'] = size


@dataclass
class ObjectSectionRecord:
    def __init__(self, s: Section, local_labels: dict[str, int], template_fields: dict[str, dict[str, int]]):
        self.address: int = s.address
        self.name: str = s.name
        self.data = bytearray()
        self.rell: set[int] = set()
        self.relh: set[tuple[int, int]] = set()
        self.ents: dict[str, int] = dict(p for p in s.labels.items() if p[0] in s.ents)
        self.xtrl: dict[str, list[int]] = dict()
        self.xtrh: dict[str, list[tuple[int, int]]] = dict()
        self.code_locations = s.code_locations

        segment_handlers = {
            code_segments_.BytesSegment: self.fill_bytes,
            code_segments_.ShortExpressionSegment: self.fill_short_expr,
            code_segments_.LongExpressionSegment: self.fill_long_expr,
            code_segments_.ConstExpressionSegment: self.fill_const_expr,
            code_segments_.OffsetExpressionSegment: self.fill_offset_expr,
            code_segments_.BranchInstruction: self.fill_goto
        }
        for seg in s.segments:
            segment_handlers[type(seg)](seg, s, local_labels, template_fields)

    def add_ext_record(self, ext: str, s: Section, val: int, seg: code_segments_.RelocatableExpressionSegment):
        if ext is None:
            return

        val_lo, _ = val.to_bytes(2, 'little', signed=(val < 0))
        match seg.expr.byte_specifier:
            case 'low':
                self.xtrl.setdefault(ext, []).append(s.address + len(self.data))
            case 'high':
                self.xtrh.setdefault(ext, []).append((s.address + len(self.data), val_lo))
            case _:
                self.xtrl.setdefault(ext, []).append(s.address + len(self.data))
                self.xtrh.setdefault(ext, []).append((s.address + len(self.data) + 1, val_lo))

    def add_rel_record(self, is_rel: bool, s: Section, val: int, seg: code_segments_.RelocatableExpressionSegment):
        if not is_rel:
            return

        val_lo, _ = val.to_bytes(2, 'little', signed=(val < 0))
        match seg.expr.byte_specifier:
            case 'low':
                self.rell.add(s.address + len(self.data))
            case 'high':
                self.relh.add((s.address + len(self.data), val_lo))
            case _:
                self.rell.add(s.address + len(self.data))
                self.relh.add((s.address + len(self.data) + 1, val_lo))

    def fill_bytes(self, seg: code_segments_.BytesSegment, s: Section,
                   local_labels: dict[str, int], template_fields: dict[str, dict[str, int]]):
        self.data += seg.data

    def fill_short_expr(self, seg: code_segments_.ShortExpressionSegment, s: Section,
                        local_labels: dict[str, int], template_fields: dict[str, dict[str, int]]):
        val, val_long, val_sect, ext = eval_rel_expr_seg(seg, s, local_labels, template_fields)

        is_rel = (val_sect == s.name != '$abs')
        if seg.expr.byte_specifier is None and (is_rel or ext is not None):
            _error(seg, 'Expected a 1-byte expression')
        if not -2 ** 7 <= val < 2 ** 8:
            _error(seg, 'Number out of range')

        self.add_rel_record(is_rel, s, val_long, seg)
        self.add_ext_record(ext, s, val_long, seg)
        self.data.extend(val.to_bytes(seg.size, 'little', signed=(val < 0)))

    def fill_long_expr(self, seg: code_segments_.LongExpressionSegment, s: Section,
                       local_labels: dict[str, int], template_fields: dict[str, dict[str, int]]):
        val, val_long, val_sect, ext = eval_rel_expr_seg(seg, s, local_labels, template_fields)

        if not -2 ** 15 <= val < 2 ** 16:
            _error(seg, 'Number out of range')

        self.add_rel_record(val_sect, s, val_long, seg)
        self.add_ext_record(ext, s, val_long, seg)
        self.data.extend(val.to_bytes(seg.size, 'little', signed=(val < 0)))

    def fill_const_expr(self, seg: code_segments_.ConstExpressionSegment, s: Section,
                        local_labels: dict[str, int], template_fields: dict[str, dict[str, int]]):
        val, _, val_sect, ext = eval_rel_expr_seg(seg, s, local_labels, template_fields)

        if val_sect is not None or ext is not None:
            _error(seg, 'Number expected but label found')
        if not -2 ** 7 <= val < 2 ** 8 or (seg.positive and val < 0):
            _error(seg, 'Number out of range')

        self.data.extend(val.to_bytes(seg.size, 'little', signed=(val < 0)))

    def fill_offset_expr(self, seg: code_segments_.OffsetExpressionSegment, s: Section,
                         local_labels: dict[str, int], template_fields: dict[str, dict[str, int]]):
        val, _, val_sect, ext = eval_rel_expr_seg(seg, s, local_labels, template_fields)

        is_rel = (val_sect == s.name != '$abs')
        if ext is not None:
            _error(seg, 'Invalid destination address (external label used)')
        if s.name != '$abs' and not is_rel:
            _error(seg, 'Invalid destination address (absolute address from rsect)')
        if seg.expr.byte_specifier is not None and is_rel:
            _error(seg, 'Invalid destination address (byte of relative address)')

        val -= s.address + len(self.data)
        if not -2 ** 7 <= val < 2 ** 7:
            _error(seg, f'Destination address is too far')

        self.data.extend(val.to_bytes(seg.size, 'little', signed=(val < 0)))

    def fill_goto(self, seg: code_segments_.BranchInstruction, s: Section,
                  local_labels: dict[str, int], template_fields: dict[str, dict[str, int]]):
        if seg.is_expanded:
            branch_opcode = target_instructions_.instructions['branch'][f'bn{seg.branch_mnemonic}']
            jmp_opcode = target_instructions_.instructions['long']['jmp']
            self.data += bytearray([branch_opcode, 4, jmp_opcode])
            self.fill_long_expr(code_segments_.LongExpressionSegment(seg.expr), s, local_labels, template_fields)
        else:
            branch_opcode = target_instructions_.instructions['branch'][f'b{seg.branch_mnemonic}']
            self.data += bytearray([branch_opcode])
            self.fill_offset_expr(code_segments_.OffsetExpressionSegment(seg.expr), s, local_labels, template_fields)


@dataclass
class ObjectModule:
    def __init__(self):
        self.asects: list[ObjectSectionRecord] = []
        self.rsects: list[ObjectSectionRecord] = []


def gather_local_labels(sects: list[Section]):
    local_labels = dict()
    for sect in sects:
        local_labels.update({p for p in sect.labels.items() if not p[0].startswith('$')})
    return local_labels


def eval_rel_expr_seg(seg: code_segments_.ShortExpressionSegment, s: Section,
                      local_labels: dict[str, int], template_fields: dict[str, dict[str, int]]):
    val_long = seg.expr.const_term
    used_exts = dict()
    s_dim = 0
    local_dim = 0
    for term, m in [(t, 1) for t in seg.expr.add_terms] + [(t, -1) for t in seg.expr.sub_terms]:
        if isinstance(term, LabelNode):
            if term.name in local_labels:
                local_dim += m
                val_long += local_labels[term.name] * m
            elif term.name in s.labels:
                s_dim += m
                val_long += s.labels[term.name] * m
            elif term.name in s.exts:
                used_exts.setdefault(term.name, 0)
                used_exts[term.name] += m
            else:
                _error(seg, f'Label "{term.name}" not found')
        elif isinstance(term, TemplateFieldNode):
            val_long += template_fields[term.template_name][term.field_name] * m

    val_lo, val_hi = val_long.to_bytes(2, 'little', signed=(val_long < 0))
    match seg.expr.byte_specifier:
        case 'low':
            val = val_lo
        case 'high':
            val = val_hi
        case _:
            val = val_long

    used_exts = dict(filter(lambda x: x[1] != 0, used_exts.items()))
    if len(used_exts) > 1:
        _error(seg, 'Cannot use multiple external labels in an address expression')

    if len(used_exts) == 0:
        if s_dim == 0 and local_dim == 0:
            return val, val_long, None, None
        elif s_dim == 0 and local_dim == 1:
            return val, val_long, '$abs', None
        elif s_dim == 1 and local_dim == 0:
            return val, val_long, s.name, None
    else:
        ext, ext_dim = used_exts.popitem()
        if local_dim == 0 and s_dim == 0 and ext_dim == 1:
            return val, val_long, None, ext

    _error(seg, 'Result is not a label or a number')


def update_varying_length(section: Section, asects_labels: dict[str, int],
                          template_fields: dict[str, dict[str, int]]):
    labels = gather_local_labels([section])
    labels.update(asects_labels)
    # while True:
    for i in range(1):  # later can be changed to use more passes
        pos = section.address

        for seg in section.segments:
            if isinstance(seg, code_segments_.BranchInstruction):

                try:
                    if seg.is_expanded:
                        continue

                    addr, _, res_sect, ext = eval_rel_expr_seg(seg, section, labels, template_fields)
                    is_rel = (res_sect == section.name != '$abs')
                    if (not -2 ** 7 <= addr - pos < 2 ** 7
                            or (section.name != '$abs' and not is_rel)
                            or (seg.expr.byte_specifier is not None and is_rel)
                            or (ext is not None)):

                        shift_length = code_segments_.BranchInstruction.expanded_size - \
                                       code_segments_.BranchInstruction.base_size
                        seg.is_expanded = True
                        old_locations = section.code_locations
                        section.code_locations = dict()
                        for PC, location in old_locations.items():
                            if PC > pos:
                                PC += shift_length
                            section.code_locations[PC] = location

                        for label_name in section.labels:
                            if section.labels[label_name] > pos:
                                section.labels[label_name] += shift_length
                                labels[label_name] += shift_length

                except Exception as e:
                    raise CdmException(TAG, seg.location.file, seg.location.line, str(e))

            pos += seg.size


def assemble(pn: ProgramNode, isa_module):
    global target_instructions_
    target_instructions_ = isa_module.TargetInstructions
    global code_segments_
    code_segments_ = isa_module.CodeSegments
    templates = [Template(t) for t in pn.template_sections]
    template_fields = dict([(t.name, t.labels) for t in templates])

    asects = [Section(asect, target_instructions_, code_segments_) for asect in pn.absolute_sections]
    rsects = [Section(rsect, target_instructions_, code_segments_) for rsect in pn.relocatable_sections]
    asects.sort(key=lambda s: s.address)

    asects_labels = gather_local_labels(asects)
    for asect in asects:
        update_varying_length(asect, asects_labels, template_fields)
        asects_labels.update(gather_local_labels([asect]))
    for rsect in rsects:
        update_varying_length(rsect, asects_labels, template_fields)

    obj = ObjectModule()
    obj.asects = [ObjectSectionRecord(asect, asects_labels, template_fields) for asect in asects]
    obj.rsects = [ObjectSectionRecord(rsect, asects_labels, template_fields) for rsect in rsects]

    return obj
