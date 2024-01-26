from collections import defaultdict
from dataclasses import dataclass, field
from pathlib import Path
from typing import Union

from .external_entry import ExternalEntry
from .location import CodeLocation


@dataclass
class ObjectSectionRecord:
    name: str
    address: int
    data: bytearray
    entries: dict[str, int]
    relative: list[ExternalEntry]
    code_locations: dict[int, CodeLocation]
    alignment: int = field(default=1)

    external: defaultdict[str, list[ExternalEntry]] = field(default_factory=lambda: defaultdict(list))
    lower_parts: dict[int, int] = field(default_factory=dict)


@dataclass
class ObjectModule:
    asects: list[ObjectSectionRecord]
    rsects: list[ObjectSectionRecord]
    debug_info_path: Union[Path, None]
