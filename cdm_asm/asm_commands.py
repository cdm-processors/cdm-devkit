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
