from dataclasses import dataclass
from enum import IntEnum


@dataclass(frozen=True)
class Entry:
    "A symbol entry in a section of an object module."
    address: int
    "The offset from the start of the section this entry is defined at."

    def __str__(self):
        return f"{self.address:02x}"


@dataclass(frozen=True)
class EntryKey:
    "A key for identifying entries in sections."
    name: str
    "The name of this entry."
    linkage: Linkage
    "The linkage type of this entry."

    def __str__(self):
        match self.linkage:
            case Linkage.FILE_LOCAL:
                return f"{self.name} +LOCAL"
            case Linkage.WEAK_GLOBAL:
                return f"{self.name} +WEAK"
            case Linkage.GLOBAL:
                return f"{self.name} +GLOBAL"
            case _:
                return self.name


class Linkage(IntEnum):
    "Describes the way an entry or external is linked."
    FILE_LOCAL = 1
    "The entry is visible in the current object module only."
    GLOBAL = 2
    "The entry is visible in all object modules."
    WEAK_GLOBAL = 3
    """
    The entry is visible in all object modules.
    When applied to an entry, it makes it possible to override with a GLOBAL entry.
    When applied to an external, it becomes optional (e.g. doesn't throw an error
    when there is no matching entry, leaving the value as is.
    """
