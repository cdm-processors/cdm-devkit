from dataclasses import dataclass
from typing import Union


@dataclass
class CodeLocation:
    """Store information about to which place in the source file the instruction belongs."""
    file: Union[str, None] = None
    """Name of the source file that generated this instruction. None if unknown"""
    line: int = 0
    column: int = 0
