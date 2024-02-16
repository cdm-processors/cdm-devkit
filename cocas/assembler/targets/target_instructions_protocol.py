from typing import TYPE_CHECKING, Protocol, runtime_checkable

from cocas.object_module import CodeLocation

from .abstract_code_segments import ICodeSegment

if TYPE_CHECKING:
    from ..ast_nodes import InstructionNode


@runtime_checkable
class TargetInstructions(Protocol):
    def assemble_instruction(self, line: "InstructionNode", temp_storage) -> list[ICodeSegment]:
        ...

    def finish(self, temp_storage: dict):
        ...

    def make_branch_instruction(self, location: CodeLocation, branch_mnemonic: str, label_name: str, inverse: bool) \
            -> list[ICodeSegment]:
        ...

    def assembly_directives(self) -> set[str]:
        ...
