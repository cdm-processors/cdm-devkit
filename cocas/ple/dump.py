__all__ = ("dump", "dumps")

from collections.abc import Callable
from functools import partial
from io import BytesIO
from typing import TYPE_CHECKING

from cocas.ple.constants import MAGIC_BYTES, PARAGRAPH_SIZE, SECTOR_SIZE, SEGMENT_HEADER_SIZE
from cocas.ple.types import PlainExecutable

if TYPE_CHECKING:
    from _typeshed import SupportsWrite

to_bytes = partial(int.to_bytes, byteorder="big", signed=False)
u8 = partial(to_bytes, length=1)
u16 = partial(to_bytes, length=2)


def fill(n: int, size: int) -> int:
    """todo: add docstring"""
    return 0 if n == size else size - (n % size)


def takes(n: int, size: int) -> int:
    fully_occupied, rem_bytes = divmod(n, size)
    return fully_occupied + bool(rem_bytes)


def writer(fp: "SupportsWrite[bytes]") -> Callable[[*tuple[bytes, ...]], int]:
    """Generate an auto-aligning write function for provided `fp`."""
    def write_bytes(*args: bytes, size: int = PARAGRAPH_SIZE) -> int:
        n = 0
        for arg in args:
            n += len(arg)
            _ = fp.write(arg)
        f = fill(n, size)
        if f:
            _ = fp.write(b"\x00" * f)
        return n + f
    return write_bytes


def dump(o: PlainExecutable, fp: "SupportsWrite[bytes]") -> int:
    """todo: add docstring"""
    write = writer(fp)

    n = write(MAGIC_BYTES, u8(o.version), u8(len(o.segments)), u16(o.entrypoint))
    headers_offset = n + (SEGMENT_HEADER_SIZE + fill(SEGMENT_HEADER_SIZE, PARAGRAPH_SIZE)) * len(o.segments)
    current_sector = takes(headers_offset, SECTOR_SIZE)

    for seg in o.segments:
        paragraphs = takes(len(seg.content), SEGMENT_HEADER_SIZE)
        n += write(
            u8(seg.type),
            u8(seg.flags),
            u16(current_sector),
            u16(paragraphs),
            u16(paragraphs),
            u16(seg.virtual_address),
        )

    for seg in o.segments:
        n += write(seg.content)

    return n


def dumps(o: PlainExecutable) -> bytes:
    """todo: add docstring"""
    buffer = BytesIO()
    dump(o, buffer)
    return buffer.getvalue()
