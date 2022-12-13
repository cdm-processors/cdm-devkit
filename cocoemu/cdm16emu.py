from abc import ABC as AbstractBaseClass, abstractmethod
from enum import IntEnum, auto
from typing import NamedTuple

"""class IOMode(IntEnum):
    BYTE = auto()
    WORD = auto() """

#BITS_8  = 0
#BITS_16 = 1

MOD_4  = 1 << 4
MOD_8  = 1 << 8
MOD_16 = 1 << 16

def normalize(val: int) -> int:
    return (val + MOD_16) % MOD_16

"""class Peripheral(AbstractBaseClass):
    
    start_address: int
    end_address: int

    def __init__(self, start_address: int, end_address: int = None) -> None: 
        self.start_address = start_address

        if end_address is None:
            self.end_address = start_address
        else:
            self.end_address = end_address

    def __repr__(self) -> str:
        return f'Peripheral at [{hex(self.start_address)};{hex(self.end_address)}]'

    def __str__(self) -> str:
        return f'Peripheral at [{hex(self.start_address)};{hex(self.end_address)}]'

    def update(self): ...   # ???

    @abstractmethod
    def write(self, address: int, value: int, mode: IOMode = IOMode.WORD): ...    

    @abstractmethod
    def read(self, address: int, mode: IOMode = IOMode.WORD) -> int: ...

class Memory(Peripheral):

    image: list[int]                                    ## init ???

    def __repr__(self) -> str:
        return f'Memory at [{hex(self.start_address)};{hex(self.end_address)}]'

    def __str__(self) -> str:
        return f'Memory at [{hex(self.start_address)};{hex(self.end_address)}]'

    def write(self, address: int, value: int, mode: IOMode = IOMode.WORD): ## bm address - start_addres ???
        value = normalize(value)

        match mode:
            case IOMode.WORD:
                self.image[address] = value % MOD_8
                self.image[address + 1] = normalize(value >> 8)

            case IOMode.BYTE:
                self.image[address] = value % MOD_8

    def read(self, address: int, mode: IOMode = IOMode.WORD) -> int:

        match mode:
            case IOMode.WORD:
                value = self.image[address]
                value += self.image[address + 1] << 8

            case IOMode.BYTE:
                value = self.image[address]

        return value

    def load(self, image: list[int]): 
        self.image = image.copy()

    def print_contents(self):
        print(self.image)

    @classmethod
    def from_image(cls, image: list[int], start_address: int = 0):

        m = cls(start_address, start_address + len(image))

        m.load(image)

        return m

class Terminal(Peripheral):

    def write(self, address: int, value: int, mode: IOMode = IOMode.WORD):
        print(chr(value))

    def read(self, address: int, mode: IOMode = IOMode.WORD) -> int:
        return -1

class Keyboard(Peripheral): ... """

class Bus:
    value: int
    name: str

    def __init__(self, name: str) -> None:
        self.value = None
        self.name = name

    def set(self, value: int) -> None:
        if self.value != None:
            print('multiple assertion on ' + self.name)
        self.value = normalize(value)

    def get(self) -> int:
        return self.value

    def reset(self) -> None:
        self.value = None

class Peripheral(AbstractBaseClass):

    @abstractmethod
    def update(self, read: bool, data: bool, word: bool) -> None: ...

class Memory(Peripheral):

    image: list[int]

    data_bus: Bus
    address_bus: Bus

    start_address: int
    end_address: int

    def __init__(self, address_bus: Bus, data_bus: Bus, start_address: int, end_address: int = None) -> None:
        self.start_address = start_address
        self.end_address = end_address
        self.address_bus = address_bus
        self.data_bus = data_bus


    def update(self, read: bool, data: bool, word: bool) -> None:
        address = self.address_bus.get()

        if not (self.start_address <= address <= self.end_address):
            return

        value = 0

        if read:
            if word:
                value = self.image[address]
                value += self.image[address + 1] << 8
            else:
                value = self.image[address]

            self.data_bus.set(value)
            
        else:
            value = self.data_bus.get()

            if word:
                self.image[address] = value % MOD_8
                self.image[address + 1] = normalize(value >> 8)
            else:
                self.image[address] = value % MOD_8

    def load(self, image: list[int]): 
        self.image = image.copy()

    def print_contents(self):
        print(self.image)

    @classmethod
    def from_image(cls, address_bus: Bus, data_bus: Bus, image: list[int], start_address: int = 0):

        m = cls(address_bus, data_bus, start_address, start_address + len(image))

        m.load(image)

        return m

