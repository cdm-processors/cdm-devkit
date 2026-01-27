from collections import defaultdict
from dataclasses import dataclass, field
from pathlib import Path
from typing import Union

from .external_entry import ExternalEntry
from .location import CodeLocation
from .entry import Entry


@dataclass
class ObjectSectionRecord:
    """Structure that represents object code and debug information of a section"""
    name: str
    """Name of the relocatable section or '$abs' if it is absolute"""
    address: int
    """Address of the section. 0 for every relocatable section"""
    data: bytearray
    """Compiled binary image of that section before linking"""
    entries: dict[str, Entry]
    """Exported labels of this section and their Entries (address, attributes e.t.c.)"""
    relocatable: list[ExternalEntry]
    """Places where the address of this relocatable section should be added"""
    code_locations: dict[int, CodeLocation]
    """Mapping between addresses in binary image and locations in the source file"""
    alignment: int = field(default=1)
    """If the relocatable section should get address that is a multiple of some number"""
    external: defaultdict[str, list[ExternalEntry]] = field(default_factory=lambda: defaultdict(list))
    """List of places in section where some external label is used"""


@dataclass
class ObjectModule:
    """Object code representation of one translation unit (source file) with multiple sections, and debug information"""
    asects: list[ObjectSectionRecord]
    """Absolute sections"""
    rsects: list[ObjectSectionRecord]
    """Relocatable sections"""
    source_file_path: Union[Path, None] = field(default=None)
    """Path to the source files that is stated in object file FILE record"""
