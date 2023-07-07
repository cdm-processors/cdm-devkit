from cocodump.base_types import BranchInstruction, DecodedSection, Instruction
from cocodump.targets.cdm8.asm import InstructionGroup, inst_decoders, registers


def decode_inst(instruction: int) -> tuple[Instruction, InstructionGroup | int]:
    high_nibble = (instruction >> 4) & 0b1111
    low_nibble = instruction & 0b1111

    rd = instruction & 0b11
    rs = (instruction >> 2) & 0b11

    decoded_inst: Instruction | None = None

    if instruction < 0x80:
        return (
            Instruction(
                inst_decoders[InstructionGroup.DIRECT].get_instruction(high_nibble),
                [
                    registers[rs],
                    registers[rd]
                ]
            ),
            InstructionGroup.DIRECT
        )

    match high_nibble:
        case InstructionGroup.UNARY_ARITH | InstructionGroup.SHIFTS:
            decoded_inst = Instruction(
                inst_decoders[high_nibble].get_instruction(rs),
                [registers[rd]]
            )

        case InstructionGroup.ST:
            decoded_inst = Instruction(
                "st",
                [
                    registers[rs],
                    registers[rd]
                ]
            )

        case InstructionGroup.LD:
            decoded_inst = Instruction(
                "ld",
                [
                    registers[rs],
                    registers[rd]
                ]
            )

        case InstructionGroup.PUSH_GR:
            if rs == 3:
                decoded_inst = Instruction(
                    inst_decoders[InstructionGroup.SP_GROUP].get_instruction(rd),
                    []
                )
            else:
                decoded_inst = Instruction(
                    inst_decoders[high_nibble].get_instruction(rs),
                    [registers[rd]]
                )

        case InstructionGroup.LDI_GR:
            if rs == 0:
                decoded_inst = Instruction(
                    "ldi",
                    [registers[rd]]
                )
            else:
                inst = inst_decoders[high_nibble].get_instruction(low_nibble)

                if inst == "jsr":
                    decoded_inst = BranchInstruction(
                        inst,
                        []
                    )
                else:
                    decoded_inst = Instruction(
                        inst,
                        []
                    )

        case InstructionGroup.BRANCHES:
            decoded_inst = BranchInstruction(
                inst_decoders[high_nibble].get_instruction(low_nibble),
                []
            )

        case InstructionGroup.LDC:
            decoded_inst = Instruction(
                "ldc",
                [
                    registers[rs],
                    registers[rd]
                ]
            )

    return decoded_inst, high_nibble


def decode(image: bytearray, has_ivt: bool = False) -> DecodedSection:
    section = DecodedSection()

    section_iter = iter(image)
    current_addr = 0

    while True:
        try:
            byte = next(section_iter)

            (inst, inst_gr) = decode_inst(byte)

            inst.addr = current_addr
            inst.inst_bytes = [byte]

            current_addr += 1

            if inst_gr == InstructionGroup.BRANCHES or \
                    inst.inst in ["ldsa", "addsp", "setsp", "ldi", "jsr", "osix"]:
                byte = next(section_iter)

                inst.inst_bytes.append(byte)

                current_addr += 1

                inst.args.append(hex(byte))

                if inst_gr == InstructionGroup.BRANCHES or \
                        inst.inst in ["jsr"]:
                    inst: BranchInstruction
                    inst.br_addr = byte

            section.add_inst(inst)

        except StopIteration:
            break

    return section
