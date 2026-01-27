from enum import Enum

class Attributes(Enum):
    LOCAL = 1,
    WEAK = 2

    def __str__(self):
        match self:
            case Attributes.LOCAL:
                return "LOCAL"
            case Attributes.WEAK:
                return "WEAK"
            case _:
                pass # do something
    
    