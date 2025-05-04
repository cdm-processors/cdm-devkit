__all__ = (
    "round_up_div",
    "Reader",
    "Writer",
)

from typing import TYPE_CHECKING, Generic, TypeVar

from cocas.ple.exceptions import ExhaustedStreamError, FailedWriteError

if TYPE_CHECKING:
    from _typeshed import SupportsRead, SupportsWrite

T = TypeVar("T")
WriterT = TypeVar("WriterT", bound="Writer")


def round_up_div(value: int, multiple: int) -> int:
    """Like `//`, but rounds to ceil, not to floor."""
    c, r = divmod(value, multiple)
    return c + bool(r)


def reverse_rem(value: int, divider: int) -> int:
    r = value % divider
    return 0 if r == 0 else (divider - r)


class Handle(Generic[T]):
    def __init__(self, fp: T) -> None:
        self._fp: T = fp


class Reader(Handle["SupportsRead[bytes]"]):
    def __init__(self, fp: "SupportsRead[bytes]") -> None:
        super().__init__(fp)
        self._read: int = 0

    def bytes(self, length: int) -> bytes:
        try:
            b = self._fp.read(length)
        except Exception as exc:
            message = "failed to read byte chunk from stream"
            raise ExhaustedStreamError(message, None, length) from exc

        self._read += len(b)
        if len(b) != length:
            message = f"chunk from stream is too short (expected to read {length} bytes, while got only {len(b)} bytes)"
            raise ExhaustedStreamError(message, b, length)

        return b

    def u8(self) -> int:
        return int.from_bytes(self.bytes(1), byteorder="big", signed=False)

    def u16(self) -> int:
        return int.from_bytes(self.bytes(2), byteorder="big", signed=False)

    def skip(self, alignment: int) -> None:
        r = reverse_rem(self._read, alignment)
        if r != 0:
            _ = self.bytes(r)


class Writer(Handle["SupportsWrite[bytes]"]):
    def __init__(self, fp: "SupportsWrite[bytes]") -> None:
        super().__init__(fp)
        self._emitted: int = 0

    @property
    def emitted(self) -> int:
        return self._emitted

    def bytes(self: WriterT, value: bytes) -> WriterT:
        try:
            _ = self._fp.write(value)
        except Exception as exc:
            message = "failed to write payload to stream"
            raise FailedWriteError(message, value) from exc

        self._emitted += len(value)
        return self

    def u8(self: WriterT, value: int) -> WriterT:
        return self.bytes(value.to_bytes(length=1, byteorder="big", signed=False))

    def u16(self: WriterT, value: int) -> WriterT:
        return self.bytes(value.to_bytes(length=2, byteorder="big", signed=False))

    def align(self: WriterT, alignment: int) -> WriterT:
        r = reverse_rem(self._emitted, alignment)
        if r != 0:
            return self.bytes(bytes(r))
        return self
