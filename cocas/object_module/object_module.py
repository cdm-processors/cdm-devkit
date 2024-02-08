from collections import defaultdict
from dataclasses import dataclass, field
from pathlib import Path
from typing import Union

from .external_entry import ExternalEntry
from .location import CodeLocation


@dataclass
class ObjectSectionRecord:
    """Structure that represents object code and debug information of a section"""
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
    """Object code representation of one source file with multiple sections, and debug information"""
    asects: list[ObjectSectionRecord]
    rsects: list[ObjectSectionRecord]
    source_file_path: Union[Path, None] = field(default=None)
