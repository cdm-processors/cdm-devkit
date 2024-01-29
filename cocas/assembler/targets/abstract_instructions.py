from typing import TYPE_CHECKING

from cocas.object_module import CodeLocation

from .abstract_code_segments import CodeSegmentsInterface

if TYPE_CHECKING:
    from cocas.assembler.ast_nodes import InstructionNode


class TargetInstructionsInterface:
    @staticmethod
    def assemble_instruction(line: "InstructionNode", temp_storage) \
            -> list[CodeSegmentsInterface.CodeSegment]:
        pass

    @staticmethod
    def finish(temp_storage: dict):
        return

    @staticmethod
    def make_branch_instruction(location: CodeLocation, branch_mnemonic: str, label_name: str, inverse: bool) \
            -> list[CodeSegmentsInterface.CodeSegment]:
        pass

    @staticmethod
    def assembly_directives() -> set[str]:
        pass