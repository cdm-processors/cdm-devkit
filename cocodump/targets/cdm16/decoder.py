from cocodump.base_types import BranchInstruction, DecodedSection, Instruction
from cocodump.targets.cdm16.asm import InstructionGroup, inst_decoders, registers


def normalize_imm6(val: int):
    return (-1 << 6) | val


def normalize_imm9(val: int):
    return (-1 << 9) | val


def decode_inst(instruction: int) -> tuple[Instruction, InstructionGroup]:
    inst_group = (instruction >> 13) & 0b111  # higher 3 bits

    X = (instruction >> 12) & 1  # 12th bit
    Y = (instruction >> 11) & 1  # 11th bit

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

    imm6_d = (instruction >> 3) & 0b111111
    imm9_d = instruction & 0b111111111

    shift_count_d = rs1_d

    decoded_inst_group: InstructionGroup | None = None
    decoded_instruction: Instruction | None = None

    match inst_group:

        case 0b000:
            if X:
                decoded_inst_group = InstructionGroup.SHIFTS
                decoded_instruction = Instruction(
                    inst_decoders[decoded_inst_group].get_instruction(alu_op_d1),
                    [
                        registers[rs0_d],
                        registers[rd_d],
                        str(shift_count_d + 1)
                    ]
                )
            else:
                if Y:
                    decoded_inst_group = InstructionGroup.BR_ABS
                    decoded_instruction = BranchInstruction(
                        inst_decoders[decoded_inst_group].get_instruction(br_abs_flags_d),
                        []
                    )
                else:
                    decoded_inst_group = InstructionGroup.ZERO_OP
                    inst = inst_decoders[decoded_inst_group].get_instruction(op_type_d0)

                    if inst == "jsr":
                        decoded_instruction = BranchInstruction(
                            inst,
                            []
                        )
                    else:
                        decoded_instruction = Instruction(
                            inst,
                            []
                        )

        case 0b001:
            decoded_inst_group = InstructionGroup.ONE_OP
            decoded_instruction = Instruction(
                inst_decoders[decoded_inst_group].get_instruction(op_type_d1),
                [registers[rd_d]]
            )

        case 0b010:
            if X:
                if Y:
                    decoded_inst_group = InstructionGroup.ALU_2
                    decoded_instruction = Instruction(
                        inst_decoders[decoded_inst_group].get_instruction(alu_op_d0),
                        [
                            registers[rs0_d],
                            registers[rd_d]
                        ]
                    )
                else:
                    decoded_inst_group = InstructionGroup.MEM_2
                    decoded_instruction = Instruction(
                        inst_decoders[decoded_inst_group].get_instruction(op_type_d2),
                        [
                            registers[rs0_d],
                            registers[rd_d]
                        ]
                    )
            else:
                if Y:
                    decoded_inst_group = InstructionGroup.ALU_3_IND
                    decoded_instruction = Instruction(
                        inst_decoders[decoded_inst_group].get_instruction(alu_op_d0),
                        [
                            registers[rs0_d],
                            registers[rd_d]
                        ]
                    )
                else:
                    decoded_inst_group = InstructionGroup.TWO_OP
                    decoded_instruction = Instruction(
                        inst_decoders[decoded_inst_group].get_instruction(op_type_d2),
                        [
                            registers[rs0_d],
                            registers[rd_d]
                        ]
                    )

        case 0b011:
            decoded_inst_group = InstructionGroup.IMM_6
            inst = inst_decoders[decoded_inst_group].get_instruction(op_type_d3)

            mult_inst = ["lsw", "ssw"]

            imm = imm6_d if op_type_d3 % 2 == 0 else normalize_imm6(imm6_d)

            if inst in mult_inst:
                imm *= 2

            decoded_instruction = Instruction(
                inst,
                [
                    registers[rd_d],
                    str(imm)
                ]
            )

        case 0b100:
            decoded_inst_group = InstructionGroup.IMM_9
            inst = inst_decoders[decoded_inst_group].get_instruction(op_type_d3)

            mult_inst = ["addsp", "jsr"]

            imm = imm9_d

            if inst not in ["int", "reset"]:
                imm = imm9_d if op_type_d3 % 2 == 0 else normalize_imm9(imm9_d)

                if inst in mult_inst:
                    imm *= 2

            if inst == "jsr":
                decoded_instruction = BranchInstruction(
                    inst,
                    [str(imm) if imm < 0 else '+' + str(imm)]
                )
            else:
                decoded_instruction = Instruction(
                    inst,
                    [str(imm)]
                )

        case 0b101:
            if X:
                decoded_inst_group = InstructionGroup.ALU_3
                decoded_instruction = Instruction(
                    inst_decoders[decoded_inst_group].get_instruction(alu_op_d1),
                    [
                        registers[rs0_d],
                        registers[rs1_d],
                        registers[rd_d]
                    ]
                )
            else:
                decoded_inst_group = InstructionGroup.MEM_3
                decoded_instruction = Instruction(
                    inst_decoders[decoded_inst_group].get_instruction(op_type_d3),
                    [
                        registers[rs0_d],
                        registers[rs1_d],
                        registers[rd_d]
                    ]
                )

        case 0b110:
            if br_rel_flags_d == 0xF:
                decoded_inst_group = InstructionGroup.ZERO_OP

                decoded_instruction = Instruction(
                    "nop",
                    []
                )
            else:
                decoded_inst_group = InstructionGroup.BR_REL

                decoded_instruction = BranchInstruction(
                    inst_decoders[decoded_inst_group].get_instruction(br_rel_flags_d),
                    [str(normalize_imm9(imm9_d) * 2)]
                )

        case 0b111:
            if br_rel_flags_d == 0xF:
                decoded_inst_group = InstructionGroup.ZERO_OP

                decoded_instruction = Instruction(
                    "nop",
                    []
                )
            else:
                decoded_inst_group = InstructionGroup.BR_REL

                decoded_instruction = BranchInstruction(
                    inst_decoders[decoded_inst_group].get_instruction(br_rel_flags_d),
                    ['+' + str(imm9_d * 2)]
                )

    if decoded_instruction is None:
        decoded_instruction = Instruction("<invalid>", [])

    return decoded_instruction, decoded_inst_group


