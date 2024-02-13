import re
from copy import copy
from dataclasses import dataclass
from typing import Callable, Union, get_args, get_origin

from ...ast_nodes import InstructionNode, LabelNode, RegisterNode, RelocatableExpressionNode
from ...exceptions import AssemblerException, AssemblerExceptionTag, CdmTempException
from .. import ICodeSegment, TargetInstructionsInterface
from .code_segments import (
    AlignmentPaddingSegment,
    Branch,
    BytesSegment,
    ExpressionSegment,
    Imm6,
    Imm9,
    InstructionBytesSegment,
    LdiSegment,
    pack,
)


def assert_args(args, *types):
    ts = [((t,) if get_origin(t) is None else get_args(t)) for t in types]
    for i in range(len(args)):
        for j in ts[i]:
            if isinstance(args[i], j):
                break
        else:
            raise CdmTempException(f'Incompatible argument type {type(args[i])}')
        if isinstance(args[i], RegisterNode) and not 0 <= args[i].number <= 7:
            raise CdmTempException(f'Invalid register number r{args[i].number}')


def assert_count_args(args, *types):
    if len(args) != len(types):
        raise CdmTempException(f'Expected {len(types)} arguments, found {len(args)}')
    assert_args(args, *types)


def handle_frame_pointer(line: InstructionNode):
    for i in range(len(line.arguments)):
        arg = line.arguments[i]
        if isinstance(arg, RelocatableExpressionNode):
            if not arg.const_term and not arg.sub_terms and not arg.byte_specifier and len(arg.add_terms) == 1 \
                    and isinstance(arg.add_terms[0], LabelNode) and arg.add_terms[0].name == 'fp':
                line.arguments[i] = RegisterNode(7)


