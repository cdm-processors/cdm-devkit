from collections import defaultdict
from dataclasses import dataclass

from cocas.abstract_params import TargetParamsInterface
from cocas.code_block import Section
from cocas.external_entry import ExternalEntry
from cocas.location import CodeLocation


class ObjectSectionRecord:
    def __init__(self, name: str, address: int, data: bytearray,
                 entries: dict[str, int], relative: list[ExternalEntry],
                 code_locations: dict[int, CodeLocation], alignment=1):
        self.name = name
        self.address = address
        self.data = data
        self.entries = entries
        self.relative = relative
        self.code_locations = code_locations
        self.alignment = alignment
        self.external: defaultdict[str, list[ExternalEntry]] = defaultdict(list)
        self.lower_parts: dict[int, int] = dict()

    @classmethod
    def from_section(cls, section: Section, labels: dict[str, int], templates: dict[str, dict[str, int]]):
        entries = dict(p for p in section.labels.items() if p[0] in section.ents)
        out = cls(section.name, section.address, bytearray(), entries, [], section.code_locations)
        for seg in section.segments:
            seg.fill(out, section, labels, templates)
        return out


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


def export_obj(obj: ObjectModule, target_params: TargetParamsInterface) -> list[str]:
    result = []
    if target_params.object_file_header():
        result.append(f'TARG {target_params.object_file_header()}\n')
    for asect in obj.asects:
        s = data_to_str(asect.data)
        result.append(f'ABS  {asect.address:02x}: {s}\n')
    for asect in obj.asects:
        for label, address in asect.entries.items():
            result.append(f'NTRY {label} {address:02x}\n')
    for rsect in obj.rsects:
        result.append(f'NAME {rsect.name}\n')
        if rsect.alignment != target_params.default_alignment():
            result.append(f'ALIG {rsect.alignment:02x}\n')
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
