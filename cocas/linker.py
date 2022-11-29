from cocas.assembler import ObjectSectionRecord, ObjectModule
import itertools

from cocas.error import CdmLinkException
from cocas.location import CodeLocation


def init_bins(asects: list[ObjectSectionRecord]):
    rsect_bins = []
    last_bin_begin = 0
    for i in range(len(asects)):
        bin_size = asects[i].address - last_bin_begin
        if bin_size > 0:
            rsect_bins.append((last_bin_begin, bin_size))
        elif bin_size < 0:
            addr1 = asects[i - 1].address
            addr2 = asects[i].address
            len1 = len(asects[i - 1].data)
            len2 = len(asects[i].data)
            raise CdmLinkException(f'Overlapping sections at {addr1} (size {len1}) and {addr2} (size {len2})')
        last_bin_begin = asects[i].address + len(asects[i].data)

    if last_bin_begin < 2 ** 16:
        rsect_bins.append((last_bin_begin, 2 ** 16 - last_bin_begin))

    return rsect_bins


def place_sects(rsects: list[ObjectSectionRecord], rsect_bins: list):
    sect_addresses = {'$abs': 0}
    for rsect in rsects:
        rsect_size = len(rsect.data)
        for i in range(len(rsect_bins)):
            bin_begin, bin_size = rsect_bins[i]
            if bin_size >= rsect_size:
                if rsect.name in sect_addresses:
                    raise CdmLinkException(f'Duplicate sections "{rsect.name}"')
                sect_addresses[rsect.name] = bin_begin
                rsect_bins[i] = (bin_begin + rsect_size, bin_size - rsect_size)
                break
        else:
            raise CdmLinkException(f'Section "{rsect.name}" exceeds image size limit')
    return sect_addresses


def gather_ents(sects: list[ObjectSectionRecord], sect_addresses: dict[str, int]):
    ents = dict()
    for sect in sects:
        for ent_name in sect.ents:
            if ent_name in ents:
                raise CdmLinkException(f'Duplicate entries "{ent_name}"')
            ents[ent_name] = sect.ents[ent_name] + sect_addresses[sect.name]
    return ents


def find_exts_by_sect(sects: list[ObjectSectionRecord]):
    exts_by_sect = dict()
    for sect in sects:
        exts = exts_by_sect.setdefault(sect.name, set())
        exts |= set(sect.xtrl.keys()) | set(sect.xtrh.keys())
    return exts_by_sect


def find_sect_by_ent(sects: list[ObjectSectionRecord]):
    sect_by_ent = dict()
    for sect in sects:
        for ent_name in sect.ents:
            sect_by_ent[ent_name] = sect.name
    return sect_by_ent


def find_referenced_sects(exts_by_sect: dict[str, set[str]], sect_by_ent: dict[str, str]):
    used_sects_queue = ['$abs']
    used_sects = {'$abs'}
    i = 0
    while i < len(used_sects_queue):
        if used_sects_queue[i] in exts_by_sect:
            for ext_name in exts_by_sect[used_sects_queue[i]]:
                if ext_name not in sect_by_ent:
                    raise CdmLinkException(f'Unresolved ext "{ext_name}"')
                new_sect = sect_by_ent[ext_name]
                if new_sect not in used_sects:
                    used_sects_queue.append(new_sect)
                    used_sects.add(new_sect)
        i += 1
    return used_sects


def link(objects: list[ObjectModule], isa):
    asects = list(itertools.chain.from_iterable([obj.asects for obj in objects]))
    rsects = list(itertools.chain.from_iterable([obj.rsects for obj in objects]))

    exts_by_sect = find_exts_by_sect(asects + rsects)
    sect_by_ent = find_sect_by_ent(asects + rsects)
    used_sects = find_referenced_sects(exts_by_sect, sect_by_ent)

    rsects = [s for s in rsects if s.name in used_sects]
    rsects.sort(key=lambda s: -len(s.data))
    asects.sort(key=lambda s: s.address)

    rsect_bins = init_bins(asects)
    sect_addresses = place_sects(rsects, rsect_bins)
    ents = gather_ents(asects + rsects, sect_addresses)
    image = bytearray(2 ** 16)
    code_locations: dict[int, CodeLocation] = {}

    for asect in asects:
        image_begin = asect.address
        image_end = image_begin + len(asect.data)
        image[image_begin:image_end] = asect.data
        for loc_offset, location in asect.code_locations.items():
            code_locations[loc_offset + image_begin] = location

    for rsect in rsects:
        image_begin = sect_addresses[rsect.name]
        image_end = image_begin + len(rsect.data)
        image[image_begin:image_end] = rsect.data
        for offset in rsect.rell:
            image[image_begin + offset] = (image[image_begin + offset] + image_begin) & 0xFF
        for offset, byte in rsect.relh:
            image[image_begin + offset] = (image[image_begin + offset] + (image_begin + byte) // 0x100) & 0xFF
        for loc_offset, location in rsect.code_locations.items():
            code_locations[loc_offset + image_begin] = location

    for sect in asects + rsects:
        for ext_name in sect.xtrl:
            for offset in sect.xtrl[ext_name]:
                image[sect_addresses[sect.name] + offset] = \
                    (image[sect_addresses[sect.name] + offset] + ents[ext_name]) & 0xFF
        for ext_name in sect.xtrh:
            for offset, byte in sect.xtrh[ext_name]:
                image[sect_addresses[sect.name] + offset] = \
                    (image[sect_addresses[sect.name] + offset] + (ents[ext_name] + byte) // 0x100) & 0xFF

    return image, code_locations
