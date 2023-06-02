from dataclasses import dataclass, field
from typing import TYPE_CHECKING

from cocas.location import CodeLocation

if TYPE_CHECKING:
    from assembler import ObjectSectionRecord

    from cocas.code_block import Section


class CodeSegmentsInterface:
    @dataclass
    class CodeSegment:
        size: int = field(init=False)
        position: int = field(init=False)

        def __post_init__(self):
            # ugly hack to store code location in segments
            # now this whole project is one big and ugly hack
            self.location: CodeLocation = CodeLocation()

        def fill(self, object_record: "ObjectSectionRecord", section: "Section", labels: dict[str, int],
                 templates: dict[str, dict[str, int]]):
            pass

    @dataclass
    class VaryingLengthSegment(CodeSegment):
        def update_varying_length(self, pos, section: "Section", labels: dict[str, int],
                                  templates: dict[str, dict[str, int]]) -> int:
            pass
