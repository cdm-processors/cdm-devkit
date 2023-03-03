from dataclasses import dataclass, field
from math import lcm
from typing import Optional

import bitstruct

from cocas.ast_nodes import RelocatableExpressionNode, LabelNode, TemplateFieldNode, RegisterNode
from cocas.code_block import Section
from cocas.default_code_segments import CodeSegmentsInterface
from cocas.error import CdmException, CdmExceptionTag
from cocas.location import CodeLocation
from cocas.object_module import ObjectSectionRecord, ExternalEntry


def pack(fmt, *args):
    b = bitstruct.pack(fmt, *args)
    return bitstruct.byteswap('2', b)


def _error(segment: CodeSegmentsInterface.CodeSegment, message: str):
    raise CdmException(CdmExceptionTag.ASM, segment.location.file, segment.location.line, message)


class CodeSegments(CodeSegmentsInterface):
    @dataclass
    class CodeSegment(CodeSegmentsInterface.CodeSegment):
        pass

    class VaryingLengthSegment(CodeSegment, CodeSegmentsInterface.VaryingLengthSegment):
        @staticmethod
        def update_surroundings(diff: int, pos: int, section: Section, labels: dict[str, int]):
            for label_name in section.labels:
                if section.labels[label_name] > pos:
                    section.labels[label_name] += diff
                    if label_name in labels:
                        labels[label_name] += diff
            old_locations = section.code_locations
            section.code_locations = dict()
            for PC, location in old_locations.items():
                if PC > pos:
                    PC += diff
                section.code_locations[PC] = location

    class AlignmentPaddingSegment(VaryingLengthSegment):
        def __init__(self, alignment: int, location: CodeLocation):
            self.location = location
            self.alignment = alignment
            self.size = alignment

        def fill(self, object_record: ObjectSectionRecord, section: Section, labels: dict[str, int],
                 templates: dict[str, dict[str, int]]):
            object_record.data += bytes(self.size)
            if section.name != '$abs':
                object_record.alignment = lcm(object_record.alignment, self.alignment)

        def update_varying_length(self, pos, section: Section, labels: dict[str, int], _):
            new_size = (-section.address - pos) % self.alignment
            if new_size == self.alignment:
                new_size = 0
            diff = new_size - self.size
            self.size = new_size
            self.__class__.update_surroundings(diff, pos, section, labels)
            return diff

    class AlignedSegment(CodeSegment):
        alignment: int

        def __init__(self, alignment: int):
            self.alignment = alignment

        def fill(self, object_record: ObjectSectionRecord, section: Section, labels: dict[str, int],
                 templates: dict[str, dict[str, int]]):
            if (section.address + len(object_record.data)) % self.alignment != 0:
                _error(self, f'Segment must be {self.alignment}-byte aligned')
            super().fill(object_record, section, labels, templates)
            if section.name != '$abs':
                object_record.alignment = lcm(object_record.alignment, self.alignment)

    class InstructionSegment(AlignedSegment):
        def __init__(self, location: CodeLocation):
            super().__init__(2)
            self.location = location

    class BytesSegment(CodeSegment):
        data: bytes

        def __init__(self, data: bytes, location: CodeLocation):
            self.location = location
            self.data = data
            self.size = len(data)

        def fill(self, object_record: ObjectSectionRecord, section: Section, labels: dict[str, int],
                 templates: dict[str, dict[str, int]]):
            super().fill(object_record, section, labels, templates)
            object_record.data += self.data

    class InstructionBytesSegment(InstructionSegment, BytesSegment):
        def __init__(self, data: bytes, location: CodeLocation):
            CodeSegments.InstructionSegment.__init__(self, location)
            CodeSegments.BytesSegment.__init__(self, data, location)

    class ExpressionSegment(CodeSegment):
        expr: RelocatableExpressionNode

        def __init__(self, location: CodeLocation, expr: RelocatableExpressionNode):
            self.location = location
            self.expr = expr
            self.size = 2

        def fill(self, object_record: ObjectSectionRecord, section: Section, labels: dict[str, int],
                 templates: dict[str, dict[str, int]]):
            parsed = CodeSegments.parse_expression(self.expr, section, labels, templates, self)
            CodeSegments.forbid_multilabel_expressions(parsed, self)
            value = CodeSegments.calculate_expression(parsed, section, labels)
            offset = section.address + len(object_record.data)
            if not -32768 <= value < 65536:
                _error(self, 'Number out of range')
            object_record.data.extend((value % 65536).to_bytes(2, 'little'))
            CodeSegments.add_relatives_externals(parsed, offset, object_record)

    class LdiSegment(InstructionSegment, VaryingLengthSegment):
        expr: RelocatableExpressionNode

        def __init__(self, location: CodeLocation, register: RegisterNode, expr: RelocatableExpressionNode):
            CodeSegments.InstructionSegment.__init__(self, location)
            self.reg: int = register.number
            self.expr = expr
            self.size = 2
            self.size_locked = False
            self.checked = False
            self.parsed: Optional[CodeSegments.ParsedExpression] = None

        def fill(self, object_record: ObjectSectionRecord, section: Section, labels: dict[str, int],
                 templates: dict[str, dict[str, int]]):
            super().fill(object_record, section, labels, templates)
            if self.size == 4:
                object_record.data.extend(pack("u3p6u4u3", 0b001, 2, self.reg))
                CodeSegments.ExpressionSegment(self.location, self.expr).fill(object_record, section, labels, templates)
            else:
                value = CodeSegments.calculate_expression(self.parsed, section, labels)
                object_record.data.extend(pack("u3u3s7u3", 0b011, 5, value, self.reg))

        def update_varying_length(self, pos, section: Section, labels: dict[str, int],
                                  templates: dict[str, dict[str, int]]):
            if self.size_locked:
                return
            bad = False
            if not self.checked:
                self.parsed = CodeSegments.parse_expression(self.expr, section, labels, templates, self)
                CodeSegments.forbid_multilabel_expressions(self.parsed, self)
                bad = self.parsed.external or self.parsed.relative_additions != 0
                self.checked = True
            value = CodeSegments.calculate_expression(self.parsed, section, labels)
            if bad or not -64 <= value < 64:
                self.size = 4
                self.size_locked = True
                self.__class__.update_surroundings(2, pos, section, labels)
                return 2

    class Branch(InstructionSegment, VaryingLengthSegment):
        expr: RelocatableExpressionNode

        def __init__(self, location: CodeLocation, branch_code: int, expr: RelocatableExpressionNode,
                     operation='branch'):
            CodeSegments.InstructionSegment.__init__(self, location)
            self.type = operation
            self.branch_code = branch_code
            self.expr = expr
            self.size = 2
            self.size_locked = False
            self.checked = False
            self.parsed: Optional[CodeSegments.ParsedExpression] = None

        def fill(self, object_record: ObjectSectionRecord, section: Section, labels: dict[str, int],
                 templates: dict[str, dict[str, int]]):
            super().fill(object_record, section, labels, templates)
            value = CodeSegments.calculate_expression(self.parsed, section, labels)
            if value % 2 != 0:
                _error(self, "Destination address must be 2-byte aligned")
            if self.size == 4:
                if self.type == 'branch':
                    object_record.data.extend(pack("u5p7u4", 0x00001, self.branch_code))
                elif self.type == 'jsr':
                    object_record.data.extend(pack("u5p7u4", 0x00000, 8))
                CodeSegments.ExpressionSegment(self.location, self.expr).fill(object_record, section, labels, templates)
            else:
                dist = value - (section.address + len(object_record.data) + 2)
                if self.type == 'branch':
                    val = dist // 2 % 512
                    sign = 0 if dist < 0 else 1
                    object_record.data.extend(pack("u2u1u4u9", 0b11, sign, self.branch_code, val))
                elif self.type == 'jsr':
                    val = dist // 2 % 1024
                    object_record.data.extend(pack("u3u3u10", 0b100, 3, val))

        def update_varying_length(self, pos, section: Section, labels: dict[str, int],
                                  templates: dict[str, dict[str, int]]):
            if self.size_locked:
                return
            bad = False
            if not self.checked:
                self.parsed = CodeSegments.parse_expression(self.expr, section, labels, templates, self)
                if self.expr.sub_terms:
                    _error(self, 'Cannot subtract labels in branch value expressions')
                elif len(self.expr.add_terms) > 1:
                    _error(self, 'Cannot use multiple labels in branch value expressions')
                const = not self.expr.add_terms and not self.expr.sub_terms
                bad = self.parsed.external or (self.parsed.asect or const) and section.name != '$abs'
                self.checked = True
            value = CodeSegments.calculate_expression(self.parsed, section, labels)
            dist = value - pos - 2
            if bad or not -1024 <= dist < 1024:
                self.size = 4
                self.size_locked = True
                self.__class__.update_surroundings(2, pos, section, labels)
                return 2

    class Imm6(InstructionSegment):
        expr: RelocatableExpressionNode

        def __init__(self, location: CodeLocation, negative: bool, op_number: int, register: RegisterNode,
                     expr: RelocatableExpressionNode, word=False):
            super().__init__(location)
            self.word = word
            self.op_number = op_number
            self.sign = -1 if negative else 1
            self.reg: int = register.number
            self.expr = expr
            self.size = 2

        def fill(self, object_record: ObjectSectionRecord, section: Section, labels: dict[str, int],
                 templates: dict[str, dict[str, int]]):
            super().fill(object_record, section, labels, templates)
            parsed = CodeSegments.parse_expression(self.expr, section, labels, templates, self)
            value = CodeSegments.calculate_expression(parsed, section, labels) * self.sign
            if parsed.external:
                _error(self, 'No external labels allowed in immediate form')
            elif parsed.relative_additions != 0:
                _error(self, 'Can use rsect labels only to find distance in immediate form')
            if self.word:
                if value % 2 != 0:
                    _error(self, "Destination address must be 2-byte aligned")
                value //= 2
            if not -64 <= value < 64:
                _error(self, 'Value is out of bounds for immediate form')
            object_record.data.extend(pack("u3u3s7u3", 0b011, self.op_number, value, self.reg))

    class Imm9(InstructionSegment):
        expr: RelocatableExpressionNode

        def __init__(self, location: CodeLocation, negative: bool, op_number: int, expr: RelocatableExpressionNode):
            super().__init__(location)
            self.op_number = op_number
            self.sign = -1 if negative else 1
            self.expr = expr
            self.size = 2

        def fill(self, object_record: ObjectSectionRecord, section: Section, labels: dict[str, int],
                 templates: dict[str, dict[str, int]]):
            super().fill(object_record, section, labels, templates)
            parsed = CodeSegments.parse_expression(self.expr, section, labels, templates, self)
            value = CodeSegments.calculate_expression(parsed, section, labels) * self.sign
            if parsed.external:
                _error(self, 'No external labels allowed in immediate form')
            elif parsed.relative_additions != 0:
                _error(self, 'Can use rsect labels only to find distance in immediate form')
            elif not -512 <= value < 512:
                _error(self, 'Value is out of bounds for immediate form')
            object_record.data.extend(pack("u3u3s10", 0b100, self.op_number, value))

    @dataclass
    class ParsedExpression:
        value: int
        relative_additions: int = field(default=0)
        asect: dict[str, int] = field(default_factory=dict)
        relative: dict[str, int] = field(default_factory=dict)
        external: dict[str, int] = field(default_factory=dict)

    @staticmethod
    def parse_expression(expr: RelocatableExpressionNode, section: Section, labels: dict[str, int],
                         templates: dict[str, dict[str, int]], segment: CodeSegment) -> ParsedExpression:
        if expr.byte_specifier is not None:
            _error(segment, f'No byte specifiers allowed in CdM-16')
        result = CodeSegments.ParsedExpression(expr.const_term)
        for term, sign in [(t, 1) for t in expr.add_terms] + [(t, -1) for t in expr.sub_terms]:
            if isinstance(term, LabelNode):
                if term.name in section.exts:
                    result.external[term.name] = result.external.get(term.name, 0) + sign
                elif term.name in section.labels and section.name != '$abs':
                    result.relative[term.name] = result.relative.get(term.name, 0) + sign
                elif term.name in section.labels:
                    result.asect[term.name] = result.asect.get(term.name, 0) + sign
                elif term.name in labels:
                    result.asect[term.name] = result.asect.get(term.name, 0) + sign
                else:
                    _error(segment, f'Label "{term.name}" not found')
            elif isinstance(term, TemplateFieldNode):
                result.value += templates[term.template_name][term.field_name] * sign
        for label, n in result.relative.items():
            result.relative_additions += n
        result.asect = {label: n for label, n in result.asect.items() if n != 0}
        result.external = {label: n for label, n in result.external.items() if n != 0}
        result.relative = {label: n for label, n in result.relative.items() if n != 0}
        return result

    @staticmethod
    def calculate_expression(parsed: ParsedExpression, section: Section, labels: dict[str, int]) -> int:
        value = parsed.value
        for label, n in parsed.asect.items():
            if label in section.labels:
                value += section.labels[label] * n
            else:
                value += labels[label] * n
        for label, n in parsed.relative.items():
            rel_address = section.labels[label]
            value += rel_address * n
        return value

    @staticmethod
    def forbid_multilabel_expressions(parsed: ParsedExpression, segment: CodeSegment):
        if len(parsed.external) > 1:
            _error(segment, 'Cannot use multiple external labels in an address expression')
        elif len(parsed.external) == 1:
            label, n = next(iter(parsed.external.items()))
            if n < 0:
                _error(segment, 'Cannot subtract external labels in an address expression')
            elif n > 1:
                _error(segment, 'Cannot add external label multiple times in an address expression')
            elif parsed.relative_additions != 0:
                _error(segment, 'Cannot add both external and relative section labels')
        elif parsed.relative_additions < 0:
            _error(segment, 'Can subtract rsect labels only to get distance from another added rsect label')
        elif parsed.relative_additions > 1:
            _error(segment, 'Can add rsect labels multiple times only to find distance '
                            'from another subtracted rsect label')

    @staticmethod
    def add_relatives_externals(parsed: ParsedExpression, offset: int, object_record: ObjectSectionRecord):
        for label in parsed.external:
            if parsed.external[label] != 0:
                entry = object_record.external.setdefault(label, [])
                n = abs(parsed.external[label])
                sign = parsed.external[label] // n
                for i in range(n):
                    entry.append(ExternalEntry(offset, range(0, 2), sign))
        if parsed.relative_additions != 0:
            sign = parsed.relative_additions // abs(parsed.relative_additions)
            for i in range(abs(parsed.relative_additions)):
                object_record.relative.append(ExternalEntry(offset, range(0, 2), sign))
