from cocas.ast_nodes import *
from cocas.code_segments import *


class TargetInstructionsInterface:
    @staticmethod
    def target_instructions(line: InstructionNode) -> list[CodeSegment]:
        pass

    instructions = {}
    assembly_directives = {}
