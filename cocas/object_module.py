from dataclasses import dataclass, field

from cocas.code_block import Section


@dataclass
class ExternalEntry:
    offset: int
    entry_bytes: range
    sign: int = field(default=1)


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
