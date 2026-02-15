__all__ = ("concat_rsects",)

from copy import copy, deepcopy
from math import lcm
from typing import TYPE_CHECKING, Iterable

if TYPE_CHECKING:
    from cocas.object_module import ObjectSectionRecord


def concat_rsects(rsects: Iterable["ObjectSectionRecord"]) -> list["ObjectSectionRecord"]:
    """
    Concatenate rsects that have same name, put one right after another with proper alignment
    :param rsects: rsects with possibly different names, unsorted
    :throws: ValueError if sections with same name declare same entry (label)
    """
    grouped: dict[str, list["ObjectSectionRecord"]] = {}
    for rsect in rsects:
        grouped.setdefault(rsect.name, []).append(rsect)
    ret = []
    for name, sections in grouped.items():
        if len(sections) < 2:
            ret.extend(sections)
        else:
            new = deepcopy(sections[0])
            prev_size = len(new.data)
            for rsect in sections[1:]:
                if (missing_attrs := set(new.attributes).symmetric_difference(rsect.attributes)):
                    message = (
                        f"two sections with name {name} have different sets of attributes, "
                        f"different are: {missing_attrs}"
                    )
                    raise ValueError(message)
                new.alignment = lcm(new.alignment, rsect.alignment)
                prev_size = (prev_size + rsect.alignment - 1) // rsect.alignment * rsect.alignment
                new.data.extend(bytearray(prev_size - len(new.data)))
                new.data += rsect.data
                same_entries = new.entries.keys() & rsect.entries.keys()
                if same_entries:
                    raise ValueError(f"Two sections with same name {name} declare label {next(iter(same_entries))}")
                new.entries.update({entry: pos + prev_size for entry, pos in rsect.entries.items()})
                for pos, loc in rsect.code_locations.items():
                    new.code_locations[pos + prev_size] = loc
                for label, exts in rsect.external.items():
                    for i in exts:
                        t = copy(i)
                        t.offset += prev_size
                        new.external[label].append(t)
                for entry in rsect.relocatable:
                    t = copy(entry)
                    t.offset += prev_size
                    new.relocatable.append(t)
                    lower_limit = 1 << 8 * entry.entry_bytes.start
                    pos = t.offset
                    val = int.from_bytes(new.data[pos:pos + len(entry.entry_bytes)], 'little', signed=False) * lower_limit
                    val += entry.lower_part
                    val += prev_size
                    val %= (1 << 8 * entry.entry_bytes.stop)
                    if entry.entry_bytes.start > 0:
                        entry.lower_part = val % lower_limit
                    new.data[pos:pos + len(entry.entry_bytes)] = \
                        (val // lower_limit).to_bytes(len(entry.entry_bytes), 'little', signed=False)
                prev_size += len(rsect.data)
            ret.append(new)
    return ret
