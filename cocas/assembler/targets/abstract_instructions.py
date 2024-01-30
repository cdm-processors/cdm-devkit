from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

from cocas.object_module import CodeLocation

from .abstract_code_segments import ICodeSegment

if TYPE_CHECKING:
    from cocas.assembler.ast_nodes import InstructionNode


class TargetInstructionsInterface(ABC):
    @staticmethod
    @abstractmethod
    def assemble_instruction(line: "InstructionNode", temp_storage) \
            -> list[ICodeSegment]:
        pass

    @staticmethod
    @abstractmethod
    def finish(temp_storage: dict):
        return

    @staticmethod
    @abstractmethod
    def make_branch_instruction(location: CodeLocation, branch_mnemonic: str, label_name: str, inverse: bool) \
            -> list[ICodeSegment]:
        pass

    @staticmethod
    @abstractmethod
    def assembly_directives() -> set[str]:
        pass
