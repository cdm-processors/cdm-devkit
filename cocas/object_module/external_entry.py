from dataclasses import dataclass, field

from .attributes import Attributes

@dataclass
class ExternalEntry:
    """Describes where and how some unknown at compile time value will be placed over the binary image.
    Takes certain bytes of teh image as a number (maybe also from `lower_parts`) and adds the value.
    Used for external and relocatable entries."""
    offset: int
    """Position from start of the section where some value will be placed"""
    entry_bytes: range
    """Selection of bytes from binary representation of the added value"""
    sign: int = field(default=1)
    """Should value be added or subtracted (not tested with -1)"""
    full_bytes: bool = field(default=True)
    """Whether no bytes were excluded by entry_bytes. Used when exporting this to object file"""
    lower_part: int = field(default=0)
    """If least significant bytes are not selected, the corresponding bytes of the constant value 
    are saved to check for possible overflows."""

    def __str__(self):
        s = f'{self.sign * self.offset:02x}'
        if not self.full_bytes:
            s += f':{self.entry_bytes.start:x}:{self.entry_bytes.stop:x}'
            if self.lower_part:
                s += f'+{self.lower_part:x}'
        return s

    def __repr__(self):
        return str(self)

    def get_attrs_str(self):
        return ""

    def as_tuple(self):
        return self.offset, self.entry_bytes, self.sign
