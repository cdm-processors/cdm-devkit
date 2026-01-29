import itertools
from math import inf
from typing import Any, Optional, Iterable

from cocas.object_module import CodeLocation, ObjectModule, ObjectSectionRecord, concat_rsects, Attributes

from .exceptions import LinkerException
from .targets import TargetParams, import_target


def init_bins(asects: list[ObjectSectionRecord], image_size: Optional[int]):
    rsect_bins = []
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
        rsect_bins.append((last_bin_begin, inf))

    return rsect_bins

def place_sects(rsects: list[ObjectSectionRecord], rsect_bins: list, image_size) -> dict[str, int]:
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


def find_referenced_sects(asects: list[ObjectSectionRecord], entry_by_ext: dict[int, (ObjectSectionRecord, Entry)]):
    used_sects_queue = asects.copy()
    used_sects = []
    i = 0
    while i < len(used_sects_queue):
        sect = used_sects_queue[i]
        used_sects.append(sect)

        for ext in sect.external:
            if not entry_by_ext[id(ext)] is None and not entry_by_ext[id(ext)][0] in used_sects_queue:
                used_sects_queue.append(entry_by_ext[id(ext)][0])
        i += 1
    return used_sects
    

def find_entries_for_exts(modules: list[ObjectModule]):
    # ret: id(ExternalEntryKey) -> (section, entry)
    ret: dict[int, (ObjectSectionRecord, Entry)] = {}

    # modules_scope: id(ObjectModule) -> (label -> (section, entry))
    modules_scope: dict[int, dict[str, (ObjectSectionRecord, Entry)]] = {}
    global_scope: dict[str, (ObjectSectionRecord, Entry)] = {}
    weak_global_scope: dict[str, list[(ObjectSectionRecord, Entry)]] = {}

    for module in modules:
        for sect in (module.rsects + module.asects):
            for name, entry in sect.entries.items():
                if Attributes.LOCAL in entry.attrs:
                    if id(module) in modules_scope and name in modules_scope[id(module)]:
                        raise LinkerException(f"File-local entry {name} is declared in multiple sections of the same object module")
                    modules_scope.setdefault(id(module), {})[name] = (sect, entry)
                elif Attributes.WEAK in entry.attrs:
                    weak_global_scope.setdefault(name, []).append((sect, entry))
                else:
                    if name in global_scope:
                        raise LinkerException(f"Global entry {name} is declared in multiple sections")
                    global_scope[name] = (sect, entry)

    for module in modules:
        for sect in (module.rsects + module.asects):
            for ext in sect.external:
                if Attributes.LOCAL in ext.attrs:
                    if (not id(module) in modules_scope) or (not ext.label in modules_scope[id(module)]):
                        raise LinkerException(f'Unresolved file-local ext "{ext.label}"')
                    ret[id(ext)] = modules_scope[id(module)][ext.label]
                elif Attributes.WEAK in ext.attrs:
                    if ext.label in global_scope:
                        ret[id(ext)] = global_scope[ext.label]
                    elif ext.label in weak_global_scope:
                        ret[id(ext)] = weak_global_scope[ext.label][0]
                    else:
                        ret[id(ext)] = None
                else:
                    if ext.label in global_scope:
                        ret[id(ext)] = global_scope[ext.label]
                    elif ext.label in weak_global_scope:
                        ret[id(ext)] = weak_global_scope[ext.label][0]
                    else:
                        raise LinkerException(f'Unresolved global ext "{ext.label}"')

    return ret


def link(objects: list[tuple[Any, ObjectModule]], image_size: Optional[int] = None) -> \
        tuple[bytearray, dict[int, CodeLocation]]:
    """
    Link object modules into one image

    :param objects: list of pairs (file path, object module)
    :param image_size: maximum size of image for current target or None if no limit
    :return: pair [bytearray of image data, mapping from image addresses to locations in source files]
    """
    entry_by_exts = find_entries_for_exts([obj for _, obj in objects])
    
    asects: list[ObjectSectionRecord] = list(itertools.chain.from_iterable([obj.asects for _, obj in objects]))
    used_sects = find_referenced_sects(asects, entry_by_exts)
    try:
        rsects = concat_rsects(filter(lambda rsect: rsect in used_sects, itertools.chain.from_iterable([obj.rsects for _, obj in objects])))
    except ValueError as e:
        raise LinkerException(str(e))

    rsects.sort(key=lambda s: -len(s.data))
    asects.sort(key=lambda s: s.address)

    rsect_bins = init_bins(asects, image_size)
    sect_addresses = place_sects(rsects, rsect_bins, image_size)

    image = bytearray(2 ** 16)
    code_locations: dict[int, CodeLocation] = {}

    # Writing asects data to image
    # Gathering code_locations from asects
    for asect in asects:
        image_begin = asect.address
        image_end = image_begin + len(asect.data)
        image[image_begin:image_end] = asect.data
        for loc_offset, location in asect.code_locations.items():
            code_locations[loc_offset + image_begin] = location

    # Writing rsects data to image
    # Rellocation
    # Gathering code_locations from rsects
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

    # Linking XTRNs with NTRYs
    for sect in asects + rsects:
        for ext_name in sect.external:
            if entry_by_exts[id(ext_name)] is None:
                symbol_value = 0
            else:
                symbol_sect, symbol = entry_by_exts[id(ext_name)]
                symbol_value = sect_addresses[symbol_sect.name] + symbol.address

            for entry in sect.external[ext_name]:
                pos = sect_addresses[sect.name] + entry.offset
                lower_limit = 1 << 8 * entry.entry_bytes.start
                val = int.from_bytes(image[pos:pos + len(entry.entry_bytes)], 'little', signed=False) * lower_limit
                val += entry.lower_part + lower_parts.get(entry.offset, 0)
                val += symbol_value * entry.sign
                val %= (1 << 8 * entry.entry_bytes.stop)
                image[pos:pos + len(entry.entry_bytes)] = \
                    (val // lower_limit).to_bytes(len(entry.entry_bytes), 'little', signed=False)
                if entry.entry_bytes.start > 0 and val % lower_limit != 0:
                    lower_parts[pos] = val % lower_limit

    return image, code_locations


def target_link(objects: list[tuple[Any, ObjectModule]], target_name: str) -> \
        tuple[bytearray, dict[int, CodeLocation]]:
    """
    Link object modules with checking constraints for the target

    :param objects: list of pairs (file path, object module)
    :param target_name: name of the target
    :return: pair [bytearray of image data, mapping from image addresses to locations in source files]
    """
    params: TargetParams = import_target(target_name)
    return link(objects, params.image_size)
