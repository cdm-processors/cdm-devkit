from cocodump.base_types import BranchInstruction, DecodedSection
from cocodump.targets.cdm8.asm import InstructionGroup, inst_decoders
from cocodump.targets.cdm8.decoder import decode_inst


def normalize_imm8(val: int):
    if val >= 0x80:
        return (-1 << 8) | val
    else:
        return val


def decode(image: bytearray, has_ivt: bool = False) -> DecodedSection:
    inst_decoders[InstructionGroup.LDI_GR].mnemonics[13] = "jmp"

    section = DecodedSection()

    section_iter = iter(image)
    current_addr = 0

    while True:
        try:
            byte = next(section_iter)

            (inst, inst_gr) = decode_inst(byte)

            if inst.inst == "jmp":
                inst = BranchInstruction(
                    "jmp",
                    []
                )

            inst.addr = current_addr
            inst.inst_bytes = [byte]

            current_addr += 1

            if inst.inst in ["jsr", "jmp"]:
                lower_byte = next(section_iter)
                higher_byte = next(section_iter)

                inst.inst_bytes.append(lower_byte)
                inst.inst_bytes.append(higher_byte)

                word = (higher_byte << 8) | lower_byte

                inst.br_addr = word
                inst.args.append(hex(word))

                current_addr += 2

            if inst_gr == InstructionGroup.BRANCHES or \
                    inst.inst in ["ldsa", "addsp", "setsp", "ldi", "osix"]:
                byte = next(section_iter)

                inst.inst_bytes.append(byte)

                current_addr += 1

                if inst_gr == InstructionGroup.BRANCHES:
                    inst: BranchInstruction

                    inst.br_addr = current_addr + normalize_imm8(byte) - 1
                    inst.args.append(str(normalize_imm8(byte)) if byte >= 0x80 else '+' + str(byte))
                else:
                    inst.args.append(hex(byte))

            section.add_inst(inst)

        except StopIteration:
            break

    return section
