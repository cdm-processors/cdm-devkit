from enum import Enum
from typing import Optional
from .symbol_attribute import SymbolAttribute

class Linkage(Enum):
    FILE_LOCAL = 1
    GLOBAL = 2
    WEAK_GLOBAL = 3

    def to_attribute(self) -> Optional[SymbolAttribute]:
        match self:
            case Linkage.FILE_LOCAL:
                return SymbolAttribute.LOCAL
            case Linkage.WEAK_GLOBAL:
                return SymbolAttribute.WEAK
            case _:
                return None
