from dataclasses import dataclass, field
from typing import TYPE_CHECKING

from cocas.ast_nodes import RelocatableExpressionNode, LabelNode, TemplateFieldNode
from cocas.code_block import Section
from cocas.default_code_segments import CodeSegmentsInterface
from cocas.error import CdmException, CdmExceptionTag
from . import target_instructions

TAG = CdmExceptionTag.ASM

if TYPE_CHECKING:
    from cocas.assembler import ObjectSectionRecord


class CodeSegments(CodeSegmentsInterface):
    @dataclass
    class CodeSegment(CodeSegmentsInterface.CodeSegment):
        pass

    @dataclass
    class RelocatableExpressionSegment(CodeSegment):
        expr: RelocatableExpressionNode

    @dataclass
    class VaryingLengthSegment(CodeSegment, CodeSegmentsInterface.VaryingLengthSegment):
        is_expanded: bool = field(init=False, default=False)
        expanded_size: int = field(init=False)

    @dataclass
    class BytesSegment(CodeSegment):
        data: bytearray

        def __init__(self, data: bytearray):
            self.data = data
            self.size = len(data)

        def fill(self, object_record: "ObjectSectionRecord", section: Section, labels: dict[str, int],
                 templates: dict[str, dict[str, int]]):
            object_record.data += self.data

    @dataclass
    class ShortExpressionSegment(RelocatableExpressionSegment):
        size = 1

        def fill(self, object_record: "ObjectSectionRecord", section: Section, labels: dict[str, int],
                 templates: dict[str, dict[str, int]]):
            val, val_long, val_sect, ext = eval_rel_expr_seg(self, section, labels, templates)

            is_rel = (val_sect == section.name != '$abs')
            if self.expr.byte_specifier is None and (is_rel or ext is not None):
                _error(self, 'Expected a 1-byte expression')
            if not -2 ** 7 <= val < 2 ** 8:
                _error(self, 'Number out of range')

            add_rel_record(object_record, is_rel, section, val_long, self)
            add_ext_record(object_record, ext, section, val_long, self)
            object_record.data.extend(val.to_bytes(self.size, 'little', signed=(val < 0)))

    @dataclass
    class ConstExpressionSegment(RelocatableExpressionSegment):
        positive: bool = False
        size = 1

        def fill(self, object_record: "ObjectSectionRecord", section: Section, labels: dict[str, int],
                 templates: dict[str, dict[str, int]]):
            val, _, val_sect, ext = eval_rel_expr_seg(self, section, labels, templates)
            if val_sect is not None or ext is not None:
                _error(self, 'Number expected but label found')
            if not -2 ** 7 <= val < 2 ** 8 or (self.positive and val < 0):
                _error(self, 'Number out of range')
            object_record.data.extend(val.to_bytes(self.size, 'little', signed=(val < 0)))

    @dataclass
    class LongExpressionSegment(RelocatableExpressionSegment):
        size = 2

        def fill(self, object_record: "ObjectSectionRecord", section: Section, labels: dict[str, int],
                 templates: dict[str, dict[str, int]]):
            val, val_long, val_sect, ext = eval_rel_expr_seg(self, section, labels, templates)

            if not -2 ** 15 <= val < 2 ** 16:
                _error(self, 'Number out of range')

            add_rel_record(object_record, val_sect, section, val_long, self)
            add_ext_record(object_record, ext, section, val_long, self)
            object_record.data.extend(val.to_bytes(self.size, 'little', signed=(val < 0)))

    @dataclass
    class OffsetExpressionSegment(RelocatableExpressionSegment):
        size = 1

        def fill(self, object_record: "ObjectSectionRecord", section: Section, labels: dict[str, int],
                 templates: dict[str, dict[str, int]]):
            val, _, val_sect, ext = eval_rel_expr_seg(self, section, labels, templates)

            is_rel = (val_sect == section.name != '$abs')
            if ext is not None:
                _error(self, 'Invalid destination address (external label used)')
            if section.name != '$abs' and not is_rel:
                _error(self, 'Invalid destination address (absolute address from rsect)')
            if self.expr.byte_specifier is not None and is_rel:
                _error(self, 'Invalid destination address (byte of relative address)')

            val -= section.address + len(object_record.data)
            if not -2 ** 7 <= val < 2 ** 7:
                _error(self, f'Destination address is too far')

            object_record.data.extend(val.to_bytes(self.size, 'little', signed=(val < 0)))

    @dataclass
    class GotoInstruction(VaryingLengthSegment):
        branch_mnemonic: str
        expr: RelocatableExpressionNode
        size = 2
        base_size = 2
        expanded_size = 5

        def update_varying_length(self, pos: int, section: "Section", labels: dict[str, int],
                                  templates: dict[str, dict[str, int]]):
            try:
                if self.is_expanded:
                    return

                addr, _, res_sect, ext = eval_rel_expr_seg(self, section, labels, templates)
                is_rel = (res_sect == section.name != '$abs')
                if (not -2 ** 7 <= addr - pos < 2 ** 7
                        or (section.name != '$abs' and not is_rel)
                        or (self.expr.byte_specifier is not None and is_rel)
                        or (ext is not None)):

                    shift_length = self.expanded_size - \
                                   self.base_size
                    self.is_expanded = True
                    self.size = self.expanded_size
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
                raise CdmException(TAG, self.location.file, self.location.line, str(e))

        def fill(self, object_record: "ObjectSectionRecord", section: Section, labels: dict[str, int],
                 templates: dict[str, dict[str, int]]):
            if self.is_expanded:
                branch_opcode = target_instructions.TargetInstructions.instructions['branch'][
                    f'bn{self.branch_mnemonic}']
                jmp_opcode = target_instructions.TargetInstructions.instructions['long']['jmp']
                object_record.data += bytearray([branch_opcode, 4, jmp_opcode])
                CodeSegments.LongExpressionSegment(self.expr).fill(object_record, section, labels, templates)
            else:
                branch_opcode = target_instructions.TargetInstructions.instructions['branch'][
                    f'b{self.branch_mnemonic}']
                object_record.data += bytearray([branch_opcode])
                CodeSegments.OffsetExpressionSegment(self.expr).fill(object_record, section, labels, templates)


