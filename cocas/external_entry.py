from dataclasses import dataclass, field


@dataclass
class ExternalEntry:
    offset: int
    entry_bytes: range
    sign: int = field(default=1)
    full_bytes: bool = field(default=True)

    def __str__(self):
        s = f'{self.sign * self.offset:02x}'
        if not self.full_bytes:
            s += f':{self.entry_bytes.start}:{self.entry_bytes.stop}'
        return s

    def __repr__(self):
        return str(self)

    def as_tuple(self):
        return self.offset, self.entry_bytes, self.sign
