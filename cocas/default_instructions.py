from typing import Type

from cocas.ast_nodes import *
from cocas.default_code_segments import CodeSegmentsInterface


class TargetInstructionsInterface:
    @staticmethod
    def assemble_instruction(line: InstructionNode) \
            -> list[CodeSegmentsInterface.CodeSegment]:
        pass

    instructions: dict
    assembly_directives: dict
