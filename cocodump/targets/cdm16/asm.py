from enum import Enum, auto

from cocodump.base_types import InstructionDecoder


class InstructionGroup(Enum):
    ZERO_OP = auto()
    ONE_OP = auto()
    TWO_OP = auto()
    MEM_2 = auto()
    IMM_6 = auto()
    IMM_9 = auto()
    MEM_3 = auto()
    BR_ABS = auto()
    SHIFTS = auto()
    ALU_2 = auto()
    ALU_3_IND = auto()
    ALU_3 = auto()
    BR_REL = auto()


inst_decoders: dict[InstructionGroup, InstructionDecoder] = {
    InstructionGroup.ZERO_OP: InstructionDecoder({0: "zero", 1: "res", 2: "res", 3: "res", 4: "halt", 5: "wait",
                                                  6: "ei", 7: "di", 8: "jsr", 9: "rti", 10: "pupc", 11: "popc",
                                                  12: "pusp", 13: "posp", 14: "pups", 15: "pops"}),

    InstructionGroup.ONE_OP: InstructionDecoder({0: "push", 1: "pop", 2: "ldi", 3: "jsrr", 4: "ldsp", 5: "stsp",
                                                 6: "ldps", 7: "stps", 8: "ldpc", 9: "stpc", 10: "addsp"}),

    InstructionGroup.TWO_OP: InstructionDecoder({0: "move"}),

    InstructionGroup.MEM_2: InstructionDecoder({0: "ldw", 1: "ldb", 2: "ldsb", 3: "lcw", 4: "lcb", 5: "lcsb",
                                                6: "stw", 7: "stb"}),

    InstructionGroup.IMM_6: InstructionDecoder({0: "lsw", 1: "lsw", 2: "lsb", 3: "lsb", 4: "lssb", 5: "lssb",
                                                6: "ssw", 7: "ssw", 8: "ssb", 9: "ssb", 10: "ldi", 11: "ldi",
                                                12: "add", 13: "add", 14: "cmp", 15: "cmp"}),

    InstructionGroup.IMM_9: InstructionDecoder({0: "int", 1: "reset", 2: "push", 3: "push", 4: "addsp", 5: "addsp",
                                                6: "jsr", 7: "jsr"}),

    InstructionGroup.MEM_3: InstructionDecoder({0: "ldw", 1: "ldb", 2: "ldsb", 3: "lcw", 4: "lcb", 5: "lcsb",
                                                6: "stw", 7: "stb"}),

    InstructionGroup.BR_ABS: InstructionDecoder({0: "beq", 1: "bne", 2: "bhs", 3: "blo", 4: "bmi", 5: "bpl",
                                                 6: "bvs", 7: "bvc", 8: "bhi", 9: "bls", 10: "bge", 11: "blt",
                                                 12: "bgt", 13: "ble", 14: "br", 15: "nop"}),

    InstructionGroup.SHIFTS: InstructionDecoder({0: "shl", 1: "shr", 2: "shra", 3: "rol", 4: "ror", 5: "rcl",
                                                6: "rcr"}),

    InstructionGroup.ALU_2: InstructionDecoder({0: "neg", 1: "not", 2: "sxt", 3: "scl"}),

    InstructionGroup.ALU_3_IND: InstructionDecoder({0: "bit", 6: "cmp"}),

    InstructionGroup.ALU_3: InstructionDecoder({0: "and", 1: "or", 2: "xor", 3: "bic", 4: "add", 5: "addc",
                                                6: "sub", 7: "subc"}),

    InstructionGroup.BR_REL: InstructionDecoder({0: "beq", 1: "bne", 2: "bhs", 3: "blo", 4: "bmi", 5: "bpl",
                                                 6: "bvs", 7: "bvc", 8: "bhi", 9: "bls", 10: "bge", 11: "blt",
                                                 12: "bgt", 13: "ble", 14: "br", 15: "nop"})
}

registers = {
    0: "r0",
    1: "r1",
    2: "r2",
    3: "r3",
    4: "r4",
    5: "r5",
    6: "r6",
    7: "fp",
}
