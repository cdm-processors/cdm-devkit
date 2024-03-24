from ...ast_nodes import InstructionNode, LabelNode, RelocatableExpressionNode
from ...exceptions import AssemblerException, AssemblerExceptionTag, CdmTempException
from .. import ICodeSegment
from ..cdm16.target_instructions import (
    Handler,
    align,
    alu2,
    alu3,
    alu3_ind,
    branch,
    dc,
    ds,
    handle_frame_pointer,
    imm6,
    imm6_word,
    ldi,
    mem,
    op0,
    op1,
    op2,
    restore,
    save,
    shifts,
    special,
)


def assemble_instruction(line: InstructionNode, temp_storage: dict) -> list[ICodeSegment]:
    handle_frame_pointer(line)
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


handlers: list[Handler]

handlers = [
    Handler(ds, {'ds': -1}),
    Handler(dc, {'dc': -1, 'db': -1, 'dw': -1}),
    Handler(align, {'align': -1}),
    Handler(save, {'save': -1}),
    Handler(restore, {'restore': -1}),
    Handler(ldi, {'ldi': -1}),
    Handler(op0, {'halt': 4, 'wait': 5, 'ei': 6, 'di': 7, 'rti': 9, 'pupc': 10, 'popc': 11, 'pusp': 12, 'posp': 13,
                  'pups': 14, 'pops': 15}),
    Handler(shifts, {'shl': 0, 'shr': 1, 'shra': 2, 'rol': 3, 'ror': 4, 'rcl': 5, 'rcr': 6}),
    Handler(op1, {'pop': 1, 'jsrr': 3, 'ldsp': 4, 'stsp': 5, 'ldps': 6, 'stps': 7, 'ldpc': 8, 'stpc': 9, 'ldssp': 14,
                  'stssp': 15}),
    Handler(op2, {'move': 0, 'swpw': 2, 'swpb': 3}),
    Handler(alu3_ind, {'bit': 0}),
    Handler(mem, {'ldw': 0, 'ldb': 1, 'ldsb': 2, 'lcw': 3, 'lcb': 4, 'lcsb': 5, 'stw': 6, 'stb': 7}),
    Handler(alu2, {'neg': 0, 'not': 1, 'sxt': 2, 'scl': 3}),
    Handler(imm6, {'lsb': 1, 'lssb': 2, 'ssb': 4}),
    Handler(imm6_word, {'lsw': 0, 'ssw': 3}),
    Handler(alu3, {'and': 0, 'or': 1, 'xor': 2, 'bic': 3, 'addc': 5, 'subc': 7}),
    Handler(special, {'add': -1, 'sub': -1, 'cmp': -1, 'int': -1, 'reset': -1, 'addsp': -1, 'jsr': -1, 'push': -1})
]


def assembly_directives():
    return {'ds', 'dc', 'db', 'dw'}
