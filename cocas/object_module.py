from collections import defaultdict
from dataclasses import dataclass, field

from cocas.code_block import Section


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

    def as_tuple(self):
        return self.offset, self.entry_bytes, self.sign


@dataclass
class ObjectSectionRecord:
    def __init__(self, section: Section, labels: dict[str, int], templates: dict[str, dict[str, int]]):
        self.address: int = section.address
        self.name: str = section.name
        self.data = bytearray()
        self.entries: dict[str, int] = dict(p for p in section.labels.items() if p[0] in section.ents)
        self.external: dict[str, list[ExternalEntry]] = dict()
        self.relative: list[ExternalEntry] = []
        self.lower_parts: dict[int, int] = dict()
        self.code_locations = section.code_locations
        self.alignment = 1

        for seg in section.segments:
            seg.fill(self, section, labels, templates)


@dataclass
class ObjectModule:
    def __init__(self):
        self.asects: list[ObjectSectionRecord] = []
        self.rsects: list[ObjectSectionRecord] = []


def data_to_str(array: bytearray):
    return ' '.join(map(lambda x: f'{x:02x}', array))


def sect_entry_to_str(pair: tuple[str, ExternalEntry]):
    name, entry = pair
    return f'{name} {entry}'


def export_obj(obj: ObjectModule) -> list[str]:
    result = []
    for asect in obj.asects:
        s = data_to_str(asect.data)
        result.append(f'ABS  {asect.address:02x}: {s}\n')
    for asect in obj.asects:
        for label, address in asect.entries.items():
            result.append(f'NTRY {label} {address:02x}\n')
    for rsect in obj.rsects:
        result.append(f'NAME {rsect.name}\n')
        s = data_to_str(rsect.data)
        result.append(f'DATA {s}\n')
        result.append(f'REL  {" ".join(map(str, rsect.relative))}\n')
        for label, address in rsect.entries.items():
            result.append(f'NTRY {label} {address:02x}\n')
    external = defaultdict(list)
    for sect in obj.asects + obj.rsects:
        for label, entries in sect.external.items():
            for entry in entries:
                external[label].append((sect.name, entry))
    for label, entries in external.items():
        result.append(f'XTRN {label}: {" ".join(map(sect_entry_to_str, entries))}\n')
        pass
    return result
