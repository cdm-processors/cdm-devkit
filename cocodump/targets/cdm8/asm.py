from enum import IntEnum

from cocodump.base_types import InstructionDecoder


class InstructionGroup(IntEnum):
    DIRECT = 0x0
    UNARY_ARITH = 0x8
    SHIFTS = 0x9
    ST = 0xA
    LD = 0xB
    PUSH_GR = 0xC
    LDI_GR = 0xD
    BRANCHES = 0xE
    LDC = 0xF
    SP_GROUP = 0xCC


inst_decoders: dict[InstructionGroup | int, InstructionDecoder] = {
    InstructionGroup.DIRECT: InstructionDecoder({0: "move", 1: "add", 2: "addc", 3: "sub", 4: "and",
                                                 5: "or", 6: "xor", 7: "cmp"}),

    InstructionGroup.UNARY_ARITH: InstructionDecoder({0: "not", 1: "neg", 2: "dec", 3: "inc"}),

    InstructionGroup.SHIFTS: InstructionDecoder({0: "shr", 1: "shla", 2: "shra", 3: "rol"}),

    InstructionGroup.PUSH_GR: InstructionDecoder({0: "push", 1: "pop", 2: "ldsa"}),

    InstructionGroup.SP_GROUP: InstructionDecoder({0: "addsp", 1: "setsp", 2: "pushall", 3: "popall"}),

    InstructionGroup.LDI_GR: InstructionDecoder({4: "halt", 5: "wait", 6: "jsr", 7: "rts",
                                                 8: "ioi", 9: "rti", 10: "crc", 11: "osix"}),

    InstructionGroup.BRANCHES: InstructionDecoder({0: "beq", 1: "bne", 2: "bhs", 3: "blo", 4: "bmi", 5: "bpl",
                                                   6: "bvs", 7: "bvc", 8: "bhi", 9: "bls", 10: "bge", 11: "blt",
                                                   12: "bgt", 13: "ble", 14: "br", 15: "nop"})

}

registers = {
    0: "r0",
    1: "r1",
    2: "r2",
    3: "r3"
}
