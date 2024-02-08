from abc import ABC, abstractmethod
from math import lcm
from typing import TYPE_CHECKING

from cocas.object_module import CodeLocation

from ..exceptions import AsmExceptionTag, AssemblerException

if TYPE_CHECKING:
    from cocas.object_module import ObjectSectionRecord

    from ..code_block import Section


class ICodeSegment(ABC):
    @property
    @abstractmethod
    def size(self) -> int:
        pass

    @property
    @abstractmethod
    def location(self) -> CodeLocation:
        pass

    @abstractmethod
    def fill(self, object_record: "ObjectSectionRecord", section: "Section", labels: dict[str, int],
             templates: dict[str, dict[str, int]]):
        pass


class IVaryingLengthSegment(ICodeSegment, ABC):
    @abstractmethod
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


class IAlignmentPaddingSegment(IVaryingLengthSegment):

    @property
    def size(self) -> int:
        return self._size

    @property
    def location(self) -> CodeLocation:
        return self._location

    def __init__(self, alignment: int, location: CodeLocation):
        self.alignment = alignment
        self._size = alignment
        self._location = location

    def fill(self, object_record: "ObjectSectionRecord", section: "Section", labels: dict[str, int],
             templates: dict[str, dict[str, int]]):
        object_record.data += bytes(self.size)
        if section.name != '$abs':
            object_record.alignment = lcm(object_record.alignment, self.alignment)

    def update_varying_length(self, pos, section: "Section", labels: dict[str, int], _) -> int:
        new_size = (-pos) % self.alignment
        if new_size == self.alignment:
            new_size = 0
        diff = new_size - self.size
        self._size = new_size
        self.__class__.update_surroundings(diff, pos, section, labels)
        return diff


class IAlignedSegment(ICodeSegment, ABC):
    @property
    @abstractmethod
    def alignment(self) -> int:
        pass

    @abstractmethod
    def fill(self, object_record: "ObjectSectionRecord", section: "Section", labels: dict[str, int],
             templates: dict[str, dict[str, int]]):
        if (section.address + len(object_record.data)) % self.alignment != 0:
            _error(self, f'Segment must be {self.alignment}-byte aligned')
        super().fill(object_record, section, labels, templates)
        if section.name != '$abs':
            object_record.alignment = lcm(object_record.alignment, self.alignment)


def _error(segment: ICodeSegment, message: str):
    raise AssemblerException(AsmExceptionTag.ASM, segment.location.file, segment.location.line, message)
