from enum import Enum
from .attributes import Attributes

class Linkage(Enum):
    FILE_LOCAL = 1
    GLOBAL = 2
    WEAK_GLOBAL = 3

    def to_attribute(self):
        match self:
            case Linkage.FILE_LOCAL:
                return Attributes.LOCAL
            case Linkage.WEAK_GLOBAL:
                return Attributes.WEAK
            case _:
                return Attributes.NONE
