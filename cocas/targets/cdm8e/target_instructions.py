# from cocas.asm_commands import instructions as insset, assembly_directives as dirset
from cocas.ast_nodes import *
from cocas.code_segments import *
from typing import get_origin, get_args
import bitstruct

from cocas.default_instructions import TargetInstructionsInterface
from cocas.error import CdmException, CdmExceptionTag, CdmTempException


class TargetInstructions(TargetInstructionsInterface):
    @staticmethod
    def target_instructions(line: InstructionNode) -> list[CodeSegment]:
        try:
            if line.mnemonic in TargetInstructions.assembly_directives:
                handler = assembler_directives[line.mnemonic]
                segments = handler(line.arguments)
            elif line.mnemonic in cpu_instructions:
                opcode, handler = cpu_instructions[line.mnemonic]
                segments = handler(opcode, line.arguments)
            else:
                raise CdmTempException(f'Unknown instruction "{line.mnemonic}"')
            for segment in segments:
                segment.location = line.location
            return segments
        except CdmTempException as e:
            raise CdmException(CdmExceptionTag.ASM, line.location.file, line.location.line, e.message)

    instructions = {
        'zero': {
            'pushall': 0xCE,
            'popall': 0xCF,
            'rts': 0xD7,
            'halt': 0xD4,
            'wait': 0xD5,
            'ioi': 0xD8,
            'rti': 0xD9,
            'crc': 0xDA,
        },
        'unary': {
            'not': 0x80,
            'neg': 0x84,
            'dec': 0x88,
            'inc': 0x8C,
            'shr': 0x90,
            'shla': 0x94,
            'shra': 0x98,
            'rol': 0x9C,
            'push': 0xC0,
            'pop': 0xC4,
        },
        'binary': {
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
            'ldc': 0xF0,
        },
        'branch': {
            'beq': 0xE0,
            'bz': 0xE0,
            'bnne': 0xE0,
            'bnnz': 0xE0,

            'bne': 0xE1,
            'bnz': 0xE1,
            'bneq': 0xE1,

            'bhs': 0xE2,
            'bcs': 0xE2,
            'bnlo': 0xE2,
            'bncc': 0xE2,

            'blo': 0xE3,
            'bcc': 0xE3,
            'bnhs': 0xE3,
            'bncs': 0xE3,

            'bmi': 0xE4,
            'bnpl': 0xE4,

            'bpl': 0xE5,
            'bnmi': 0xE5,

            'bvs': 0xE6,
            'bnvc': 0xE6,

            'bvc': 0xE7,
            'bnvs': 0xE7,

            'bhi': 0xE8,
            'bnlc': 0xE8,

            'bls': 0xE9,
            'bnhi': 0xE9,

            'bge': 0xEA,
            'bnlt': 0xEA,

            'blt': 0xEB,
            'bnge': 0xEB,

            'bgt': 0xEC,
            'bnle': 0xEC,

            'ble': 0xED,
            'bngt': 0xED,

            'br': 0xEE,
            'banything': 0xEE,
            'btrue': 0xEE,
            'bnfalse': 0xEE,

            'nop': 0xEF,
            'bnanything': 0xEF,
            'bntrue': 0xEF,
            'bfalse': 0xEF,
        },
        'long': {
            'jsr': 0xD6,
            'jmp': 0xDD,
        },
        'ldsa': {'ldsa': 0xC8},
        'ldi': {'ldi': 0xD0},
        'osix': {'osix': 0xDB},
        'spmove': {
            'addsp': 0xCC,
            'setsp': 0xCD,
        },
    }

    assembly_directives = {'ds', 'dc'}


def assert_args(args, *types, single_type=False):
    ts = [(t if get_origin(t) is None else get_args(t)) for t in types]
    if single_type:
        if len(ts) != 1:
            raise TypeError('Exactly one type must be specified when single_type is True')
        ts = ts * len(args)
    elif len(args) != len(ts):
        raise CdmTempException(f'Expected {len(ts)} arguments, but found {len(args)}')

    for i in range(len(args)):
        if not isinstance(args[i], ts[i]):
            raise CdmTempException(f'Incompatible argument type {type(args[i])}')