class Display(Peripheral):

    def __init__(self, bus) -> None:
        self.bus = bus

    def update(self, read: bool, data: bool, word: bool) -> None:
        value = self.bus.get()

        if data:
            print(value)

class Register:
    
    value: int

    def __init__(self) -> None: 
        self.value = 0

    def __str__(self) -> str:
        return '0x' + format(self.value, '04x')

    def __repr__(self) -> str:
        return '0x' + format(self.value, '04x')

    def set(self, value: int) -> None:
        self.value = normalize(value)

    def get(self) -> int:
        return self.value

    def clear(self) -> None:
        self.value = 0

class RegisterCounter(Register):

    def inc(self, n: int = 1):
        self.value += n
        self.value = normalize(self.value)

    def dec(self, n: int = 1): 
        self.value -= n
        self.value = normalize(self.value)

class StatusRegister(): 

    value: int

    def __init__(self) -> None:
        self.value = 0

    def __str__(self) -> str:
        return (f'I: {format(self.value % MOD_16, "016b")[0]}'
                f' CVZN: {format(self.value % MOD_4, "04b")}')

    def __repr__(self) -> str:
       return (f'I: {format(self.value % MOD_16, "016b")[0]}'
               f' CVZN: {format(self.value % MOD_4, "04b")}')

    def set_word(self, word: int):
        self.value = normalize(word)

    def set_flags(self, flags: int):
        self.value &= 0xFFF0
        self.value |= flags % MOD_4

    def get_word(self):
        return self.value

    def get_flags(self):
        return self.value % MOD_4

