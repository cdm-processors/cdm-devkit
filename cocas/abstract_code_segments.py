from dataclasses import dataclass, field
from math import lcm
from typing import TYPE_CHECKING

from cocas.error import CdmException, CdmExceptionTag
from cocas.location import CodeLocation

if TYPE_CHECKING:
    from assembler import ObjectSectionRecord

    from cocas.code_block import Section


class CodeSegmentsInterface:
    @dataclass
    class CodeSegment:
        size: int = field(init=False)
        position: int = field(init=False)

        def __post_init__(self):
            # ugly hack to store code location in segments
            # now this whole project is one big and ugly hack
            self.location: CodeLocation = CodeLocation()

        def fill(self, object_record: "ObjectSectionRecord", section: "Section", labels: dict[str, int],
                 templates: dict[str, dict[str, int]]):
            pass

    @dataclass
    class VaryingLengthSegment(CodeSegment):
        def update_varying_length(self, pos, section: "Section", labels: dict[str, int],
                                  templates: dict[str, dict[str, int]]) -> int:
            pass

        @staticmethod
        def update_surroundings(diff: int, pos: int, section: "Section", labels: dict[str, int]):
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

        def fill(self, object_record: "ObjectSectionRecord", section: "Section", labels: dict[str, int],
                 templates: dict[str, dict[str, int]]):
            object_record.data += bytes(self.size)
            if section.name != '$abs':
                object_record.alignment = lcm(object_record.alignment, self.alignment)

        def update_varying_length(self, pos, section: "Section", labels: dict[str, int], _):
            new_size = (-pos) % self.alignment
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

        def fill(self, object_record: "ObjectSectionRecord", section: "Section", labels: dict[str, int],
                 templates: dict[str, dict[str, int]]):
            if (section.address + len(object_record.data)) % self.alignment != 0:
                _error(self, f'Segment must be {self.alignment}-byte aligned')
            super().fill(object_record, section, labels, templates)
            if section.name != '$abs':
                object_record.alignment = lcm(object_record.alignment, self.alignment)


def _error(segment: CodeSegmentsInterface.CodeSegment, message: str):
    raise CdmException(CdmExceptionTag.ASM, segment.location.file, segment.location.line, message)
