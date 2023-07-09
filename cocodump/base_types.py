from cocodump.label_generator import get_label


class Instruction:
    inst: str
    args: list[str]
    addr: int
    inst_bytes: bytearray
    labels: list[str]
    comment: str | None

    TEXT_ALIGN = 20

    def __init__(self, inst: str, args: list[str], addr: int = None, inst_bytes: bytearray = None) -> None:
        self.inst = inst
        self.args = args
        self.addr = addr
        self.inst_bytes = inst_bytes
        self.labels = []
        self.comment = None

    def has_labels(self) -> bool:
        return len(self.labels) > 0

    def get_label(self) -> str:
        return self.labels[0]

    def add_label(self, label: str) -> None:
        self.labels.append(label)

    def equals_bytes(self, other: "Instruction") -> bool:
        return self.inst_bytes == other.inst_bytes

    def emit_base(self) -> str:
        label_str = "".join([f"{x}:\n" for x in self.labels])

        return label_str + \
            f"{' ' * 2}" \
            f"{format(self.addr, '04x')}: " \
            f"{' '.join([format(x, '02x') for x in self.inst_bytes])}" \
            f"{' ' * (15 - len(self.inst_bytes) * 3)}"

    def emit(self) -> str:
        string = self.emit_base() + \
                 f"{self.inst} {', '.join(self.args)}"

        content_length = len(self.inst + ', '.join(self.args))
        align_length = (content_length // self.TEXT_ALIGN + 1) * self.TEXT_ALIGN

        if self.comment is not None:
            string += f"{' ' * (align_length - content_length)}" \
                      f"# {self.comment}"

        return string


class BranchInstruction(Instruction):
    br_addr: int
    br_label: str | None

    def __init__(self, inst: str, args: list[str], addr: int = None, br_addr: int = None) -> None:
        super().__init__(inst, args, addr)
        self.br_addr = br_addr
        self.br_label = None

    def emit(self) -> str:
        if self.br_label is None:
            return self.emit_base() + \
                f"{self.inst} {hex(self.br_addr)}"
        else:
            content_length = len(self.inst + self.br_label)
            align_length = (content_length // self.TEXT_ALIGN + 1) * self.TEXT_ALIGN

            return self.emit_base() + \
                f"{self.inst} {self.br_label}" \
                f"{' ' * (align_length - content_length)}" \
                f"# {self.inst} {self.args[0]}"


class InterruptVectorInstruction(Instruction):
    TEXT_ALIGN = 40


class FoldedInstruction(Instruction):
    size: int

    def __init__(self, inst: Instruction, size: int) -> None:
        self.size = size
        super().__init__(
            inst.inst,
            inst.args,
            inst.addr,
            inst.inst_bytes
        )

    def emit(self) -> str:
        return (' ' * 12) + "..."


class DecodedSection:
    memory: dict[int, Instruction]

    def __init__(self) -> None:
        self.memory = dict()

    def add_inst(self, inst: Instruction):
        self.memory[inst.addr] = inst

    def place_labels(self) -> None:

        for loc in self.memory.keys():
            curr_inst = self.memory[loc]

            if isinstance(curr_inst, BranchInstruction):
                br_inst = self.memory.get(curr_inst.br_addr)

                if br_inst is None:
                    continue

                if br_inst.has_labels():
                    curr_inst.br_label = br_inst.get_label()
                else:
                    new_label = get_label()
                    curr_inst.br_label = new_label
                    br_inst.add_label(new_label)

    def to_instructions(self) -> list[Instruction]:
        return [self.memory[x] for x in self.memory.keys()]


class InstructionDecoder:
    mnemonics: dict[int, str]

    def __init__(self, mnemonics: dict[int, str]) -> None:
        self.mnemonics = mnemonics

    def get_instruction(self, number: int) -> str:
        return self.mnemonics.get(number, "<invalid>")
