from typing import Type

from cocas.ast_nodes import *
from cocas.default_code_segments import CodeSegmentsInterface
from cocas.error import CdmTempException


class TargetInstructionsInterface:
    @staticmethod
    def assemble_instruction(line: InstructionNode, temp_storage) \
            -> list[CodeSegmentsInterface.CodeSegment]:
        pass

    @staticmethod
    def finish(temp_storage: dict):
        if len(temp_storage.get("save_restore_stack", [])) != 0:
            raise CdmTempException("Missed restore statement")

    @staticmethod
    def make_branch_instruction(branch_mnemonic: str, label_name: str) \
            -> list[CodeSegmentsInterface.CodeSegment]:
        pass

    assembly_directives: dict
