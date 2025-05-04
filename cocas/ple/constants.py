"""Plain Executalbe constants."""

__all__ = (
    "MAGIC_BYTES",
    "SECTOR_SIZE",
    "PARAGRAPH_SIZE",
)

from typing import Final

MAGIC_BYTES: Final[bytes] = b"\x7fPLE"
SECTOR_SIZE: Final[int] = 512
PARAGRAPH_SIZE: Final[int] = 16
