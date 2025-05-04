__all__ = (
    "PleImage",
    "PleSegmentEntry",
    "PleSegmentType",
    "PleSegmentFlag",
)

import bisect
from collections.abc import Sequence
from dataclasses import dataclass, field
from enum import IntEnum, IntFlag, auto
from io import BytesIO
from typing import TYPE_CHECKING, SupportsIndex, TypeVar, cast

import cocas.ple._io as _io
from cocas.library import stdint
from cocas.ple.constants import MAGIC_BYTES, PARAGRAPH_SIZE, SECTOR_SIZE
from cocas.ple.exceptions import CorruptedImageError

if TYPE_CHECKING:
    from _typeshed import SupportsRead, SupportsWrite

PleImageT = TypeVar("PleImageT", bound="PleImage")
SENTINEL = object()


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
    memory_size: int = field(default=cast(int, SENTINEL), metadata=stdint.sized(16))
    type: PleSegmentType = field(default=PleSegmentType.NONE)
    flags: PleSegmentFlag = field(default=PleSegmentFlag(0))

    @property
    def physical_size(self) -> int:
        return _io.round_up(len(self.content), PARAGRAPH_SIZE)

    def __post_init__(self) -> None:
        if self.memory_size is SENTINEL:
            self.memory_size = self.physical_size


@stdint.validate
@dataclass
class PleImage:
    """todo: add docstring"""

    entrypoint: int = field(metadata=stdint.sized(16))
    version: int = field(default=1, metadata=stdint.sized(8))

    _segments: list[PleSegmentEntry] = field(default_factory=list, init=False)

    @property
    def segments(self) -> Sequence[PleSegmentEntry]:
        return self._segments

    def add(self: PleImageT, segment: PleSegmentEntry) -> PleImageT:
        self._segments.append(segment)
        return self

    def pop(self, index: SupportsIndex = -1) -> PleSegmentEntry | None:
        try:
            segment = self._segments.pop(index)
        except IndexError:
            segment = None

        return segment

    def dump(self, fp: "SupportsWrite[bytes]") -> int:
        writer = _io.Writer(fp)

        segments_n = len(self.segments)
        _ = writer.bytes(MAGIC_BYTES).u8(self.version).u8(segments_n).u16(self.entrypoint).align(PARAGRAPH_SIZE)

        headers_bytes = writer.emitted + PARAGRAPH_SIZE * segments_n
        sector_index = _io.round_up(headers_bytes, SECTOR_SIZE)

        for s in self.segments:
            _ = (
                writer.u8(s.type)
                .u8(s.flags)
                .u16(sector_index)
                .u16(s.physical_size)
                .u16(s.memory_size)
                .u16(s.virtual_address)
                .align(PARAGRAPH_SIZE)
            )
            sector_index += _io.round_up(len(s.content), SECTOR_SIZE)

        for s in self.segments:
            _ = writer.bytes(s.content).align(SECTOR_SIZE)

        return writer.emitted

    def dumps(self) -> bytes:
        buffer = BytesIO()
        _ = self.dump(buffer)
        return buffer.getvalue()

    @classmethod
    def load(cls: type[PleImageT], fp: "SupportsRead[bytes]") -> PleImageT:
        fp_reader = _io.Reader(fp)

        buffer = bytearray(fp_reader.bytes(SECTOR_SIZE))
        magic = buffer[0: len(MAGIC_BYTES)]
        if magic != MAGIC_BYTES:  # pyright: ignore[reportUnnecessaryComparison]
            message = f"first {len(MAGIC_BYTES)} of PLE expected to be '{MAGIC_BYTES}', while '{magic}' has been read"
            raise CorruptedImageError(message)

        index = len(MAGIC_BYTES)
        version = buffer[index]
        if version != 1:
            message = f"only version 1 is supported, while provided image is version {version}"
            raise NotImplementedError(message)
        index += 1

        segments_n = buffer[index]
        headers_sectors = _io.round_up((1 + segments_n) * PARAGRAPH_SIZE, SECTOR_SIZE)
        if headers_sectors > 1:
            buffer += fp_reader.bytes((headers_sectors - 1) * SECTOR_SIZE)

        buffer_reader = _io.Reader(BytesIO(buffer))
        buffer_reader.skip(index)
        entrypoint = buffer_reader.u16()
        buffer_reader.skip(PARAGRAPH_SIZE)

        entries_metadata: list[tuple[int, int, PleSegmentEntry]] = []
        for _ in range(segments_n):
            type = PleSegmentType(buffer_reader.u8())
            flags = PleSegmentFlag(buffer_reader.u8())
            physical_offset = buffer_reader.u16()
            physical_size = buffer_reader.u16()
            memory_size = buffer_reader.u16()
            virtual_address = buffer_reader.u16()
            entry = PleSegmentEntry(bytes(), virtual_address, memory_size, type, flags)
            bisect.insort(entries_metadata, (physical_offset, physical_size, entry), key=lambda x: x[0])

        current_offset = 0
        for physical_offset, physical_size, entry in entries_metadata:
            offset_delta = physical_offset - current_offset
            if offset_delta:
                buffer = buffer[offset_delta:]
                current_offset = physical_offset

            bytes_size = physical_size * PARAGRAPH_SIZE
            size_delta = bytes_size - len(buffer)
            if size_delta:
                buffer += fp_reader.bytes(_io.round_up(size_delta, SECTOR_SIZE))

            entry.content = bytes(buffer[0: bytes_size])

        image = cls(entrypoint)
        image._segments = [entry for _, _, entry in entries_metadata]
        return image

    @classmethod
    def loads(cls: type[PleImageT], s: bytes | bytearray) -> PleImageT:
        return cls.load(BytesIO(s))
