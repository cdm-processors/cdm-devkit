__all__ = (
    "MAGIC_BYTES",
    "SECTOR_SIZE",
    "PARAGRAPH_SIZE",
)

from typing import Final

MAGIC_BYTES: Final[bytes] = b"\x7fPLE"
"""todo: add docstring"""
SECTOR_SIZE: Final[int] = 512
"""todo: add docstring"""
PARAGRAPH_SIZE: Final[int] = 16
"""todo: add docstring"""
