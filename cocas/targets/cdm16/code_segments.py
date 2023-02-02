from copy import copy
from dataclasses import dataclass, field

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

    class BytesSegment(CodeSegment):
        data: bytearray

        def __init__(self, data: bytearray):
            self.data = data
            self.size = len(data)

        def fill(self, object_record: ObjectSectionRecord, section: Section, labels: dict[str, int],
                 templates: dict[str, dict[str, int]]):
            object_record.data += self.data

    class VaryingLengthSegment(CodeSegment, CodeSegmentsInterface.VaryingLengthSegment):
        pass

    class LdiSegment(VaryingLengthSegment):
        expr: RelocatableExpressionNode

        def __init__(self, register: RegisterNode, expr: RelocatableExpressionNode):
            self.reg: int = register.number
            self.expr = expr
            self.size = 2
            self.size_locked = False
            self.location: CodeLocation = CodeLocation()

        def fill(self, object_record: ObjectSectionRecord, section: Section, labels: dict[str, int],
                 templates: dict[str, dict[str, int]]):
            parsed = CodeSegments.parse_expression(self.expr, section, labels, templates, self)
            parsed = CodeSegments.forbid_multilabel_expressions(parsed, self)
            if self.size == 4:
                object_record.data.extend(pack("u3p6u4u3", 0b001, 2, self.reg))
                offset = section.address + len(object_record.data)
                object_record.data.extend((parsed.value_with_relative % 65536).to_bytes(2, 'little'))
                CodeSegments.add_relatives_externals(parsed, offset, object_record)
            else:
                object_record.data.extend(pack("u3u3s7u3", 0b011, 5, parsed.value_with_relative, self.reg))

        def update_varying_length(self, pos, section: Section, labels: dict[str, int],
                                  templates: dict[str, dict[str, int]]):
            if self.size_locked:
                return
            parsed = CodeSegments.parse_expression(self.expr, section, labels, templates, self)
            parsed = CodeSegments.forbid_multilabel_expressions(parsed, self)
            if parsed.external or parsed.relative_additions != 0 or not -64 <= parsed.value_with_relative < 64:
                self.size = 4
                self.size_locked = True
                for label_name in section.labels:
                    if section.labels[label_name] > pos:
                        section.labels[label_name] += 2
                        labels[label_name] += 2
                old_locations = section.code_locations
                section.code_locations = dict()
                for PC, location in old_locations.items():
                    if PC > pos:
                        PC += 2
                    section.code_locations[PC] = location
                return 2

    @dataclass
    class ParsedExpression:
        value: int
        value_with_relative: int = field(init=False)
        relative_additions: int = field(default=0)
        asect: dict[str, int] = field(default_factory=dict)
        relative: dict[str, int] = field(default_factory=dict)
        external: dict[str, int] = field(default_factory=dict)

    @staticmethod
    def parse_expression(expr: RelocatableExpressionNode, section: Section, labels: dict[str, int],
                         templates: dict[str, dict[str, int]], segment: CodeSegment):
        if expr.byte_specifier is not None:
            _error(segment, f'No byte specifiers allowed in CdM-16')
        result = CodeSegments.ParsedExpression(expr.const_term)
        for term, sign in [(t, 1) for t in expr.add_terms] + [(t, -1) for t in expr.sub_terms]:
            if isinstance(term, LabelNode):
                if term.name in section.exts:
                    result.external[term.name] = result.external.get(term.name, 0) + sign
                elif term.name in section.labels and section.name != '$abs':
                    result.relative[term.name] = result.relative.get(term.name, 0) + sign
                elif term.name in labels:
                    result.value += labels[term.name] * sign
                    result.asect[term.name] = result.asect.get(term.name, 0) + sign
                else:
                    _error(segment, f'Label "{term.name}" not found')
            elif isinstance(term, TemplateFieldNode):
                result.value += templates[term.template_name][term.field_name] * sign

        result.value_with_relative = result.value
        for label, n in result.relative.items():
            rel_address = section.labels[label]
            result.value_with_relative += rel_address * n
            result.relative_additions += n
        return result

    @staticmethod
    def forbid_multilabel_expressions(parsed: ParsedExpression, segment: CodeSegment):
        parsed = copy(parsed)
        parsed.external = {label: n for label, n in parsed.external.items() if n != 0}
        parsed.relative = {label: n for label, n in parsed.relative.items() if n != 0}
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
        return parsed

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