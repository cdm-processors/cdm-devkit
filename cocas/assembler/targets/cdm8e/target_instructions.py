from typing import Union, get_args, get_origin

import bitstruct

from cocas.error import CdmException, CdmExceptionTag, CdmTempException

from ...ast_nodes import InstructionNode, LabelNode, RegisterNode, RelocatableExpressionNode
from .. import CodeSegmentsInterface, TargetInstructionsInterface
from .code_segments import CodeSegments
from .simple_instructions import simple_instructions


def assert_args(args, *types, single_type=False):
    ts = [(t if get_origin(t) is None else get_args(t)) for t in types]
    if single_type:
        if len(ts) != 1:
            raise TypeError('Exactly one type must be specified when single_type is True')
        ts = ts * len(args)
    elif len(args) != len(ts):
        raise CdmTempException(f'Expected {len(ts)} arguments, but found {len(args)}')

    for i in range(len(args)):
        # noinspection PyTypeHints
        if not isinstance(args[i], ts[i]):
            raise CdmTempException(f'Incompatible argument type {type(args[i])}')
        if isinstance(args[i], RegisterNode) and not 0 <= args[i].number <= 3:
            raise CdmTempException(f'Invalid register number r{args[i].number}')


class TargetInstructions(TargetInstructionsInterface):
    @staticmethod
    def assemble_instruction(line: InstructionNode, temp_storage) \
            -> list[CodeSegmentsInterface.CodeSegment]:
        try:
            if line.mnemonic in TargetInstructions.assembly_directives():
                handler = assembler_directives[line.mnemonic]
                segments = handler(line.arguments)
            elif line.mnemonic in cpu_instructions:
                opcode, handler = cpu_instructions[line.mnemonic]
                segments = handler(opcode, line.arguments)
            elif line.mnemonic in TargetInstructions.special_instructions:
                return TargetInstructions.special_instructions[line.mnemonic](line.arguments, temp_storage,
                                                                              line.location)
            else:
                raise CdmTempException(f'Unknown instruction "{line.mnemonic}"')
            for segment in segments:
                segment.location = line.location
            return segments
        except CdmTempException as e:
            raise CdmException(CdmExceptionTag.ASM, line.location.file, line.location.line, e.message)

    @staticmethod
    def finish(temp_storage: dict):
        if len(temp_storage.get("save_restore_stack", [])) != 0:
            raise CdmTempException("Expected restore statement")

    @staticmethod
    def make_branch_instruction(location, branch_mnemonic: str, label_name: str, inverse: bool) \
            -> list[CodeSegmentsInterface.CodeSegment]:
        arg2 = RelocatableExpressionNode(None, [LabelNode(label_name)], [], 0)
        if inverse:
            branch_mnemonic = 'n' + branch_mnemonic
        return [CodeSegments.GotoSegment(branch_mnemonic, arg2)]

    @staticmethod
    def goto_handler(arguments: list, _, location):
        assert_args(arguments, RelocatableExpressionNode, RelocatableExpressionNode)
        br_mnemonic: RelocatableExpressionNode
        br_mnemonic = arguments[0]
        if br_mnemonic.byte_specifier is not None or len(br_mnemonic.sub_terms) != 0 \
                or len(br_mnemonic.add_terms) != 1 or not isinstance(br_mnemonic.add_terms[0], LabelNode):
            raise CdmTempException('Branch mnemonic must be single word')
        goto = CodeSegments.GotoSegment(br_mnemonic.add_terms[0].name, arguments[1])
        goto.location = location
        return [goto]

    @staticmethod
    def save_handler(arguments: list, temp_storage: dict, _):
        assert_args(arguments, RegisterNode)
        save_restore_stack: list[RegisterNode]
        save_restore_stack = temp_storage.get("save_restore_stack", [])
        save_restore_stack.append(arguments[0])
        temp_storage["save_restore_stack"] = save_restore_stack
        return TargetInstructions.assemble_instruction(InstructionNode("push", [arguments[0]]), temp_storage)

    @staticmethod
    def restore_handler(arguments: list, temp_storage: dict, _):
        save_restore_stack: list[RegisterNode]
        save_restore_stack = temp_storage.get("save_restore_stack", [])
        if len(save_restore_stack) == 0:
            raise CdmTempException("Every restore statement must be preceded by a save statement")
        reg = save_restore_stack.pop()
        if len(arguments) > 0:
            assert_args(arguments, RegisterNode)
            reg = arguments[0]
        return TargetInstructions.assemble_instruction(InstructionNode("pop", [reg]), temp_storage)

    special_instructions = {
        'goto': goto_handler,
        'save': save_handler,
        'restore': restore_handler
    }

    simple_instructions = simple_instructions

    @staticmethod
    def assembly_directives():
        return {'ds', 'dc'}