class Processor:

    class ALU_InstructionGroups(IntEnum):
        ALU_3 = 1
        ALU_2 = 1 << 1
        SHIFTS = 1 << 2

    class ALU_Shifts(IntEnum):
        SHL = 0
        SHR = 1
        SHRA = 2
        ROR = 3
        ROL = 4
        RCR = 5
        RCL = 6

    class ALU_3op(IntEnum):
        AND = 0
        OR = 1
        XOR = 2
        BIC = 3
        ADD = 4
        ADC = 5
        SUB = 6
        SBC = 7

    class ALU_2op(IntEnum):
        NEG = 0
        NOT = 1
        SXT = 2
        SCL = 3

    class IMM_Type(IntEnum):
        IMM_6 = auto()
        IMM_9 = auto()

    class InstructionGroups(IntEnum):
        ZERO_OP = 0x00
        ONE_OP = 0x10
        TWO_OP = 0x20
        MEM_2 = 0x30
        IMM_6 = 0x40
        IMM_9 = 0x50
        MEM_3 = 0x60

    class Instructions(IntEnum):
        BR_ABS = 0x70
        SHIFTS = 0x71
        ALU_2 = 0x71
        ALU_3_IND = 0x72
        ALU_3 = 0x73
        BR_REL_N = 0x74
        BR_REL_P = 0x75
        BR_ABS_NOP = 0x76
        BR_REL_NOP = 0x76
        FETCH = 0x77

    class InternalSignals(IntEnum):
        ALU_ASRTD = 1
        DATA = 1 << 1
        FP_ASRT0 = 1 << 2
        IMM_ASRT1 = 1 << 3
        IMM_ASRTD = 1 << 4
        IMM_EXTEND_NEGATIVE = 1 << 5
        IMM_SHIFT = 1 << 6
        MEM = 1 << 7
        PC_ASRT0 = 1 << 8
        PC_ASRTD = 1 << 9
        PC_INC = 1 << 10
        PC_LATCH = 1 << 11
        PS_ASRTD = 1 << 12
        PS_LATCH_FLAGS = 1 << 13
        PS_LATCH_WORD = 1 << 14
        R_ASRT0 = 1 << 15
        R_ASRT1 = 1 << 16
        R_ASRTD = 1 << 17
        R_LATCH = 1 << 18
        READ = 1 << 19
        SIGN_EXTEND = 1 << 20
        SP_ASRT0 = 1 << 21
        SP_ASRTD = 1 << 22
        SP_DEC = 1 << 23
        SP_INC = 1 << 24
        SP_LATCH = 1 << 25
        WORD = 1 << 26
        CUT = 1 << 27
    
    # Registers
    gp_registers: list[Register]    # r0, r1, r2, r3, r4, r5, r6, fp

    fp: Register
    sp: RegisterCounter

    pc: RegisterCounter
    ps: StatusRegister

    ir: Register

    # Peripherals
    peripherals: list[Peripheral]

    # Microcode
    microcode: list[int] = []

    # Internal signlas
    fetch: bool

    phase: int

    br_rel_nop: bool
    
    alu_func: int
    shift_count_d: int
    alu_op_type: int

    arith_carry: bool

    imm: int
    imm_type: IMM_Type

    rd: int
    rs0: int
    rs1: int

    alu_flags: int

    # Busses

    # Internal busses
    bus0: Bus
    bus1: Bus
    busD: Bus
    busA: Bus # busA is both internal and address output

    # Data interface bus
    data_bus: Bus # data bus for communicating with devices

    busses: list[Bus]

    def __init__(self, microcode: list[int], address_bus: Bus = None, data_bus: Bus = None) -> None:

        self.microcode = microcode

        self.gp_registers = [] # Register() for _ in range(6)
        self.peripherals = []

        for _ in range(7):
            self.gp_registers.append(Register())

        self.fp = Register()
        self.gp_registers.append(self.fp)

        self.sp = RegisterCounter()

        self.pc = RegisterCounter()
        self.ps = StatusRegister()

        self.ir = Register()

        self.fetch = True

        self.phase = 0

        self.br_rel_nop = False
    
        self.alu_func = None
        self.shift_count_d = None
        self.alu_op_type = None

        self.rd = None
        self.rs0 = None
        self.rs1 = None

        self.alu_flags = None

        self.arith_carry = False

        self.imm = None
        self.imm_type = Processor.IMM_Type.IMM_9

        self.bus0 = Bus("bus0")
        self.bus1 = Bus("bus1")
        self.busD = Bus("busD")
        self.busA = address_bus if address_bus != None else Bus("busA")
        self.data_bus = data_bus if data_bus != None else Bus("busD_Interface")

        self.busses = [
            self.bus0,
            self.bus1,
            self.busD,
            self.busA,
            self.data_bus
        ]

    def __str__(self) -> str:
        return (f'Processor - '
                f'r0:{self.gp_registers[0]} '
                f'r1:{self.gp_registers[1]} '
                f'r2:{self.gp_registers[2]} '
                f'r3:{self.gp_registers[3]} '
                f'r4:{self.gp_registers[4]} '
                f'r5:{self.gp_registers[5]} '
                f'r6:{self.gp_registers[6]} '
                f'fp:{self.gp_registers[7]} '
                f'sp:{self.sp} '
                f'pc:{self.pc} '
                f'ps: {self.ps} '
        )

    def __repr__(self) -> str:
        return (f'Processor - '
                f'r0:{self.gp_registers[0]} '
                f'r1:{self.gp_registers[1]} '
                f'r2:{self.gp_registers[2]} '
                f'r3:{self.gp_registers[3]} '
                f'r4:{self.gp_registers[4]} '
                f'r5:{self.gp_registers[5]} '
                f'r6:{self.gp_registers[6]} '
                f'fp:{self.gp_registers[7]} '
                f'sp:{self.sp} '
                f'pc:{self.pc} '
                f'ps: {self.ps} '
        )

    def attach(self, p: Peripheral):
        self.peripherals.append(p)

    """def bus_write(self, address: int, value: int, mode: IOMode = IOMode.WORD):
        for i, p in enumerate(self.peripherals):
            if p.start_address <= address <= p.end_address:
                self.peripherals[i].write(address, value, mode)

    def bus_read(self, address: int, mode: IOMode = IOMode.WORD) -> int:
        for i, p in enumerate(self.peripherals):
            if p.start_address <= address <= p.end_address:
                return self.peripherals[i].read(address, mode)"""

    def step(self) -> int:

        self.reset_signals()

        for bus in self.busses:
            bus.reset()

        microcode_address = self.phase << 7

        if self.fetch:
            microcode_address += Processor.Instructions.FETCH
            self.alu_op_type = Processor.ALU_InstructionGroups.ALU_3
            self.alu_func = Processor.ALU_3op.ADC
        else:
            microcode_address += self.decode_instruction()

        self.execute_microcommand(self.microcode[microcode_address])

        #opcode = self.bus_read(self.pc.get())
        #self.pc.inc()

        #if opcode >= 0x40:
        #    return self.execute_indirect(opcode)
        #else:
        #    return self.execute_direct(opcode)

    def decode_instruction(self) -> int:

        instruction = self.ir.get()
        
        inst_group = (instruction >> 13) & 0b111 # higher 3 bits

        X = (instruction >> 12) & 1 # 12th bit
        Y = (instruction >> 11) & 1 # 11th bit

        op_type_d0 = instruction & 0b1111
        op_type_d1 = (instruction >> 3) & 0b1111
        op_type_d2 = (instruction >> 6) & 0b1111
        op_type_d3 = (instruction >> 9) & 0b1111

        br_abs_flags_d = op_type_d0
        br_rel_flags_d = op_type_d3

        rd_d = instruction & 0b111
        rs0_d = (instruction >> 3) & 0b111
        rs1_d = (instruction >> 6) & 0b111

        alu_op_d0 = rs1_d
        alu_op_d1 = (instruction >> 9) & 0b111

        microcode_address = 0

        switch_alu_func0 = False
        switch_alu_func1 = False

        imm6_d = (instruction >> 3) & 0b111111
        imm9_d = instruction & 0b111111111

        self.shift_count_d = rs1_d

        match inst_group:

            case 0b000:
                if X:
                    microcode_address = Processor.Instructions.SHIFTS
                    self.alu_op_type = Processor.ALU_InstructionGroups.SHIFTS
                    switch_alu_func0 = True
                else:
                    if Y:
                        if self.check_flags(br_abs_flags_d):
                            microcode_address = Processor.Instructions.BR_ABS
                        else:
                            microcode_address = Processor.Instructions.BR_ABS_NOP
                    else:
                        microcode_address = Processor.InstructionGroups.ZERO_OP + op_type_d0

            case 0b001:
                microcode_address = Processor.InstructionGroups.ONE_OP + op_type_d1

            case 0b010:
                if X:
                    if Y:
                        microcode_address = Processor.Instructions.ALU_2
                        self.alu_op_type = Processor.ALU_InstructionGroups.ALU_2
                        switch_alu_func1 = True
                    else:
                        microcode_address = Processor.InstructionGroups.MEM_2 + op_type_d2
                else:
                    if Y:
                        microcode_address = Processor.Instructions.ALU_3_IND
                        self.alu_op_type = Processor.ALU_InstructionGroups.ALU_3
                        self.rs1 = rd_d
                        switch_alu_func1 = True
                    else:
                        microcode_address = Processor.InstructionGroups.TWO_OP + op_type_d2

            case 0b011:
                microcode_address = Processor.InstructionGroups.IMM_6 + op_type_d3
                self.rs0 = rd_d
                self.imm_type = Processor.IMM_Type.IMM_6

            case 0b100:
                microcode_address = Processor.InstructionGroups.IMM_9 + op_type_d3

            case 0b101:
                if X:
                    microcode_address = Processor.Instructions.ALU_3
                    self.alu_op_type = Processor.ALU_InstructionGroups.ALU_3
                    switch_alu_func0 = True
                else:
                    microcode_address = Processor.InstructionGroups.MEM_3 + op_type_d3

            case 0b110:
                if self.check_flags(br_rel_flags_d):
                    microcode_address = Processor.Instructions.BR_REL_N
                else:
                    microcode_address = Processor.Instructions.BR_REL_NOP
                    self.br_rel_nop = True

            case 0b110:
                if self.check_flags(br_rel_flags_d):
                    microcode_address = Processor.Instructions.BR_REL_P
                else:
                    microcode_address = Processor.Instructions.BR_REL_NOP
                    self.br_rel_nop = True

        if self.alu_op_type == None:
            self.alu_op_type = Processor.ALU_InstructionGroups.ALU_3

        self.rd = rd_d
    
        if self.rs1 == None:
            self.rs1 = rs1_d

        if self.rs0 == None:
            self.rs0 = rs0_d

        self.arith_carry = switch_alu_func0

        if switch_alu_func0 or switch_alu_func1:
            if switch_alu_func1:
                self.alu_func = alu_op_d0
            else:
                self.alu_func = alu_op_d1
        else:
            if microcode_address & 0b1110000 == Processor.InstructionGroups.IMM_6 and \
               op_type_d3 >= 0b1110:
                self.alu_func = Processor.ALU_3op.SUB
            else:
                self.alu_func = Processor.ALU_3op.ADC

        if self.imm_type == Processor.IMM_Type.IMM_6:
            self.imm = imm6_d
        elif self.imm_type == Processor.IMM_Type.IMM_9:
            self.imm = imm9_d
        else:
            print('?')

        return microcode_address

    def execute_microcommand(self, command: int) -> None:

        # IMM config

        if command & Processor.InternalSignals.IMM_EXTEND_NEGATIVE:
            if self.imm_type == Processor.IMM_Type.IMM_6:
                self.imm |= 0b1111111111000000
            elif self.imm_type == Processor.IMM_Type.IMM_9:
                self.imm |= 0b1111111000000000
            else:
                print('?')

        if command & Processor.InternalSignals.IMM_SHIFT:
            self.imm <<= 1

        # Asserts

        if command & Processor.InternalSignals.R_ASRT0:
            self.bus0.set(self.gp_registers[self.rs0].get())
        
        if command & Processor.InternalSignals.R_ASRT1:
            self.bus1.set(self.gp_registers[self.rs1].get())

        if command & Processor.InternalSignals.R_ASRTD:
            self.busD.set(self.gp_registers[self.rd].get())

        if command & Processor.InternalSignals.FP_ASRT0:
            self.bus0.set(self.fp.get())
        
        if command & Processor.InternalSignals.IMM_ASRT1:
            self.bus1.set(self.imm)

        if command & Processor.InternalSignals.IMM_ASRTD:
            self.busD.set(self.imm)

        if command & Processor.InternalSignals.SP_ASRT0:
            self.bus0.set(self.sp.get())

        if command & Processor.InternalSignals.SP_ASRTD:
            self.busD.set(self.sp.get())

        if command & Processor.InternalSignals.PC_ASRT0:
            self.bus0.set(self.pc.get())

        if command & Processor.InternalSignals.PC_ASRTD:
            self.busD.set(self.pc.get())

        if command & Processor.InternalSignals.PS_ASRTD:
            self.busD.set(self.ps.get_word())

        # ALU

        self.alu()

        if command & Processor.InternalSignals.ALU_ASRTD:
            self.busD.set(self.busA.get())

        # Memory

        if command & Processor.InternalSignals.MEM:

            word = bool(command & Processor.InternalSignals.WORD)
            data = bool(command & Processor.InternalSignals.DATA)
            read = bool(command & Processor.InternalSignals.READ)
            sign_extend = bool(command & Processor.InternalSignals.SIGN_EXTEND)

            if read:
                self.update_peripherals(read, data, word)

                value = self.data_bus.get()

                if sign_extend:
                    value = self.sign_extend(value)
                
                self.busD.set(value)
            else:
                self.data_bus.set(self.busD.get())
                self.update_peripherals(read, data, word)

            # word
            # sign_extend
            # data
            # read

        # Latches

        if command & Processor.InternalSignals.R_LATCH:
            self.gp_registers[self.rd].set(self.busD.get())

        if command & Processor.InternalSignals.SP_LATCH:
            self.sp.set(self.busD.get())

        if command & Processor.InternalSignals.PC_LATCH:
            self.pc.set(self.busD.get())

        if command & Processor.InternalSignals.PS_LATCH_FLAGS:
            self.ps.set_flags(self.alu_flags)

        if command & Processor.InternalSignals.PS_LATCH_WORD:
            self.ps.set_word(self.busD.get())

        if self.fetch:
            self.ir.set(self.busD.get())

        if command & Processor.InternalSignals.CUT:
            self.phase = 0

            if self.fetch:
                self.fetch = False
            else:
                self.fetch = True
        else:
            self.phase += 1

        # Increments and decrements

        if command & Processor.InternalSignals.PC_INC:
            if not self.br_rel_nop:
                self.pc.inc(2)

        if command & Processor.InternalSignals.SP_INC:
            self.sp.inc(2)

        if command & Processor.InternalSignals.SP_DEC:
            self.sp.dec(2)

    def alu(self):

        if self.bus0.get() == None:
            self.bus0.set(0)

        if self.bus1.get() == None:
            self.bus1.set(0)

        cin = False
        result = 0

        C = 0
        V = 0
        Z = 0
        N = 0

        if self.arith_carry:
            (cin, *_) = self.decode_flags(self.ps.get_flags())

        match self.alu_op_type:
            case Processor.ALU_InstructionGroups.ALU_3:
                match self.alu_func:
                    case Processor.ALU_3op.AND: ...
                    case Processor.ALU_3op.OR: ...
                    case Processor.ALU_3op.XOR: ...
                    case Processor.ALU_3op.BIC: ...
                    case Processor.ALU_3op.ADD: ...
                    case Processor.ALU_3op.ADC:
                        result = self.bus0.get() + self.bus1.get() + cin
                        C = 0 #?
                        V = 0 #?
                        (Z, N) = self.check_ZN(result)
                    case Processor.ALU_3op.SUB: ...
                    case Processor.ALU_3op.SBC: ...

            case Processor.ALU_InstructionGroups.ALU_2:
                match self.alu_func:
                    case Processor.ALU_2op.NEG: ...
                    case Processor.ALU_2op.NOT: ...
                    case Processor.ALU_2op.SXT: ...
                    case Processor.ALU_2op.SCL: ...

            case Processor.ALU_InstructionGroups.SHIFTS:
                match self.alu_func:
                    case Processor.ALU_Shifts.SHL: ...
                    case Processor.ALU_Shifts.SHR: ...
                    case Processor.ALU_Shifts.SHRA: ...
                    case Processor.ALU_Shifts.ROR: ...
                    case Processor.ALU_Shifts.ROL: ...
                    case Processor.ALU_Shifts.RCR: ...
                    case Processor.ALU_Shifts.RCL: ...

        self.alu_flags = self.encode_flags(C, V, Z, N)
        self.busA.set(result)

    def reset_signals(self):
        self.br_rel_nop = False
    
        self.alu_func = None
        self.shift_count_d = None
        self.alu_op_type = None

        self.rd = None
        self.rs0 = None
        self.rs1 = None

        self.alu_flags = None

        self.arith_carry = False

        self.imm = None
        self.imm_type = Processor.IMM_Type.IMM_9

    def encode_flags(self, C: int = 0, V: int = 0, Z: int = 0, N: int = 0) -> int:
        return (C << 3) + (V << 2) + (Z << 1) + N

    def decode_flags(self, flags: int) -> tuple[int, int, int, int]:
        return (
            (self.ps.get_flags() >> 3) & 1,
            (self.ps.get_flags() >> 2) & 1,
            (self.ps.get_flags() >> 1) & 1,
            self.ps.get_flags() & 1,
        )

    def check_ZN(self, value: int) -> int:
        Z = 0
        N = 0

        value = normalize(value)

        if (value >> 15) & 1 == 1:
            N = 1

        if value == 0:
            Z = 1

        return (Z, N)

    # from cdm8emu
    def check_flags(self, flags: int) -> bool:
        cccc = flags
        reverse = cccc & 1
        ccc = cccc >> 1

        (C, V, Z, N) = self.decode_flags(self.ps.get_flags())

        match ccc:
            case 0:
                dcsn = Z
            case 1:
                dcsn = C
            case 2:
                dcsn = N
            case 3:
                dcsn = V
            case 4:
                dcsn = C & (~Z) & 1
            case 5:
                dcsn = ~(N ^ V) & 1
            case 6:
                dcsn = (~Z) & ~(N ^ V) & 1
            case 7:
                dcsn = 1

        dcsn = reverse ^ dcsn

        if dcsn != 0:
            return True
        else:
            return False

    def sign_extend(self, value: int) -> int:
        if value & 0xFF >= 0x80:
            return value | 0xff00
        else:
            return value & 0xFF

    def get_address_bus(self) -> Bus:
        return self.busA

    def get_data_bus(self) -> Bus:
        return self.data_bus

    def update_peripherals(self, read: bool, data: bool, word: bool) -> None:
        for peripheral in self.peripherals:
            peripheral.update(read, data, word)

    """
    # -> (result, C, V)
    def adder(self, a: int, b: int, cin: int = 0, bitness: int = BITS_16) -> tuple[int, int, int]:
        C = 0
        V = 0

        if bitness == BITS_8:
            old_higher_bit = (a >> 7) & 1
            result = a + b + cin
            new_higher_bit = (result >> 7) & 1

            C = (result >> 8) & 1
            V = old_higher_bit ^ new_higher_bit
            result %= MOD_8
            
            return (result, C, V)

        elif bitness == BITS_16:
            old_higher_bit = (a >> 15) & 1
            result = a + b + cin
            new_higher_bit = (result >> 15) & 1

            C = (result >> 16) & 1
            V = old_higher_bit ^ new_higher_bit
            result %= MOD_16
            
            return (result, C, V)

    # -> (result, flags)
    def alu(self, a: int, b: int = 0, function: ALUFunctions = ALUFunctions.ADD, bitness: int = BITS_16) -> tuple[int, int]:
        C = 0
        V = 0
        Z = 0
        N = 0

        result = 0

        #match function:

        (Z, N) = self.check_ZN(result, bitness)

        return (result, self.encode_flags(C, V, Z, N))"""