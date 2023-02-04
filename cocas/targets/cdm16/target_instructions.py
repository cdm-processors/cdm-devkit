from dataclasses import dataclass
from typing import get_origin, get_args, Callable

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
    def assemble_instruction(line: InstructionNode, temp_storage: dict) -> list[CodeSegmentsInterface.CodeSegment]:
        try:
            for h in TargetInstructions.handlers:
                if line.mnemonic in h.instructions:
                    return h.handler(line, temp_storage, h.instructions[line.mnemonic])
            raise CdmException(CdmExceptionTag.ASM, line.location.file, line.location.line,
                               f'Unknown instruction "{line.mnemonic}"')
        except CdmTempException as e:
            raise CdmException(CdmExceptionTag.ASM, line.location.file, line.location.line, e.message)

    @staticmethod
    def ldi(line: InstructionNode, _, __) -> list[CodeSegmentsInterface.CodeSegment]:
        args = line.arguments
        if len(args) == 2:
            assert_args(args, RegisterNode, RelocatableExpressionNode)
            ldi = CodeSegments.LdiSegment(*args)
            ldi.location = line.location
            return [ldi]
        else:
            raise CdmTempException(f'Expected 2 arguments, found {len(args)}')

    @staticmethod
    def ds(line: InstructionNode, _, __):
        assert_args(line.arguments, RelocatableExpressionNode)
        arg = line.arguments[0]
        if len(arg.add_terms) != 0 or len(arg.sub_terms) != 0:
            raise CdmTempException('Number expected')
        if arg.const_term < 0:
            raise CdmTempException('Cannot specify negative size in "ds"')
        return [CodeSegments.BytesSegment(bytes(arg.const_term + arg.const_term % 2))]

    @staticmethod
    def dc(line: InstructionNode, _, __):
        if len(line.arguments) == 0:
            raise CdmTempException('At least one argument must be provided')
        data = []
        size = 0
        command = line.mnemonic
        for arg in line.arguments:
            if isinstance(arg, RelocatableExpressionNode):
                if len(arg.add_terms) != 0 or len(arg.sub_terms) != 0:
                    raise CdmTempException('Number expected')
                if command == 'db':
                    if -256 < arg.const_term < 256:
                        data.append(CodeSegments.BytesSegment((arg.const_term % 256).to_bytes(1, 'little')))
                        size += 1
                    else:
                        raise CdmTempException(f'Number is not a byte: {arg.const_term}')
                else:
                    if -65536 < arg.const_term < 65536:
                        data.append(CodeSegments.BytesSegment((arg.const_term % 65536).to_bytes(2, 'little')))
                        size += 2
                    else:
                        raise CdmTempException(f'Number is not a word: {arg.const_term}')
            elif isinstance(arg, str):
                if command == 'dw':
                    raise CdmTempException(f'Currently "dw" doesn\'t support strings')
                data.append(CodeSegments.BytesSegment(arg.encode('utf-8')))
        if sum(map(lambda x: x.size, data)) % 2 == 1:
            data.append(CodeSegments.BytesSegment(bytes(1)))
        return data

    @dataclass
    class Handler:
        handler: Callable[[InstructionNode, dict, int], list[CodeSegmentsInterface.CodeSegment]]
        instructions: dict[str, int]

    handlers: list[Handler]
    handlers = [
        Handler(ds, {'ds': -1}),
        Handler(dc, {'dc': -1, 'db': -1, 'dw': -1}),
        Handler(ldi, {'ldi': -1})
    ]