def binary_handler(opcode: int, arguments: list):
    assert_args(arguments, RegisterNode, RegisterNode)
    data = bitstruct.pack("u4u2u2", opcode // 16, arguments[0].number, arguments[1].number)
    return [CodeSegments.BytesSegment(bytearray(data))]


def unary_handler(opcode: int, arguments: list):
    assert_args(arguments, RegisterNode)
    data = bitstruct.pack('u6u2', opcode // 4, arguments[0].number)
    return [CodeSegments.BytesSegment(bytearray(data))]


def zero_handler(opcode: int, arguments: list):
    assert_args(arguments)
    return [CodeSegments.BytesSegment(bytearray([opcode]))]


def branch_handler(opcode: int, arguments: list):
    assert_args(arguments, RelocatableExpressionNode)
    arg = arguments[0]

    return [CodeSegments.BytesSegment(bytearray([opcode])), CodeSegments.OffsetExpressionSegment(arg)]


def long_handler(opcode: int, arguments: list):
    assert_args(arguments, RelocatableExpressionNode)
    arg = arguments[0]

    return [CodeSegments.BytesSegment(bytearray([opcode])), CodeSegments.LongExpressionSegment(arg)]


def ldsa_handler(opcode: int, arguments: list):
    assert_args(arguments, RegisterNode, RelocatableExpressionNode)
    reg, arg = arguments
    cmd_piece = unary_handler(opcode, [reg])[0]

    return [CodeSegments.BytesSegment(cmd_piece.data), CodeSegments.ShortExpressionSegment(arg)]


def ldi_handler(opcode: int, arguments: list):
    # check types
    assert_args(arguments, RegisterNode, Union[RelocatableExpressionNode, str])
    reg, arg = arguments
    cmd_piece = unary_handler(opcode, [reg])[0]

    if isinstance(arg, str):
        arg_data = bytearray(arg, 'utf8')
        if len(arg_data) != 1:
            raise CdmTempException('Argument must be a string of length 1')
        cmd_piece.data.extend(arg_data)
        return [CodeSegments.BytesSegment(cmd_piece.data)]
    elif isinstance(arg, RelocatableExpressionNode):
        return [CodeSegments.BytesSegment(cmd_piece.data), CodeSegments.ShortExpressionSegment(arg)]


def osix_handler(opcode: int, arguments: list):
    assert_args(arguments, RelocatableExpressionNode)
    arg = arguments[0]

    return [CodeSegments.BytesSegment(bytearray([opcode])), CodeSegments.ConstExpressionSegment(arg, positive=True)]


def spmove_handler(opcode: int, arguments: list):
    assert_args(arguments, RelocatableExpressionNode)
    arg = arguments[0]

    return [CodeSegments.BytesSegment(bytearray([opcode])), CodeSegments.ConstExpressionSegment(arg)]


def dc_handler(arguments: list):
    assert_args(arguments, Union[RelocatableExpressionNode, str], single_type=True)
    if len(arguments) == 0:
        raise CdmTempException('At least one argument must be provided')

    segments = []
    for arg in arguments:
        if isinstance(arg, str):
            segments.append(CodeSegments.BytesSegment(bytearray(arg, 'utf8')))
        elif isinstance(arg, RelocatableExpressionNode):
            if arg.byte_specifier is None:
                added_labels = list(filter(lambda t: isinstance(t, LabelNode), arg.add_terms))
                subtracted_labels = list(filter(lambda t: isinstance(t, LabelNode), arg.sub_terms))
                if len(added_labels) == len(subtracted_labels):
                    segments.append(CodeSegments.ShortExpressionSegment(arg))
                else:
                    segments.append(CodeSegments.LongExpressionSegment(arg))
            else:
                segments.append(CodeSegments.ShortExpressionSegment(arg))
    return segments


def ds_handler(arguments: list):
    assert_args(arguments, RelocatableExpressionNode)
    arg = arguments[0]

    if len(arg.add_terms) != 0 or len(arg.sub_terms) != 0:
        raise CdmTempException('Number expected')
    if arg.const_term < 0:
        raise CdmTempException('Cannot specify negative size in "ds"')
    return [CodeSegments.BytesSegment(bytearray(arg.const_term))]


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
assembler_directives = {}


def initialize():
    for category, instructions in TargetInstructions.simple_instructions.items():
        for mnemonic, opcode in instructions.items():
            cpu_instructions[mnemonic] = (opcode, command_handlers[category])

    for directive in TargetInstructions.assembly_directives():
        assembler_directives[directive] = command_handlers[directive]


initialize()