def decode(image: bytearray) -> DecodedSection:
    section = DecodedSection()

    image.append(0)

    section_iter = iter(image)
    current_addr = 0

    while True:
        try:
            lower_byte = next(section_iter)
            higher_byte = next(section_iter)

            word = (higher_byte << 8) | lower_byte

            (inst, inst_group) = decode_inst(word)

            if inst.inst == "<invalid>":
                inst: Instruction = Instruction("<invalid>", [])

            inst.addr = current_addr
            inst.inst_bytes = [lower_byte, higher_byte]

            current_addr += 2

            if inst_group == InstructionGroup.BR_REL or \
                    (inst_group == InstructionGroup.IMM_9 and inst.inst == "jsr"):
                inst: BranchInstruction
                inst.br_addr = current_addr + int(inst.args[0])

            if inst_group == InstructionGroup.BR_ABS or \
                    (inst_group == InstructionGroup.ONE_OP and inst.inst == "ldi") or \
                    (inst_group == InstructionGroup.ZERO_OP and inst.inst == "jsr"):
                lower_byte = next(section_iter)
                higher_byte = next(section_iter)

                inst.inst_bytes.append(lower_byte)
                inst.inst_bytes.append(higher_byte)

                word = (higher_byte << 8) | lower_byte

                inst.args.append(hex(word))

                if inst_group == InstructionGroup.BR_ABS or \
                        (inst_group == InstructionGroup.ZERO_OP and inst.inst == "jsr"):
                    inst: BranchInstruction
                    inst.br_addr = word

                current_addr += 2

            section.add_inst(inst)

        except StopIteration:
            break

    return section
