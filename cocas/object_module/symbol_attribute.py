from enum import IntEnum

class SymbolAttribute(IntEnum):
    LOCAL = 1
    WEAK = 2

    def __str__(self):
        match self:
            case SymbolAttribute.LOCAL:
                return "LOCAL"
            case SymbolAttribute.WEAK:
                return "WEAK"
            case _:
                raise ValueError("Unknown symbol attribute")
