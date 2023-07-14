from colorama import Fore, Style

from cocodump.colorizer import colorize, colorize_argument
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

    def emit_base(self, colored: bool = False) -> str:
        label_str = "".join([f"{x}:\n" for x in self.labels])

        address_str = f"{' ' * 2}{format(self.addr, '04x')}: "

        bytes_str = f"{' '.join([format(x, '02x') for x in self.inst_bytes])}" \
                    f"{' ' * (15 - len(self.inst_bytes) * 3)}"

        if colored:
            label_str = colorize(label_str, Fore.LIGHTYELLOW_EX)
            address_str = colorize(address_str, Style.NORMAL)
            bytes_str = colorize(bytes_str, Style.DIM)

        return label_str + address_str + bytes_str

    def emit(self, colored: bool = False) -> str:
        inst_str = self.inst
        arg_str = ', '.join(self.args)

        if colored:
            inst_str = colorize(inst_str, Fore.LIGHTBLUE_EX)
            colored_args = [colorize_argument(arg) for arg in self.args]
            arg_str = ', '.join(colored_args)

        string = self.emit_base(colored) + f"{inst_str} {arg_str}"

        content_length = len(self.inst + ', '.join(self.args))
        align_length = (content_length // self.TEXT_ALIGN + 1) * self.TEXT_ALIGN

        if self.comment is not None:
            comment_str = f"{' ' * (align_length - content_length)}" \
                          f"# {self.comment}"
            if colored:
                comment_str = colorize(comment_str, Fore.GREEN)

            string += comment_str

        return string


class BranchInstruction(Instruction):
    br_addr: int
    br_label: str | None

    def __init__(self, inst: str, args: list[str], addr: int = None, br_addr: int = None) -> None:
        super().__init__(inst, args, addr)
        self.br_addr = br_addr
        self.br_label = None

    def emit(self, colored: bool = False) -> str:
        inst_str = self.inst

        if colored:
            inst_str = colorize(inst_str, Fore.LIGHTBLUE_EX)

        if self.br_label is None:
            return self.emit_base(colored) + \
                f"{inst_str} {hex(self.br_addr)}"
        else:
            content_length = len(self.inst + self.br_label)
            align_length = (content_length // self.TEXT_ALIGN + 1) * self.TEXT_ALIGN

            label_str = self.br_label
            comment_str = f"{' ' * (align_length - content_length)}" \
                          f"# {self.inst} {self.args[0]}"

            if colored:
                label_str = colorize(label_str, Fore.LIGHTYELLOW_EX)
                comment_str = colorize(comment_str, Fore.GREEN)

            return self.emit_base(colored) + f"{inst_str} {label_str}" + comment_str


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

    def emit(self, colored: bool = False) -> str:
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
