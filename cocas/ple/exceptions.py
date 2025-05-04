__all__ = (
    "PleException",
    "PleIoError",
    "ExhaustedStreamError",
    "FailedWriteError",
    "CorruptedImageError",
)

from cocas.exceptions import CocasException


class PleException(CocasException):
    """Base exception class for PLE utilities."""


class PleIoError(PleException):
    """I/O PLE errors."""


class ExhaustedStreamError(PleIoError):
    """Failed to read a requested number of bytes from stream."""
    def __init__(self, message: str, chunk: bytes | None, length: int) -> None:
        super().__init__(message)
        self.chunk: bytes | None = chunk
        """Successfully read bytes, if any."""
        self.length: int = length
        """Length of requested chunk."""


class FailedWriteError(PleIoError):
    """Failed to write to provided stream."""
    def __init__(self, message: str, payload: bytes) -> None:
        super().__init__(message)
        self.payload: bytes = payload
        """Payload, which was passed to `SupportsWrite[bytes].write`."""


class CorruptedImageError(PleException):
    """Provided image source is corrupted."""
    def __init__(self, message: str) -> None:
        super().__init__(message)
