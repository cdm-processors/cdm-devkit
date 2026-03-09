from dataclasses import dataclass
from math import lcm
from cocas.object_module import ObjectSectionRecord

@dataclass(frozen=True)
class RsectsGroup:
    "A group of rsects, which must be placed in image one right after another with proper alignment."
    name: str
    rsects: list[ObjectSectionRecord]
    "Rsects of the group"
    size: int
    "Size of the group"
    alignment: int
    "Alignment of the group"

    def __init__(self, name: str, rsects: list[ObjectSectionRecord]):
        object.__setattr__(self, "rsects", [])
        object.__setattr__(self, "name", name)

        if len(rsects) == 0:
            object.__setattr__(self, "size", 0)
            object.__setattr__(self, "alignment", 1)
            return

        self.rsects.append(rsects[0])
        size = len(rsects[0].data)
        alignment = rsects[0].alignment
        for rsect in rsects[1:]:
            alignment = lcm(alignment, rsect.alignment)
            aligned_size = (size + rsect.alignment - 1) // rsect.alignment * rsect.alignment
            self.rsects[-1].data.extend(bytearray(aligned_size - size))
            self.rsects.append(rsect)

            size = aligned_size + len(rsect.data)

        object.__setattr__(self, "size", size)
        object.__setattr__(self, "alignment", alignment)


def group_rsects(rsects: list[ObjectSectionRecord]) -> list[RsectsGroup]:
    """
    Groups rsects with same name into RsectsGroup.
    :param rsects: rsects with possibly different names, unsorted
    :returns: list of RsectsGroups sorted by names
    """
    ret: list[RsectsGroup] = []

    grouped: dict[str, list[ObjectSectionRecord]] = {}
    for rsect in rsects:
        grouped.setdefault(rsect.name, []).append(rsect)

    return list(map(lambda p: RsectsGroup(p[0], p[1]), sorted(grouped.items(), key = lambda p: p[0])))