def binary_handler(opcode: int, arguments: list):
    assert_args(arguments, RegisterNode, RegisterNode)
    data = bitstruct.pack("u4u2u2", opcode // 16, arguments[0].number, arguments[1].number)
    return [BytesSegment(bytearray(data))]


def unary_handler(opcode: int, arguments: list):
    assert_args(arguments, RegisterNode)
    data = bitstruct.pack('u6u2', opcode // 4, arguments[0].number)
    return [BytesSegment(bytearray(data))]


def zero_handler(opcode: int, arguments: list):
    assert_args(arguments)
    return [BytesSegment(bytearray([opcode]))]


def branch_handler(opcode: int, arguments: list):
    assert_args(arguments, RelocatableExpressionNode)
    arg = arguments[0]

    return [BytesSegment(bytearray([opcode])), OffsetExpressionSegment(arg)]


def long_handler(opcode: int, arguments: list):
    assert_args(arguments, RelocatableExpressionNode)
    arg = arguments[0]

    return [BytesSegment(bytearray([opcode])), LongExpressionSegment(arg)]


def ldsa_handler(opcode: int, arguments: list):
    assert_args(arguments, RegisterNode, RelocatableExpressionNode)
    reg, arg = arguments
    cmd_piece = unary_handler(opcode, [reg])[0]

    return [BytesSegment(cmd_piece.data), ShortExpressionSegment(arg)]


def ldi_handler(opcode: int, arguments: list):
    # check types
    assert_args(arguments, RegisterNode, RelocatableExpressionNode | str)
    reg, arg = arguments
    cmd_piece = unary_handler(opcode, [reg])[0]

    if isinstance(arg, str):
        arg_data = bytearray(arg, 'utf8')
        if len(arg_data) != 1:
            raise CdmTempException('Argument must be a string of length 1')
        cmd_piece.data.extend(arg_data)
        return [BytesSegment(cmd_piece.data)]
    elif isinstance(arg, RelocatableExpressionNode):
        return [BytesSegment(cmd_piece.data), ShortExpressionSegment(arg)]


def osix_handler(opcode: int, arguments: list):
    assert_args(arguments, RelocatableExpressionNode)
    arg = arguments[0]

    return [BytesSegment(bytearray([opcode])), ConstExpressionSegment(arg, positive=True)]


def spmove_handler(opcode: int, arguments: list):
    assert_args(arguments, RelocatableExpressionNode)
    arg = arguments[0]

    return [BytesSegment(bytearray([opcode])), ConstExpressionSegment(arg)]


def dc_handler(arguments: list):
    assert_args(arguments, RelocatableExpressionNode | str, single_type=True)
    if len(arguments) == 0:
        raise CdmTempException('At least one argument must be provided')

    segments = []
    for arg in arguments:
        if isinstance(arg, str):
            segments.append(BytesSegment(bytearray(arg, 'utf8')))
        elif isinstance(arg, RelocatableExpressionNode):
            if arg.byte_specifier is None:
                addedLabels = list(filter(lambda t: isinstance(t, LabelNode), arg.add_terms))
                subtractedLabels = list(filter(lambda t: isinstance(t, LabelNode), arg.sub_terms))
                if len(addedLabels) == len(subtractedLabels):
                    segments.append(ShortExpressionSegment(arg))
                else:
                    segments.append(LongExpressionSegment(arg))
            else:
                segments.append(ShortExpressionSegment(arg))
    return segments


def ds_handler(arguments: list):
    assert_args(arguments, RelocatableExpressionNode)
    arg = arguments[0]

    if len(arg.add_terms) != 0 or len(arg.sub_terms) != 0:
        raise CdmTempException('Number expected')
    if arg.const_term < 0:
        raise CdmTempException('Cannot specify negative size in "ds"')
    return [BytesSegment(bytearray(arg.const_term))]


command_handlers = {
    'zero': zero_handler,
    'unary': unary_handler,
    'binary': binary_handler,
    'branch': branch_handler,
    'long': long_handler,
    'ldsa': ldsa_handler,
    'ldi': ldi_handler,
    'osix': osix_handler,
    'spmove': spmove_handler,

    'dc': dc_handler,
    'ds': ds_handler,
}

cpu_instructions = {}
for category, instructions in TargetInstructions.instructions.items():
    for mnemonic, opcode in instructions.items():
        cpu_instructions[mnemonic] = (opcode, command_handlers[category])

assembler_directives = {}
for directive in TargetInstructions.assembly_directives:
    assembler_directives[directive] = command_handlers[directive]
