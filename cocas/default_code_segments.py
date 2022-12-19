from cocas.location import CodeLocation
from dataclasses import dataclass, field

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from cocas.code_block import Section


class CodeSegmentsInterface:
    @dataclass
    class CodeSegment:
        base_size: int = field(init=False)
        position: int = field(init=False)

        def __post_init__(self):
            # ugly hack to store code location in segments
            # now this whole project is one big and ugly hack
            self.location: CodeLocation = CodeLocation()

        # noinspection PyMethodMayBeStatic
        def update_relative(self, section: "Section", local_labels: dict[str, int],
        # def update_relative(self, section, local_labels: dict[str, int],
                            templates: dict[str, dict[str, int]]):
            return False
