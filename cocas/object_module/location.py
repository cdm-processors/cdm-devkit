from dataclasses import dataclass
from typing import Union


@dataclass
class CodeLocation:
    """
    Store information about to which place in the source file the instruction belongs.
    File is None if and only if there is no information for this line.
    """
    file: Union[str, None] = None
    line: int = 0
    column: int = 0
