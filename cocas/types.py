__all__ = (
    "Address",
    "AttributeName",
    "EntryName",
    "ExtName",
    "SectionName",
    "ImageName",
    "Bin",
    "LinkedImage",
)

from typing import NamedTuple

from cocas.object_module.location import CodeLocation

Address = int
AttributeName = str
EntryName = str
ExtName = str
ImageName = str
SectionName = str


class Bin(NamedTuple):
    """Vacant space in memory for relocatable sections."""
    address: Address
    size: int


class LinkedImage(NamedTuple):
    image: bytearray
    code_locations: dict[Address, CodeLocation]
