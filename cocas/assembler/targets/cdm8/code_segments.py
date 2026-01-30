from abc import ABC
from dataclasses import dataclass, field
from typing import TYPE_CHECKING

from cocas.object_module import CodeLocation, ExternalEntry, ObjectSectionRecord

from ...ast_nodes import LabelNode, RelocatableExpressionNode, TemplateFieldNode
from ...exceptions import AssemblerException, AssemblerExceptionTag
from .. import IAlignmentPaddingSegment, ICodeSegment
from ....object_module.external_label_key import ExternalLabelKey

if TYPE_CHECKING:
    from ...code_block import Section


def _error(segment: ICodeSegment, message: str):
    raise AssemblerException(AssemblerExceptionTag.ASM, segment.location.file, segment.location.line, message)


# noinspection DuplicatedCode
class CodeSegment(ICodeSegment, ABC):
    pass


class AlignmentPaddingSegment(IAlignmentPaddingSegment, CodeSegment):
    pass


class BytesSegment(CodeSegment):
    data: bytes

    @property
    def size(self) -> int:
        return self._size

    @property
    def location(self) -> CodeLocation:
        return self._location

    def __init__(self, data: bytes, location: CodeLocation):
        self.data = data
        self._size = len(data)
        self._location = location

    def fill(self, object_record: "ObjectSectionRecord", section: "Section", labels: dict[str, int],
             templates: dict[str, dict[str, int]]):
        super().fill(object_record, section, labels, templates)
        object_record.data += self.data


class ExpressionSegment(CodeSegment):
    expr: RelocatableExpressionNode
    size = 1

    @property
    def location(self) -> CodeLocation:
        return self._location

    def __init__(self, expr: RelocatableExpressionNode, location: CodeLocation):
        self.expr = expr
        self._location = location

    def fill(self, object_record: "ObjectSectionRecord", section: "Section", labels: dict[str, int],
             templates: dict[str, dict[str, int]]):
        parsed = parse_expression(self.expr, section, labels, templates, self)
        forbid_multilabel_expressions(parsed, self)
        value = calculate_expression(parsed, section, labels)
        offset = section.address + len(object_record.data)
        if not -128 <= value < 256:
            _error(self, 'Number out of range')
        object_record.data.extend((value % 256).to_bytes(1, 'little'))
        add_rel_ext_entries(parsed, offset, object_record)


# noinspection DuplicatedCode
@dataclass
class ParsedExpression:
    value: int
    relocate_additions: int = field(default=0)
    asect: dict[str, int] = field(default_factory=dict)
    rel_labels: dict[str, int] = field(default_factory=dict)
    ext_labels: dict[ExternalLabelKey, int] = field(default_factory=dict)


def parse_expression(expr: RelocatableExpressionNode, section: "Section", labels: dict[str, int],
                     templates: dict[str, dict[str, int]], segment: CodeSegment) -> ParsedExpression:
    if expr.byte_specifier is not None:
        _error(segment, 'No byte specifiers allowed in CdM-8')
    result = ParsedExpression(expr.const_term)
    for term, sign in [(t, 1) for t in expr.add_terms] + [(t, -1) for t in expr.sub_terms]:
        if isinstance(term, LabelNode):
            if term.name in section.exts:
                result.ext_labels[ExternalLabelKey(term.name, section.exts[term.name])] = \
                    result.ext_labels.get(ExternalLabelKey(term.name, section.exts[term.name]), 0) + sign
            elif term.name in section.labels and section.name != '$abs':
                result.rel_labels[term.name] = result.rel_labels.get(term.name, 0) + sign
            elif term.name in section.labels:
                result.asect[term.name] = result.asect.get(term.name, 0) + sign
            elif term.name in labels:
                result.asect[term.name] = result.asect.get(term.name, 0) + sign
            else:
                _error(segment, f'Label "{term.name}" not found')
        elif isinstance(term, TemplateFieldNode):
            result.value += templates[term.template_name][term.field_name] * sign
    for label, n in result.rel_labels.items():
        result.relocate_additions += n
    result.asect = {label: n for label, n in result.asect.items() if n != 0}
    result.ext_labels = {label: n for label, n in result.ext_labels.items() if n != 0}
    result.rel_labels = {label: n for label, n in result.rel_labels.items() if n != 0}
    return result


def calculate_expression(parsed: ParsedExpression, section: "Section", labels: dict[str, int]) -> int:
    value = parsed.value
    for label, n in parsed.asect.items():
        if label in section.labels:
            value += section.labels[label] * n
        else:
            value += labels[label] * n
    for label, n in parsed.rel_labels.items():
        rel_address = section.labels[label]
        value += rel_address * n
    return value


def forbid_multilabel_expressions(parsed: ParsedExpression, segment: CodeSegment):
    if len(parsed.ext_labels) > 1:
        _error(segment, 'Cannot use multiple external labels in an address expression')
    elif len(parsed.ext_labels) == 1:
        label, n = next(iter(parsed.ext_labels.items()))
        if n < 0:
            _error(segment, 'Cannot subtract external labels in an address expression')
        elif n > 1:
            _error(segment, 'Cannot add external label multiple times in an address expression')
        elif parsed.relocate_additions != 0:
            _error(segment, 'Cannot add both external and relocatable section labels')
    elif parsed.relocate_additions < 0:
        _error(segment, 'Can subtract rsect labels only to get distance from another added rsect label')
    elif parsed.relocate_additions > 1:
        _error(segment, 'Can add rsect labels multiple times only to find distance '
                        'from another subtracted rsect label')


def add_rel_ext_entries(parsed: ParsedExpression, offset: int, object_record: "ObjectSectionRecord"):
    for label in parsed.ext_labels:
        if parsed.ext_labels[label] != 0:
            entry = object_record.external.setdefault(label, [])
            n = abs(parsed.ext_labels[label])
            sign = parsed.ext_labels[label] // n
            for i in range(n):
                entry.append(ExternalEntry(offset, range(0, 1), sign))
    if parsed.relocate_additions != 0:
        sign = parsed.relocate_additions // abs(parsed.relocate_additions)
        for i in range(abs(parsed.relocate_additions)):
            object_record.relocatable.append(ExternalEntry(offset, range(0, 1), sign))
