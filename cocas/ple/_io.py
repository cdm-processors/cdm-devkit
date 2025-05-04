__all__ = (
    "round_up_div",
    "Reader",
    "Writer",
)

from typing import TYPE_CHECKING, TypeVar

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
    """Get such minimal `n`, that `(value + n) % divider == 0`."""
    r = value % divider
    return 0 if r == 0 else (divider - r)


class Reader:
    def __init__(self, fp: "SupportsRead[bytes]") -> None:
        self._fp: "SupportsRead[bytes]" = fp
        self._read: int = 0

    @property
    def read(self) -> int:
        """Number of read bytes."""
        return self._read

    def bytes(self, length: int) -> bytes:
        """Read exactly `length` bytes from the stream.

        Raises:
            ExhaustedStreamError:
                If there are no enough bytes.
        """
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
        """Read an unsigned byte.

        Raises:
            ExhaustedStreamError:
                If there are no enough bytes.
        """
        return int.from_bytes(self.bytes(1), byteorder="little", signed=False)

    def u16(self) -> int:
        """Read an unsigned short.

        Raises:
            ExhaustedStreamError:
                If there are no enough bytes.
        """
        return int.from_bytes(self.bytes(2), byteorder="little", signed=False)

    def skip(self, alignment: int, force: bool = False) -> None:
        """Read and discard `n` bytes; `(Reader.read + n) % alignment == 0`.

        Raises:
            ExhaustedStreamError:
                If there are no enough bytes.
        """
        r = reverse_rem(self._read, alignment)
        if r != 0 or force:
            _ = self.bytes(r or alignment)


class Writer:
    def __init__(self, fp: "SupportsWrite[bytes]") -> None:
        self._fp: "SupportsWrite[bytes]" = fp
        self._emitted: int = 0

    @property
    def emitted(self) -> int:
        """Number of written bytes."""
        return self._emitted

    def bytes(self: WriterT, value: bytes) -> WriterT:
        """Write `value` bytes to the stream.

        Raises:
            FailedWriteError:
                If write hasn't succeeded.
        """
        try:
            _ = self._fp.write(value)
        except Exception as exc:
            message = "failed to write payload to stream"
            raise FailedWriteError(message, value) from exc

        self._emitted += len(value)
        return self

    def u8(self: WriterT, value: int) -> WriterT:
        """Write unsigned byte `value` to the stream.

        Raises:
            FailedWriteError:
                If write hasn't succeeded.
        """
        return self.bytes(value.to_bytes(length=1, byteorder="little", signed=False))

    def u16(self: WriterT, value: int) -> WriterT:
        """Write unsigned short `value` to the stream.

        Raises:
            FailedWriteError:
                If write hasn't succeeded.
        """
        return self.bytes(value.to_bytes(length=2, byteorder="little", signed=False))

    def align(self: WriterT, alignment: int) -> WriterT:
        """Write `n` null bytes; `(Writer.emitted + n) % alignment == 0`."""
        r = reverse_rem(self._emitted, alignment)
        if r != 0:
            return self.bytes(bytes(r))
        return self
