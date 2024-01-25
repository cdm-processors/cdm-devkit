from cocas.abstract_code_segments import CodeSegmentsInterface
from cocas.abstract_instructions import TargetInstructionsInterface
from cocas.ast_nodes import InstructionNode
from cocas.error import CdmException, CdmExceptionTag, CdmTempException

from ..cdm16.target_instructions import TargetInstructions as Cdm16Instructions, handle_frame_pointer


# noinspection DuplicatedCode
class TargetInstructions(Cdm16Instructions, TargetInstructionsInterface):
    @staticmethod
    def assemble_instruction(line: InstructionNode, temp_storage: dict) -> list[CodeSegmentsInterface.CodeSegment]:
        handle_frame_pointer(line)
        try:
            for h in TargetInstructions.handlers:
                if line.mnemonic in h.instructions:
                    return h.handler(line, temp_storage, h.instructions[line.mnemonic])
            if line.mnemonic.startswith('b'):
                return TargetInstructions.branch(line)
            raise CdmException(CdmExceptionTag.ASM, line.location.file, line.location.line,
                               f'Unknown instruction "{line.mnemonic}"')
        except CdmTempException as e:
            raise CdmException(CdmExceptionTag.ASM, line.location.file, line.location.line, e.message)

    @staticmethod
    def finish(*args, **kwargs):
        return Cdm16Instructions.finish(*args, **kwargs)

    @staticmethod
    def make_branch_instruction(*args, **kwargs):
        return Cdm16Instructions.make_branch_instruction(*args, **kwargs)

    class Handler(Cdm16Instructions.Handler):
        pass

    handlers: list[Handler]

    handlers = [
        Handler(Cdm16Instructions.ds, {'ds': -1}),
        Handler(Cdm16Instructions.dc, {'dc': -1, 'db': -1, 'dw': -1}),
        Handler(Cdm16Instructions.align, {'align': -1}),
        Handler(Cdm16Instructions.save, {'save': -1}),
        Handler(Cdm16Instructions.restore, {'restore': -1}),
        Handler(Cdm16Instructions.ldi, {'ldi': -1}),
        Handler(Cdm16Instructions.op0, {'halt': 4, 'wait': 5, 'ei': 6, 'di': 7, 'rti': 9, 'pupc': 10, 'popc': 11, 'pusp': 12, 'posp': 13, 'pups': 14, 'pops': 15}),
        Handler(Cdm16Instructions.shifts, {'shl': 0, 'shr': 1, 'shra': 2, 'rol': 3, 'ror': 4, 'rcl': 5, 'rcr': 6}),
        Handler(Cdm16Instructions.op1, {'pop': 1, 'jsrr': 3, 'ldsp': 4, 'stsp': 5, 'ldps': 6, 'stps': 7, 'ldpc': 8, 'stpc': 9, 'ldssp': 14, 'stssp': 15}),
        Handler(Cdm16Instructions.op2, {'move': 0, 'swpw': 2, 'swpb': 3}),
        Handler(Cdm16Instructions.alu3_ind, {'bit': 0}),
        Handler(Cdm16Instructions.mem,  {'ldw': 0, 'ldb': 1, 'ldsb': 2, 'lcw': 3, 'lcb': 4, 'lcsb': 5, 'stw': 6, 'stb': 7}),
        Handler(Cdm16Instructions.alu2, {'neg': 0, 'not': 1, 'sxt': 2, 'scl': 3}),
        Handler(Cdm16Instructions.imm6, {'lsb': 1, 'lssb': 2, 'ssb': 4}),
        Handler(Cdm16Instructions.imm6_word, {'lsw': 0, 'ssw': 3}),
        Handler(Cdm16Instructions.alu3, {'and': 0, 'or': 1, 'xor': 2, 'bic': 3, 'addc': 5, 'subc': 7}),
        Handler(Cdm16Instructions.special, {'add': -1, 'sub': -1, 'cmp': -1, 'int': -1, 'reset': -1, 'addsp': -1, 'jsr': -1, 'push': -1})
    ]

    @staticmethod
    def assembly_directives() -> set[str]:
        return super().assembly_directives()
