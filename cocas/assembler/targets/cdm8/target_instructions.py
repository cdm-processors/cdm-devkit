import re
from dataclasses import dataclass
from typing import Callable, get_args, get_origin

from bitstruct import pack

from ...ast_nodes import InstructionNode, LabelNode, RegisterNode, RelocatableExpressionNode
from ...exceptions import AssemblerException, AssemblerExceptionTag, CdmTempException
from .. import ICodeSegment
from .code_segments import AlignmentPaddingSegment, BytesSegment, ExpressionSegment


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


def assemble_instruction(line: InstructionNode, temp_storage: dict) -> list[ICodeSegment]:
    try:
        for h in handlers:
            if line.mnemonic in h.instructions:
                return h.handler(line, temp_storage, h.instructions[line.mnemonic])
        if line.mnemonic.startswith('b'):
            return branch(line)
        raise AssemblerException(AssemblerExceptionTag.ASM, line.location.file, line.location.line,
                                 f'Unknown instruction "{line.mnemonic}"')
    except CdmTempException as e:
        raise AssemblerException(AssemblerExceptionTag.ASM, line.location.file, line.location.line, e.message)


def finish(temp_storage: dict):
    if len(temp_storage.get("save_restore_stack", [])) != 0:
        raise CdmTempException("Expected restore statement")


def make_branch_instruction(location, branch_mnemonic: str, label_name: str, inverse: bool) \
        -> list[ICodeSegment]:
    instruction = InstructionNode('b' + branch_mnemonic,
                                  [RelocatableExpressionNode(None, [LabelNode(label_name)], [], 0)])
    instruction.location = location
    return branch(instruction, inverse)


def ds(line: InstructionNode, _, __):
    assert_args(line.arguments, RelocatableExpressionNode)
    arg = line.arguments[0]
    if arg.const_term < 0:
        raise CdmTempException('Cannot specify negative size in "ds"')
    if len(arg.add_terms) != 0 or len(arg.sub_terms) != 0:
        raise CdmTempException('Const number expected')
    return [BytesSegment(bytes(arg.const_term), line.location)]


def dc(line: InstructionNode, _, __):
    if len(line.arguments) == 0:
        raise CdmTempException('At least one argument must be provided')
    segments = []
    size = 0
    for arg in line.arguments:
        if isinstance(arg, RelocatableExpressionNode):
            segments.append(ExpressionSegment(arg, line.location))
        elif isinstance(arg, bytes):
            segments.append(BytesSegment(arg, line.location))
            size += len(arg)
        else:
            raise CdmTempException(f'Incompatible argument type: {type(arg)}')
    return segments


def align(line: InstructionNode, _, __):
    assert_args(line.arguments, RelocatableExpressionNode)
    arg: RelocatableExpressionNode = line.arguments[0]
    if arg.add_terms or arg.sub_terms:
        raise CdmTempException('Const number expected')
    alignment = arg.const_term
    if alignment <= 0:
        raise CdmTempException('Alignment should be positive')
    elif alignment == 1:
        return []
    return [AlignmentPaddingSegment(alignment, line.location)]


def save(line: InstructionNode, temp_storage: dict, __) -> list[ICodeSegment]:
    assert_args(line.arguments, RegisterNode)
    save_restore_stack: list[RegisterNode]
    save_restore_stack = temp_storage.get("save_restore_stack", [])
    save_restore_stack.append(line.arguments[0])
    temp_storage["save_restore_stack"] = save_restore_stack
    return assemble_instruction(InstructionNode("push", [line.arguments[0]]), temp_storage)


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
    return assemble_instruction(InstructionNode("pop", [reg]), temp_storage)


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


def branch(line: InstructionNode, inverse=False) -> list[ICodeSegment]:
    cond = re.match(r'b(\w*)', line.mnemonic)[1]
    for pair in branch_codes:
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
    return [BytesSegment(pack('u4u4', 0xE, branch_code), line.location),
            ExpressionSegment(line.arguments[0], line.location)]


def zero(line: InstructionNode, _, opcode: int):
    assert_count_args(line.arguments)
    return [BytesSegment(bytearray([opcode]), line.location)]


def unary(line: InstructionNode, _, opcode: int):
    assert_args(line.arguments, RegisterNode)
    data = pack('u6u2', opcode // 4, line.arguments[0].number)
    return [BytesSegment(bytearray(data), line.location)]


def binary(line: InstructionNode, _, opcode: int):
    assert_args(line.arguments, RegisterNode, RegisterNode)
    data = pack('u4u2u2', opcode // 16, line.arguments[0].number, line.arguments[1].number)
    return [BytesSegment(bytearray(data), line.location)]


def imm(line: InstructionNode, _, opcode: int):
    assert_args(line.arguments, RelocatableExpressionNode)
    return [BytesSegment(bytearray([opcode]), line.location),
            ExpressionSegment(line.arguments[0], line.location)]


def unary_imm(line: InstructionNode, _, opcode: int):
    assert_args(line.arguments, RegisterNode, RelocatableExpressionNode)
    data = pack('u6u2', opcode // 4, line.arguments[0].number)
    return [BytesSegment(bytearray(data), line.location),
            ExpressionSegment(line.arguments[1], line.location)]


@dataclass
class Handler:
    handler: Callable[[InstructionNode, dict, int], list[ICodeSegment]]
    instructions: dict[str, int]


handlers: list[Handler]
handlers = [
    Handler(ds, {'ds': -1}),
    Handler(dc, {'dc': -1}),
    Handler(align, {'align': -1}),
    Handler(save, {'save': -1}),
    Handler(restore, {'restore': -1}),
    Handler(zero, {
        'pushall': 0xCE,
        'popall': 0xCF,
        'rts': 0xD7,
        'halt': 0xD4,
        'wait': 0xD5,
        'ioi': 0xD8,
        'rti': 0xD9,
        'crc': 0xDA
    }),
    Handler(unary, {
        'not': 0x80,
        'neg': 0x84,
        'dec': 0x88,
        'inc': 0x8C,
        'shr': 0x90,
        'shla': 0x94,
        'shra': 0x98,
        'rol': 0x9C,
        'push': 0xC0,
        'pop': 0xC4
    }),
    Handler(binary, {
        'move': 0x00,
        'add': 0x10,
        'addc': 0x20,
        'sub': 0x30,
        'and': 0x40,
        'or': 0x50,
        'xor': 0x60,
        'cmp': 0x70,
        'st': 0xA0,
        'ld': 0xB0,
        'ldc': 0xF0
    }),
    Handler(imm, {
        'jsr': 0xD6,
        'osix': 0xDB,
        'addsp': 0xCC,
        'setsp': 0xCD
    }),
    Handler(unary_imm, {
        'ldsa': 0xC8,
        'ldi': 0xD0
    })
]


def assembly_directives():
    return {'ds', 'dc'}
