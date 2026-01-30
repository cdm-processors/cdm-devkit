from enum import IntEnum

class Attributes(IntEnum):
    NONE = 0,
    LOCAL = 1,
    WEAK = 2

    def __str__(self):
        match self:
            case Attributes.LOCAL:
                return "LOCAL"
            case Attributes.WEAK:
                return "WEAK"
            case Attributes.NONE:
                return ""
            case _:
                pass # do something