def _error(segment: CodeSegmentsInterface.CodeSegment, message: str):
    raise CdmException(TAG, segment.location.file, segment.location.line, message)


def eval_rel_expr_seg(seg: CodeSegments.ShortExpressionSegment, s: Section,
                      labels: dict[str, int], templates: dict[str, dict[str, int]]):
    val_long = seg.expr.const_term
    used_exts = dict()
    s_dim = 0
    local_dim = 0
    for term, m in [(t, 1) for t in seg.expr.add_terms] + [(t, -1) for t in seg.expr.sub_terms]:
        if isinstance(term, LabelNode):
            if term.name in labels:
                local_dim += m
                val_long += labels[term.name] * m
            elif term.name in s.labels:
                s_dim += m
                val_long += s.labels[term.name] * m
            elif term.name in s.exts:
                used_exts.setdefault(term.name, 0)
                used_exts[term.name] += m
            else:
                _error(seg, f'Label "{term.name}" not found')
        elif isinstance(term, TemplateFieldNode):
            val_long += templates[term.template_name][term.field_name] * m

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


def add_ext_record(obj_rec: "ObjectSectionRecord", ext: str, s: Section, val: int,
                   seg: CodeSegments.RelocatableExpressionSegment):
    if ext is None:
        return

    val_lo, _ = val.to_bytes(2, 'little', signed=(val < 0))
    match seg.expr.byte_specifier:
        case 'low':
            obj_rec.xtrl.setdefault(ext, []).append(s.address + len(obj_rec.data))
        case 'high':
            obj_rec.xtrh.setdefault(ext, []).append((s.address + len(obj_rec.data), val_lo))
        case _:
            obj_rec.xtrl.setdefault(ext, []).append(s.address + len(obj_rec.data))
            obj_rec.xtrh.setdefault(ext, []).append((s.address + len(obj_rec.data) + 1, val_lo))


def add_rel_record(obj_rec: "ObjectSectionRecord", is_rel: bool, s: Section, val: int,
                   seg: CodeSegments.RelocatableExpressionSegment):
    if not is_rel:
        return

    val_lo, _ = val.to_bytes(2, 'little', signed=(val < 0))
    match seg.expr.byte_specifier:
        case 'low':
            obj_rec.rell.add(s.address + len(obj_rec.data))
        case 'high':
            obj_rec.relh.add((s.address + len(obj_rec.data), val_lo))
        case _:
            obj_rec.rell.add(s.address + len(obj_rec.data))
            obj_rec.relh.add((s.address + len(obj_rec.data) + 1, val_lo))
