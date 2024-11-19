import itertools
from collections.abc import Iterable, Sequence
from math import inf
from typing import Any, Optional

from cocas.object_module import CodeLocation, ObjectModule, ObjectSectionRecord, concat_rsects

from .exceptions import LinkerException
from .targets import TargetParams, import_target


def init_bins(asects: Sequence[ObjectSectionRecord], image_size: Optional[int]) -> list[tuple[int, int]]:
    rsect_bins: list[tuple[int, int]] = []
    last_bin_begin = 0
    for i in range(len(asects)):
        if len(asects[i].data) > 0:
            bin_size = asects[i].address - last_bin_begin
            if bin_size > 0:
                rsect_bins.append((last_bin_begin, bin_size))
            elif bin_size < 0:
                addr1 = asects[i - 1].address
                addr2 = asects[i].address
                len1 = len(asects[i - 1].data)
                len2 = len(asects[i].data)
                raise LinkerException(f'Overlapping sections at {addr1} (size {len1}) and {addr2} (size {len2})')
            last_bin_begin = asects[i].address + len(asects[i].data)
            if image_size and last_bin_begin > image_size:
                raise LinkerException(f'Absolute section at address {asects[i].address} (size {len(asects[i].data)}) '
                                      f'exceeds image size limit {image_size}')
    if image_size:
        if last_bin_begin < image_size:
            rsect_bins.append((last_bin_begin, image_size - last_bin_begin))
    else:
        rsect_bins.append((last_bin_begin, inf))  # type: ignore[arg-type]

    return rsect_bins


def place_sects(rsects: list[ObjectSectionRecord], rsect_bins: list[tuple[int, int]], image_size) -> dict[str, int]:
    sect_addresses = {'$abs': 0}
    for rsect in rsects:
        rsect_size = len(rsect.data)
        for i in range(len(rsect_bins)):
            bin_begin, bin_size = rsect_bins[i]
            if bin_size >= rsect_size:
                address = (bin_begin + rsect.alignment - 1) // rsect.alignment * rsect.alignment
                if address + rsect_size <= bin_begin + bin_size:
                    if rsect.name in sect_addresses:
                        raise LinkerException(f'Duplicate sections "{rsect.name}"')
                    sect_addresses[rsect.name] = address
                    rsect_bins[i] = (address + rsect_size, bin_size - rsect_size)
                    break
        else:
            raise LinkerException(f'Section "{rsect.name}" exceeds image size limit {image_size}')
    return sect_addresses


def gather_ents(sects: Iterable[ObjectSectionRecord], sect_addresses: dict[str, int]) -> dict[str, int]:
    ents = dict()
    for sect in sects:
        for ent_name in sect.entries:
            if ent_name in ents:
                raise LinkerException(f'Duplicate entries "{ent_name}"')
            ents[ent_name] = sect.entries[ent_name] + sect_addresses[sect.name]
    return ents


def find_exts_by_sect(sects: Iterable[ObjectSectionRecord]) -> dict[str, set[str]]:
    exts_by_sect = dict[str, set[str]]()
    for sect in sects:
        exts = exts_by_sect.setdefault(sect.name, set())
        exts |= set(sect.external.keys())
    return exts_by_sect


def find_sect_by_ent(sects: Iterable[ObjectSectionRecord]) -> dict[str, str]:
    sect_by_ent = dict()
    for sect in sects:
        for ent_name in sect.entries:
            if ent_name in sect_by_ent:
                raise LinkerException(f"Entry {ent_name} is declared in multiple sections")
            sect_by_ent[ent_name] = sect.name
    return sect_by_ent


def find_referenced_sects(exts_by_sect: dict[str, set[str]], sect_by_ent: dict[str, str]) -> set[str]:
    used_sects_queue = ['$abs']
    used_sects = {'$abs'}
    i = 0
    while i < len(used_sects_queue):
        if used_sects_queue[i] in exts_by_sect:
            for ext_name in exts_by_sect[used_sects_queue[i]]:
                if ext_name not in sect_by_ent:
                    raise LinkerException(f'Unresolved ext "{ext_name}"')
                new_sect = sect_by_ent[ext_name]
                if new_sect not in used_sects:
                    used_sects_queue.append(new_sect)
                    used_sects.add(new_sect)
        i += 1
    return used_sects


