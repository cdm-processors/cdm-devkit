from dataclasses import dataclass


@dataclass
class InterruptVector:
    addr: int
    label: str
    desc: str


ivt_descriptions: list[InterruptVector] = [
    InterruptVector(0x00, "_start", "Startup/Reset vector"),
    InterruptVector(0x04, "_unaligned_sp", "Unaligned SP"),
    InterruptVector(0x08, "_unaligned_pc", "Unaligned PC"),
    InterruptVector(0x0C, "_invalid_instruction", "Invalid instruction"),
    InterruptVector(0x10, "_double_fault", "Double fault")
]
