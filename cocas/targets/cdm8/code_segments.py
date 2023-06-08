from dataclasses import dataclass, field

from cocas.abstract_code_segments import CodeSegmentsInterface
from cocas.ast_nodes import LabelNode, RelocatableExpressionNode, TemplateFieldNode
from cocas.code_block import Section
from cocas.error import CdmException, CdmExceptionTag
from cocas.location import CodeLocation
from cocas.object_module import ExternalEntry, ObjectSectionRecord


def _error(segment: CodeSegmentsInterface.CodeSegment, message: str):
    raise CdmException(CdmExceptionTag.ASM, segment.location.file, segment.location.line, message)


# noinspection DuplicatedCode
class CodeSegments(CodeSegmentsInterface):
    @dataclass
    class CodeSegment(CodeSegmentsInterface.CodeSegment):
        pass

    class AlignmentPaddingSegment(CodeSegmentsInterface.AlignmentPaddingSegment, CodeSegment):
        pass

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

    class ExpressionSegment(CodeSegment):
        expr: RelocatableExpressionNode

        def __init__(self, location: CodeLocation, expr: RelocatableExpressionNode):
            self.location = location
            self.expr = expr
            self.size = 1

        def fill(self, object_record: ObjectSectionRecord, section: Section, labels: dict[str, int],
                 templates: dict[str, dict[str, int]]):
            parsed = CodeSegments.parse_expression(self.expr, section, labels, templates, self)
            CodeSegments.forbid_multilabel_expressions(parsed, self)
            value = CodeSegments.calculate_expression(parsed, section, labels)
            offset = section.address + len(object_record.data)
            if not -128 <= value < 256:
                _error(self, 'Number out of range')
            object_record.data.extend((value % 256).to_bytes(1, 'little'))
            CodeSegments.add_relatives_externals(parsed, offset, object_record)

    # noinspection DuplicatedCode
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
            _error(segment, 'No byte specifiers allowed in CdM-8')
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
                    entry.append(ExternalEntry(offset, range(0, 1), sign))
        if parsed.relative_additions != 0:
            sign = parsed.relative_additions // abs(parsed.relative_additions)
            for i in range(abs(parsed.relative_additions)):
                object_record.relative.append(ExternalEntry(offset, range(0, 1), sign))
