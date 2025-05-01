__all__ = (
    "PlainExecutable",
    "PleSegmentEntry",
    "PleSegmentType",
    "PleSegmentFlag",
)

from collections.abc import Sequence
from dataclasses import dataclass, field
from enum import IntEnum, IntFlag, auto
from typing import SupportsIndex, TypeVar

from cocas.library import stdint

PleT = TypeVar("PleT", bound="PlainExecutable")


class PleSegmentType(IntEnum):
    """todo: add docstring"""
    NONE = auto()
    LOAD = auto()


class PleSegmentFlag(IntFlag):
    """todo: add docstring"""
    DATA = auto()
    WRITE_PROTECTED = auto()


@stdint.validate
@dataclass
class PleSegmentEntry:
    """todo: add docstring"""
    content: bytes
    virtual_address: int = field(metadata=stdint.sized(16))
    type: PleSegmentType = field(default=PleSegmentType.NONE)
    flags: PleSegmentFlag = field(default=PleSegmentFlag(0))


@stdint.validate
@dataclass
class PlainExecutable:
    """todo: add docstring"""
    entrypoint: int = field(metadata=stdint.sized(16))
    version: int = field(default=1, metadata=stdint.sized(8))

    _segments: list[PleSegmentEntry] = field(default_factory=list, init=False)

    @property
    def segments(self) -> Sequence[PleSegmentEntry]:
        return self._segments

    def add(self: PleT, segment: PleSegmentEntry) -> PleT:
        self._segments.append(segment)
        return self

    def pop(self, index: SupportsIndex = -1) -> PleSegmentEntry | None:
        try:
            segment = self._segments.pop(index)
        except IndexError:
            segment = None

        return segment