def link(
    objects: list[tuple[Any, ObjectModule]],
    image_size: Optional[int] = None,
) -> tuple[bytearray, dict[int, CodeLocation]]:
    """
    Link object modules into one image

    :param objects: list of pairs (file path, object module)
    :param image_size: maximum size of image for current target or None if no limit
    :return: pair [bytearray of image data, mapping from image addresses to locations in source files]
    """
    asects: list[ObjectSectionRecord] = list(itertools.chain.from_iterable([obj.asects for _, obj in objects]))
    try:
        rsects = concat_rsects(itertools.chain.from_iterable([obj.rsects for _, obj in objects]))
    except ValueError as e:
        raise LinkerException(str(e))

    exts_by_sect = find_exts_by_sect(asects + rsects)
    sect_by_ent = find_sect_by_ent(asects + rsects)
    used_sects = find_referenced_sects(exts_by_sect, sect_by_ent)

    rsects = [s for s in rsects if s.name in used_sects]
    rsects.sort(key=lambda s: -len(s.data))
    asects.sort(key=lambda s: s.address)

    rsect_bins = init_bins(asects, image_size)
    sect_addresses = place_sects(rsects, rsect_bins, image_size)
    ents = gather_ents(asects + rsects, sect_addresses)
    image = bytearray(2 ** 16)
    code_locations: dict[int, CodeLocation] = {}

    for asect in asects:
        image_begin = asect.address
        image_end = image_begin + len(asect.data)
        image[image_begin:image_end] = asect.data
        for loc_offset, location in asect.code_locations.items():
            code_locations[loc_offset + image_begin] = location

    lower_parts: dict[int, int] = {}  # Won't be empty if two entries added together, currently targets don't do that
    for rsect in rsects:
        image_begin = sect_addresses[rsect.name]
        image_end = image_begin + len(rsect.data)
        image[image_begin:image_end] = rsect.data
        for entry in rsect.relocatable:
            pos = image_begin + entry.offset
            lower_limit = 1 << 8 * entry.entry_bytes.start
            val = int.from_bytes(image[pos:pos + len(entry.entry_bytes)], 'little', signed=False) * lower_limit
            val += entry.lower_part + lower_parts.get(entry.offset, 0)
            val += image_begin * entry.sign
            val %= (1 << 8 * entry.entry_bytes.stop)
            if entry.entry_bytes.start > 0 and val % lower_limit != 0:
                lower_parts[pos] = val % lower_limit
            image[pos:pos + len(entry.entry_bytes)] = \
                (val // lower_limit).to_bytes(len(entry.entry_bytes), 'little', signed=False)
        for loc_offset, location in rsect.code_locations.items():
            code_locations[loc_offset + image_begin] = location

    for sect in asects + rsects:
        for ext_name in sect.external:
            for entry in sect.external[ext_name]:
                pos = sect_addresses[sect.name] + entry.offset
                lower_limit = 1 << 8 * entry.entry_bytes.start
                val = int.from_bytes(image[pos:pos + len(entry.entry_bytes)], 'little', signed=False) * lower_limit
                val += entry.lower_part + lower_parts.get(entry.offset, 0)
                val += ents[ext_name] * entry.sign
                val %= (1 << 8 * entry.entry_bytes.stop)
                image[pos:pos + len(entry.entry_bytes)] = \
                    (val // lower_limit).to_bytes(len(entry.entry_bytes), 'little', signed=False)
                if entry.entry_bytes.start > 0 and val % lower_limit != 0:
                    lower_parts[pos] = val % lower_limit

    return image, code_locations


def target_link(
    objects: list[tuple[Any, ObjectModule]],
    target_name: str,
) -> tuple[bytearray, dict[int, CodeLocation]]:
    """
    Link object modules with checking constraints for the target

    :param objects: list of pairs (file path, object module)
    :param target_name: name of the target
    :return: pair [bytearray of image data, mapping from image addresses to locations in source files]
    """
    params: TargetParams = import_target(target_name)
    return link(objects, params.image_size)