class TargetInstructions(TargetInstructionsInterface):
    @staticmethod
    def assemble_instruction(line: InstructionNode, temp_storage: dict) -> list[ICodeSegment]:
        handle_frame_pointer(line)
        try:
            for h in TargetInstructions.handlers:
                if line.mnemonic in h.instructions:
                    return h.handler(line, temp_storage, h.instructions[line.mnemonic])
            if line.mnemonic.startswith('b'):
                return TargetInstructions.branch(line)
            raise AssemblerException(AssemblerExceptionTag.ASM, line.location.file, line.location.line,
                                     f'Unknown instruction "{line.mnemonic}"')
        except CdmTempException as e:
            raise AssemblerException(AssemblerExceptionTag.ASM, line.location.file, line.location.line, e.message)

    @staticmethod
    def finish(temp_storage: dict):
        if len(temp_storage.get("save_restore_stack", [])) != 0:
            raise CdmTempException("Expected restore statement")

    @staticmethod
    def make_branch_instruction(location, branch_mnemonic: str, label_name: str, inverse: bool) \
            -> list[ICodeSegment]:
        instruction = InstructionNode('b' + branch_mnemonic,
                                      [RelocatableExpressionNode(None, [LabelNode(label_name)], [], 0)])
        instruction.location = location
        return TargetInstructions.branch(instruction, inverse)

    @staticmethod
    def ds(line: InstructionNode, _, __):
        assert_args(line.arguments, RelocatableExpressionNode)
        arg = line.arguments[0]
        if len(arg.add_terms) != 0 or len(arg.sub_terms) != 0:
            raise CdmTempException('Const number expected')
        if arg.const_term < 0:
            raise CdmTempException('Cannot specify negative size in "ds"')
        return [BytesSegment(bytes(arg.const_term), line.location)]

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
                        segments.append(BytesSegment((arg.const_term % 256).to_bytes(1, 'little'),
                                                     line.location))
                        size += 2
                    else:
                        raise CdmTempException(f'Number is not a byte: {arg.const_term}')
                else:
                    segments.append(ExpressionSegment(arg, line.location))
            elif isinstance(arg, str):
                if command == 'dw':
                    raise CdmTempException('Currently "dw" doesn\'t support strings')
                encoded = arg.encode('utf-8')
                segments.append(BytesSegment(encoded, line.location))
                size += len(encoded)
            else:
                raise CdmTempException(f'Incompatible argument type: {type(arg)}')
        return segments

    @staticmethod
    def align(line: InstructionNode, _, __):
        if len(line.arguments) > 0:
            assert_args(line.arguments, RelocatableExpressionNode)
            arg: RelocatableExpressionNode = line.arguments[0]
            if arg.add_terms or arg.sub_terms:
                raise CdmTempException('Const number expected')
            alignment = arg.const_term
        else:
            alignment = 2
        if alignment <= 0:
            raise CdmTempException('Alignment should be positive')
        elif alignment == 1:
            return []
        return [AlignmentPaddingSegment(alignment, line.location)]

    @staticmethod
    def save(line: InstructionNode, temp_storage: dict, __) -> list[ICodeSegment]:
        assert_args(line.arguments, RegisterNode)
        save_restore_stack: list[RegisterNode]
        save_restore_stack = temp_storage.get("save_restore_stack", [])
        save_restore_stack.append(line.arguments[0])
        temp_storage["save_restore_stack"] = save_restore_stack
        return TargetInstructions.assemble_instruction(InstructionNode("push", [line.arguments[0]]), temp_storage)

    @staticmethod
    def restore(line: InstructionNode, temp_storage: dict, __) -> list[ICodeSegment]:
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
    def ldi(line: InstructionNode, _, __) -> list[ICodeSegment]:
        assert_count_args(line.arguments, RegisterNode, RelocatableExpressionNode)
        return [LdiSegment(line.arguments[0], line.arguments[1], line.location)]

    @dataclass
    class BranchCode:
        condition: list[str]
        code: int
        inverse: list[str]
        inv_code: int

    branch_codes: list[BranchCode] = [BranchCode(['eq', 'z'], 0, ['ne', 'nz'], 1),
                                      BranchCode(['hs', 'cs'], 2, ['lo', 'cc'], 3),
                                      BranchCode(['mi'], 4, ['pl'], 5),
                                      BranchCode(['vs'], 6, ['vc'], 7),
                                      BranchCode(['hi'], 8, ['ls'], 9),
                                      BranchCode(['ge'], 10, ['lt'], 11),
                                      BranchCode(['gt'], 12, ['le'], 13),
                                      BranchCode(['anything', 'true', 'r'], 14, ['false'], 15)]

    @staticmethod
    def branch(line: InstructionNode, inverse=False) -> list[ICodeSegment]:
        cond = re.match(r'b(\w*)', line.mnemonic)[1]
        for pair in TargetInstructions.branch_codes:
            if cond in pair.condition:
                branch_code = pair.code if not inverse else pair.inv_code
                break
            elif cond in pair.inverse:
                branch_code = pair.inv_code if not inverse else pair.code
                break
        else:
            raise AssemblerException(AssemblerExceptionTag.ASM, line.location.file, line.location.line,
                                     f'Invalid branch condition: {cond}')
        assert_count_args(line.arguments, RelocatableExpressionNode)
        return [Branch(line.location, branch_code, line.arguments[0])]

    @staticmethod
    def op0(line: InstructionNode, _, op_number: int):
        assert_count_args(line.arguments)
        return [InstructionBytesSegment(pack("u5p7u4", 0b00000, op_number), line.location)]

    @staticmethod
    def const_only(arg: RelocatableExpressionNode):
        if arg.add_terms or arg.sub_terms:
            raise CdmTempException('Constant number expected as shift value')
        return arg.const_term

    @staticmethod
    def shifts(line: InstructionNode, _, op_number: int):
        args = line.arguments
        if len(args) == 3:
            assert_args(args, RegisterNode, RegisterNode, RelocatableExpressionNode)
            rs = args[0].number
            rd = args[1].number
            val = TargetInstructions.const_only(args[2])
        elif len(args) == 2 and isinstance(args[1], RegisterNode):
            assert_args(args, RegisterNode, RegisterNode)
            rs = args[0].number
            rd = args[1].number
            val = 1
        elif len(args) == 2:
            assert_args(args, RegisterNode, RelocatableExpressionNode)
            rs = args[0].number
            rd = args[0].number
            val = TargetInstructions.const_only(args[1])
        elif len(args) == 1:
            assert_args(args, RegisterNode)
            rs = args[0].number
            rd = args[0].number
            val = 1
        else:
            raise CdmTempException(f'Expected 1-3 arguments, found {len(args)}')
        if not 0 <= val <= 8:
            raise CdmTempException('Shift value out of range')
        if val == 0:
            return []
        return [
            InstructionBytesSegment(pack("u4u3u3u3u3", 0b0001, op_number, val - 1, rs, rd), line.location)]

    @staticmethod
    def op1(line: InstructionNode, _, op_number: int):
        assert_count_args(line.arguments, RegisterNode)
        reg = line.arguments[0].number
        return [InstructionBytesSegment(pack("u3p6u4u3", 0b001, op_number, reg), line.location)]

    @staticmethod
    def op2(line: InstructionNode, _, op_number: int):
        assert_count_args(line.arguments, RegisterNode, RegisterNode)
        rs = line.arguments[0].number
        rd = line.arguments[1].number
        return [InstructionBytesSegment(pack("u5p1u4u3u3", 0b01000, op_number, rs, rd), line.location)]

    @staticmethod
    def alu3_ind(line: InstructionNode, _, op_number: int):
        assert_count_args(line.arguments, RegisterNode, RegisterNode)
        rs = line.arguments[0].number
        rd = line.arguments[1].number
        return [InstructionBytesSegment(pack("u5p2u3u3u3", 0b01001, op_number, rs, rd), line.location)]

    @staticmethod
    def mem(line: InstructionNode, _, op_number: int):
        if len(line.arguments) == 2:
            assert_args(line.arguments, RegisterNode, RegisterNode)
            addr1 = line.arguments[0].number
            arg = line.arguments[1].number
            return [
                InstructionBytesSegment(pack("u5p1u4u3u3", 0b01010, op_number, addr1, arg), line.location)]
        elif len(line.arguments) == 3:
            assert_args(line.arguments, RegisterNode, RegisterNode, RegisterNode)
            addr1 = line.arguments[0].number
            addr2 = line.arguments[1].number
            arg = line.arguments[2].number
            return [InstructionBytesSegment(pack("u4u3u3u3u3", 0b1010, op_number, addr1, addr2, arg),
                                            line.location)]
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
        return [InstructionBytesSegment(pack("u5p2u3u3u3", 0b01011, op_number, rs, rd), line.location)]

    @staticmethod
    def imm6(line: InstructionNode, _, op_number: int) -> list[ICodeSegment]:
        assert_count_args(line.arguments, RegisterNode, RelocatableExpressionNode)
        return [Imm6(line.location, False, op_number, *line.arguments)]

    @staticmethod
    def imm6_word(line: InstructionNode, _, op_number: int) -> list[ICodeSegment]:
        assert_count_args(line.arguments, RegisterNode, RelocatableExpressionNode)
        return [Imm6(line.location, False, op_number, *line.arguments, word=True)]

    @staticmethod
    def alu3(line: InstructionNode, _, op_number: int):
        if len(line.arguments) == 3:
            assert_args(line.arguments, RegisterNode, RegisterNode, RegisterNode)
            arg1 = line.arguments[0].number
            arg2 = line.arguments[1].number
            dest = line.arguments[2].number
            return [InstructionBytesSegment(pack("u4u3u3u3u3", 0b1011, op_number, arg2, arg1, dest),
                                            line.location)]
        elif len(line.arguments) == 2:
            assert_args(line.arguments, RegisterNode, RegisterNode)
            arg1 = line.arguments[0].number
            arg2 = line.arguments[1].number
            return [InstructionBytesSegment(pack("u4u3u3u3u3", 0b1011, op_number, arg2, arg1, arg2),
                                            line.location)]
        else:
            raise CdmTempException(f'Expected 2 or 3 arguments, found {len(line.arguments)}')

    @staticmethod
    def special(line: InstructionNode, temp_storage: dict, _):
        if line.mnemonic == 'add':
            if len(line.arguments) == 2 and isinstance(line.arguments[1], RelocatableExpressionNode):
                assert_args(line.arguments, RegisterNode, RelocatableExpressionNode)
                return [Imm6(line.location, False, 6, *line.arguments)]
            else:
                return TargetInstructions.alu3(line, temp_storage, 4)
        elif line.mnemonic == 'sub':
            if len(line.arguments) == 2 and isinstance(line.arguments[1], RelocatableExpressionNode):
                assert_args(line.arguments, RegisterNode, RelocatableExpressionNode)
                return [Imm6(line.location, True, 6, *line.arguments)]
            else:
                return TargetInstructions.alu3(line, temp_storage, 6)
        elif line.mnemonic == 'cmp':
            if len(line.arguments) == 2 and isinstance(line.arguments[1], RelocatableExpressionNode):
                return [Imm6(line.location, False, 7, *line.arguments)]
            else:
                return TargetInstructions.alu3_ind(line, temp_storage, 6)
        elif line.mnemonic == 'int':
            assert_count_args(line.arguments, RelocatableExpressionNode)
            arg = line.arguments[0]
            if len(arg.add_terms) != 0 or len(arg.sub_terms) != 0:
                raise CdmTempException('Const number expected')
            if arg.const_term < 0:
                raise CdmTempException('Interrupt number must be not negative')
            return [InstructionBytesSegment(pack("u3u4s9", 0b100, 0, arg.const_term), line.location)]
        elif line.mnemonic == 'reset':
            if len(line.arguments) == 0:
                arg = RelocatableExpressionNode(None, [], [], 0)
            elif len(line.arguments) == 1:
                assert_args(line.arguments, RelocatableExpressionNode)
                arg = line.arguments[0]
            else:
                raise CdmTempException(f'Expected 0 or 1 arguments, found {len(line.arguments)}')
            if len(arg.add_terms) != 0 or len(arg.sub_terms) != 0:
                raise CdmTempException('Const number expected')
            if arg.const_term < 0:
                raise CdmTempException('Vector number must be not negative')
            return [InstructionBytesSegment(pack("u3u4s9", 0b100, 1, arg.const_term), line.location)]
        elif line.mnemonic == 'addsp':
            assert_count_args(line.arguments, Union[RelocatableExpressionNode, RegisterNode])
            if isinstance(line.arguments[0], RelocatableExpressionNode):
                arg = copy(line.arguments[0])
                if len(arg.add_terms) != 0 or len(arg.sub_terms) != 0:
                    raise CdmTempException('Const number expected')
                if arg.const_term % 2 == 1:
                    raise CdmTempException('Only even numbers can be added to stack pointer')
                arg.const_term //= 2
                return [Imm9(line.location, False, 2, arg)]
            else:
                reg = line.arguments[0].number
                return [InstructionBytesSegment(pack("u3p6u4u3", 0b001, 10, reg), line.location)]
        elif line.mnemonic == 'jsr':
            if len(line.arguments) == 1 and isinstance(line.arguments[0], RegisterNode):
                jsrr = copy(line)
                jsrr.mnemonic = 'jsrr'
                return TargetInstructions.assemble_instruction(jsrr, temp_storage)
            assert_count_args(line.arguments, RelocatableExpressionNode)
            return [Branch(line.location, 0, line.arguments[0], operation='jsr')]
        elif line.mnemonic == 'push':
            assert_count_args(line.arguments, Union[RegisterNode, RelocatableExpressionNode])
            if isinstance(line.arguments[0], RegisterNode):
                reg = line.arguments[0].number
                return [InstructionBytesSegment(pack("u3p6u4u3", 0b001, 0, reg), line.location)]
            else:
                return [Imm9(line.location, False, 1, *line.arguments)]

    @dataclass
    class Handler:
        handler: Callable[[InstructionNode, dict, int], list[ICodeSegment]]
        instructions: dict[str, int]

    handlers: list[Handler]

    handlers = [
        Handler(ds.__get__(object), {'ds': -1}),
        Handler(dc.__get__(object), {'dc': -1, 'db': -1, 'dw': -1}),
        Handler(align.__get__(object), {'align': -1}),
        Handler(save.__get__(object), {'save': -1}),
        Handler(restore.__get__(object), {'restore': -1}),
        Handler(ldi.__get__(object), {'ldi': -1}),
        Handler(op0.__get__(object), {'halt': 4, 'wait': 5, 'ei': 6, 'di': 7, 'rti': 9,
                                      'pupc': 10, 'popc': 11, 'pusp': 12, 'posp': 13, 'pups': 14, 'pops': 15}),
        Handler(shifts.__get__(object), {'shl': 0, 'shr': 1, 'shra': 2, 'rol': 3, 'ror': 4, 'rcl': 5, 'rcr': 6}),
        Handler(op1.__get__(object), {'pop': 1, 'jsrr': 3, 'ldsp': 4, 'stsp': 5,
                                      'ldps': 6, 'stps': 7, 'ldpc': 8, 'stpc': 9}),
        Handler(op2.__get__(object), {'move': 0}),
        Handler(alu3_ind.__get__(object), {'bit': 0}),
        Handler(mem.__get__(object), {'ldw': 0, 'ldb': 1, 'ldsb': 2, 'lcw': 3,
                                      'lcb': 4, 'lcsb': 5, 'stw': 6, 'stb': 7}),
        Handler(alu2.__get__(object), {'neg': 0, 'not': 1, 'sxt': 2, 'scl': 3}),
        Handler(imm6.__get__(object), {'lsb': 1, 'lssb': 2, 'ssb': 4}),
        Handler(imm6_word.__get__(object), {'lsw': 0, 'ssw': 3}),
        Handler(alu3.__get__(object), {'and': 0, 'or': 1, 'xor': 2, 'bic': 3, 'addc': 5, 'subc': 7}),
        Handler(special.__get__(object), {'add': -1, 'sub': -1, 'cmp': -1, 'int': -1,
                                          'reset': -1, 'addsp': -1, 'jsr': -1, 'push': -1})
    ]

    @staticmethod
    def assembly_directives():
        return {'ds', 'dc', 'db', 'dw'}
