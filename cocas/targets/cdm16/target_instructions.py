from cocas.ast_nodes import InstructionNode
from cocas.default_code_segments import CodeSegmentsInterface
from cocas.default_instructions import TargetInstructionsInterface


class TargetInstructions(TargetInstructionsInterface):
    @staticmethod
    def assemble_instruction(line: InstructionNode, temp_storage) \
            -> list[CodeSegmentsInterface.CodeSegment]:
        return []
