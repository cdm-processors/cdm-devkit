from typing import get_origin, get_args

from cocas.ast_nodes import InstructionNode, RegisterNode, RelocatableExpressionNode
from cocas.default_code_segments import CodeSegmentsInterface
from cocas.default_instructions import TargetInstructionsInterface
from cocas.error import CdmTempException, CdmException, CdmExceptionTag
from .code_segments import CodeSegments


def assert_args(args, *types):
    ts = [((t,) if get_origin(t) is None else get_args(t)) for t in types]
    for i in range(len(args)):
        for j in ts[i]:
            if not isinstance(args[i], j):
                raise CdmTempException(f'Incompatible argument type {type(args[i])}')
        if isinstance(args[i], RegisterNode) and not 0 <= args[i].number <= 7:
            raise CdmTempException(f'Invalid register number r{args[i].number}')


class TargetInstructions(TargetInstructionsInterface):
    @staticmethod
    def assemble_instruction(line: InstructionNode, temp_storage) \
            -> list[CodeSegmentsInterface.CodeSegment]:
        try:
            if line.mnemonic == 'ldi':
                args = line.arguments
                if len(args) == 2:
                    assert_args(args, RegisterNode, RelocatableExpressionNode)
                    ldi = CodeSegments.LdiSegment(*args)
                    ldi.location = line.location
                    return [ldi]
                else:
                    raise CdmTempException(f'Expected 2 arguments, found {len(args)}')
            else:
                exit(-1)
        except CdmTempException as e:
            raise CdmException(CdmExceptionTag.ASM, line.location.file, line.location.line, e.message)

# if len(line.arguments) == 2:
#     assert_args(line.arguments, RegisterNode, Union[RegisterNode, RelocatableExpressionNode])
#     return
# elif len(line.arguments) == 3:
#     assert_args(line.arguments, RegisterNode, RegisterNode, RegisterNode)
# else:
#     raise CdmTempException(f'Expected 2 or 3 arguments, but found {len(line.arguments)}')
