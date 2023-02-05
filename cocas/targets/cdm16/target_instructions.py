from dataclasses import dataclass
from typing import get_origin, get_args, Callable
import re

from cocas.ast_nodes import InstructionNode, RegisterNode, RelocatableExpressionNode
from cocas.default_code_segments import CodeSegmentsInterface
from cocas.default_instructions import TargetInstructionsInterface
from cocas.error import CdmTempException, CdmException, CdmExceptionTag
from .code_segments import CodeSegments, pack


def assert_args(args, *types):
    ts = [((t,) if get_origin(t) is None else get_args(t)) for t in types]
    for i in range(len(args)):
        for j in ts[i]:
            if not isinstance(args[i], j):
                raise CdmTempException(f'Incompatible argument type {type(args[i])}')
        if isinstance(args[i], RegisterNode) and not 0 <= args[i].number <= 7:
            raise CdmTempException(f'Invalid register number r{args[i].number}')


def assert_count_args(args, *types):
    if len(args) != len(types):
        raise CdmTempException(f'Expected {len(types)} arguments, found {len(args)}')
    assert_args(args, *types)


class TargetInstructions(TargetInstructionsInterface):
    @staticmethod
    def assemble_instruction(line: InstructionNode, temp_storage: dict) -> list[CodeSegmentsInterface.CodeSegment]:
        try:
            for h in TargetInstructions.handlers:
                if line.mnemonic in h.instructions:
                    return h.handler(line, temp_storage, h.instructions[line.mnemonic])
            if line.mnemonic.startswith('b'):
                return TargetInstructions.branch(line, temp_storage)
            raise CdmException(CdmExceptionTag.ASM, line.location.file, line.location.line,
                               f'Unknown instruction "{line.mnemonic}"')
        except CdmTempException as e:
            raise CdmException(CdmExceptionTag.ASM, line.location.file, line.location.line, e.message)

    @staticmethod
    def finish(temp_storage: dict):
        if len(temp_storage.get("save_restore_stack", [])) != 0:
            raise CdmTempException("Expected restore statement")

    @staticmethod
    def ds(line: InstructionNode, _, __):
        assert_args(line.arguments, RelocatableExpressionNode)
        arg = line.arguments[0]
        if len(arg.add_terms) != 0 or len(arg.sub_terms) != 0:
            raise CdmTempException('Number expected')
        if arg.const_term < 0:
            raise CdmTempException('Cannot specify negative size in "ds"')
        return [CodeSegments.BytesSegment(bytes(arg.const_term + arg.const_term % 2), line.location)]

    @staticmethod
    def dc(line: InstructionNode, _, __):
        if len(line.arguments) == 0:
            raise CdmTempException('At least one argument must be provided')
        segments = []
        size = 0
        command = line.mnemonic
        for arg in line.arguments:
            if isinstance(arg, RelocatableExpressionNode):
                if command == 'db':
                    if len(arg.add_terms) != 0 or len(arg.sub_terms) != 0:
                        raise CdmTempException('Only constants allowed for 1 byte')
                    if -128 < arg.const_term < 256:
                        segments.append(CodeSegments.BytesSegment((arg.const_term % 256).to_bytes(1, 'little'),
                                                                  line.location))
                        size += 2
                    else:
                        raise CdmTempException(f'Number is not a byte: {arg.const_term}')
                else:
                    segments.append(CodeSegments.ExpressionSegment(line.location, arg))
            elif isinstance(arg, str):
                if command == 'dw':
                    raise CdmTempException(f'Currently "dw" doesn\'t support strings')
                encoded = arg.encode('utf-8')
                if command == 'dc':
                    if len(encoded) % 2 == 1:
                        encoded += bytes(1)
                    segments.append(CodeSegments.AlignedBytesSegment(encoded, line.location))
                else:
                    segments.append(CodeSegments.BytesSegment(encoded, line.location))
                size += len(encoded)
            else:
                raise CdmTempException(f'Incompatible argument type: {type(arg)}')
        if size % 2 == 1:
            segments.append(CodeSegments.BytesSegment(bytes(1), line.location))
        return segments

    @staticmethod
    def save(line: InstructionNode, temp_storage: dict, __) -> list[CodeSegmentsInterface.CodeSegment]:
        assert_args(line.arguments, RegisterNode)
        save_restore_stack: list[RegisterNode]
        save_restore_stack = temp_storage.get("save_restore_stack", [])
        save_restore_stack.append(line.arguments[0])
        temp_storage["save_restore_stack"] = save_restore_stack
        return TargetInstructions.assemble_instruction(InstructionNode("push", [line.arguments[0]]), temp_storage)

    @staticmethod
    def restore(line: InstructionNode, temp_storage: dict, __) -> list[CodeSegmentsInterface.CodeSegment]:
        assert_args(line.arguments, RegisterNode)
        save_restore_stack: list[RegisterNode]
        save_restore_stack = temp_storage.get("save_restore_stack", [])
        if len(save_restore_stack) == 0:
            raise CdmTempException("Every restore statement must be preceded by a save statement")
        reg = save_restore_stack.pop()
        if len(line.arguments) > 0:
            assert_args(line.arguments, RegisterNode)
            reg = line.arguments[0]
        return TargetInstructions.assemble_instruction(InstructionNode("pop", [reg]), temp_storage)

    @staticmethod
    def ldi(line: InstructionNode, _, __) -> list[CodeSegmentsInterface.CodeSegment]:
        assert_count_args(line.arguments, RegisterNode, RelocatableExpressionNode)
        return [CodeSegments.LdiSegment(line.location, *line.arguments)]

    branch_codes = {'eq': 0, 'z': 0, 'nne': 0, 'nnz': 0, 'ne': 1, 'nz': 1, 'neq': 1,
                    'hs': 2, 'cs': 2, 'nlo': 2, 'ncc': 2, 'lo': 3, 'cc': 3, 'nhs': 3, 'ncs': 3,
                    'mi': 4, 'npl': 4, 'pl': 5, 'nmi': 5, 'vs': 6, 'nvc': 6, 'vc': 7, 'nvs': 7,
                    'hi': 8, 'nlc': 8, 'ls': 9, 'nhi': 9, 'ge': 10, 'nlt': 10, 'lt': 11, 'nge': 11,
                    'gt': 12, 'nle': 12, 'le': 13, 'ngt': 13, 'r': 14, 'anything': 14, 'true': 14, 'nfalse': 14,
                    'op': 15, 'nanything': 15, 'ntrue': 15, 'false': 15}

    @staticmethod
    def branch(line: InstructionNode, _) -> list[CodeSegmentsInterface.CodeSegment]:
        cond = re.match(r'b(\w*)', line.mnemonic)[1]
        if cond not in TargetInstructions.branch_codes:
            raise CdmTempException(f'Invalid branch condition: {cond}')
        assert_count_args(line.arguments, RelocatableExpressionNode)
        code = TargetInstructions.branch_codes[cond]
        return [CodeSegments.BytesSegment(pack("u5p7u4", 0x00001, code), line.location),
                CodeSegments.ExpressionSegment(line.location, line.arguments[0])]

    @staticmethod
    def op0(line: InstructionNode, _, op_number: int):
        assert_count_args(line.arguments)
        return [CodeSegments.BytesSegment(pack("u5p7u4", 0b00000, op_number), line.location)]

    @staticmethod
    def op1(line: InstructionNode, _, op_number: int):
        assert_count_args(line.arguments, RegisterNode)
        reg = line.arguments[0].number
        return [CodeSegments.BytesSegment(pack("u3p6u4u3", 0b001, op_number, reg), line.location)]

    @staticmethod
    def op2(line: InstructionNode, _, op_number: int):
        assert_count_args(line.arguments, RegisterNode, RegisterNode)
        rs = line.arguments[0].number
        rd = line.arguments[1].number
        return [CodeSegments.BytesSegment(pack("u5p1u4u3u3", 0b01000, op_number, rs, rd), line.location)]

    @staticmethod
    def alu3_ind(line: InstructionNode, _, op_number: int):
        assert_count_args(line.arguments, RegisterNode, RegisterNode)
        rs = line.arguments[0].number
        rd = line.arguments[1].number
        return [CodeSegments.BytesSegment(pack("u5p2u3u3u3", 0b01001, op_number, rs, rd), line.location)]

    @staticmethod
    def mem(line: InstructionNode, _, op_number: int):
        if len(line.arguments) == 2:
            assert_args(line.arguments, RegisterNode, RegisterNode)
            addr1 = line.arguments[0].number
            arg = line.arguments[1].number
            return [CodeSegments.BytesSegment(pack("u5p1u4u3u3", 0b01010, op_number, addr1, arg), line.location)]
        elif len(line.arguments) == 3:
            assert_args(line.arguments, RegisterNode, RegisterNode, RegisterNode)
            addr1 = line.arguments[0].number
            addr2 = line.arguments[1].number
            arg = line.arguments[2].number
            return [CodeSegments.BytesSegment(pack("u4u3u3u3u3", 0b1010, op_number, addr1, addr2, arg), line.location)]
        else:
            raise CdmTempException(f'Expected 2 or 3 arguments, found {len(line.arguments)}')

    @staticmethod
    def alu2(line: InstructionNode, _, op_number: int):
        if len(line.arguments) == 2:
            assert_args(line.arguments, RegisterNode, RegisterNode)
            rd = line.arguments[1].number
        elif len(line.arguments) == 1:
            assert_args(line.arguments, RegisterNode)
            rd = line.arguments[0].number
        else:
            raise CdmTempException(f'Expected 1 or 2 arguments, found {len(line.arguments)}')
        rs = line.arguments[0].number
        return [CodeSegments.BytesSegment(pack("u5p2u3u3u3", 0b01011, op_number, rs, rd), line.location)]

    @staticmethod
    def imm6(line: InstructionNode, _, op_number: int) -> list[CodeSegmentsInterface.CodeSegment]:
        assert_count_args(line.arguments, RegisterNode, RelocatableExpressionNode)
        return [CodeSegments.Imm6(line.location, False, op_number, *line.arguments)]

    @staticmethod
    def alu3(line: InstructionNode, _, op_number: int):
        if len(line.arguments) == 3:
            assert_args(line.arguments, RegisterNode, RegisterNode, RegisterNode)
            arg1 = line.arguments[0].number
            arg2 = line.arguments[1].number
            dest = line.arguments[2].number
            return [CodeSegments.BytesSegment(pack("u4u3u3u3u3", 0b1011, op_number, arg2, arg1, dest), line.location)]
        elif len(line.arguments) == 2:
            assert_args(line.arguments, RegisterNode, RegisterNode)
            arg1 = line.arguments[0].number
            arg2 = line.arguments[1].number
            return [CodeSegments.BytesSegment(pack("u4u3u3u3u3", 0b1011, op_number, arg2, arg1, arg2),
                                              line.location)]
        else:
            raise CdmTempException(f'Expected 2 or 3 arguments, found {len(line.arguments)}')

    @staticmethod
    def may_imm(line: InstructionNode, temp_storage: dict, _):
        if line.mnemonic == 'add':
            if len(line.arguments) == 2 and isinstance(line.arguments[1], RelocatableExpressionNode):
                assert_args(line.arguments, RegisterNode, RelocatableExpressionNode)
                return [CodeSegments.Imm6(line.location, False, 6, *line.arguments)]
            else:
                return TargetInstructions.alu3(line, temp_storage, 4)
        elif line.mnemonic == 'sub':
            if len(line.arguments) == 2 and isinstance(line.arguments[1], RelocatableExpressionNode):
                assert_args(line.arguments, RegisterNode, RelocatableExpressionNode)
                return [CodeSegments.Imm6(line.location, True, 6, *line.arguments)]
            else:
                return TargetInstructions.alu3(line, temp_storage, 6)
        elif line.mnemonic == 'cmp':
            if len(line.arguments) == 2 and isinstance(line.arguments[1], RelocatableExpressionNode):
                return [CodeSegments.Imm6(line.location, False, 7, *line.arguments)]
            else:
                return TargetInstructions.alu3_ind(line, temp_storage, 6)

        # n = len(line.arguments)
        # if n == 3:
        #     assert_args(line.arguments, RegisterNode, RegisterNode, RegisterNode)
        # elif n == 2:
        #     assert_args(line.arguments, RegisterNode, RelocatableExpressionNode)
        # else:
        #     raise CdmTempException(f'Expected 2 or 3 arguments, found {len(line.arguments)}')

    @dataclass
    class Handler:
        handler: Callable[[InstructionNode, dict, int], list[CodeSegmentsInterface.CodeSegment]]
        instructions: dict[str, int]

    handlers: list[Handler]
    handlers = [
        Handler(ds, {'ds': -1}),
        Handler(dc, {'dc': -1, 'db': -1, 'dw': -1}),
        Handler(save, {'save': -1}),
        Handler(restore, {'restore': -1}),
        Handler(ldi, {'ldi': -1}),
        Handler(op0, {'halt': 4, 'wait': 5, 'ei': 6, 'di': 7, 'jsr': 8, 'rti': 9,
                      'pupc': 10, 'popc': 11, 'pusp': 12, 'posp': 13, 'pups': 14, 'pops': 15}),
        Handler(op1, {'push': 0, 'pop': 1, 'jsrr': 3, 'ldsp': 4, 'stsp': 5,
                      'ldps': 6, 'stps': 7, 'ldpc': 8, 'stpc': 9}),
        Handler(op2, {'move': 0}),
        Handler(alu3_ind, {'bit': 0}),
        Handler(mem, {'ldw': 0, 'ldb': 1, 'ldsb': 2, 'lcw': 3, 'lcb': 4, 'lcsb': 5, 'stw': 6, 'stb': 7}),
        Handler(alu2, {'neg': 0, 'not': 1, 'sxt': 2, 'scl': 3}),
        Handler(imm6, {'lsw': 0, 'lsb': 1, 'lssb': 2, 'ssw': 3, 'ssb': 4}),
        Handler(alu3, {'and': 0, 'or': 1, 'xor': 2, 'bic': 3, 'addc': 5, 'subc': 7}),
        Handler(may_imm, {'add': -1, 'sub': -1, 'cmp': -1}),
    ]
