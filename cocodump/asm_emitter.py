from cocodump.base_types import DecodedSection, FoldedInstruction, Instruction


def fold_instructions(instructions: list[Instruction], fold_threshold: int) -> list[Instruction]:
    prev_inst = Instruction("", [])
    start_idx: int | None = None
    repeated = False

    inst_acc: list[Instruction] = []
    folded_instructions: list[Instruction] = []

    instructions.append(Instruction("", []))

    for (num, inst) in enumerate(instructions):
        num: int
        inst: Instruction

        if inst.equals_bytes(prev_inst) and not repeated:
            repeated = True
            start_idx = num

        if not inst.equals_bytes(prev_inst) and repeated:
            repeated = False

            region_size = num - start_idx

            if region_size > fold_threshold:
                folded_instructions.append(FoldedInstruction(
                    prev_inst,
                    region_size
                ))

                folded_instructions.append(prev_inst)
            else:
                folded_instructions += inst_acc

            inst_acc.clear()

        if not inst.equals_bytes(prev_inst) and not repeated:
            folded_instructions.append(inst)

        if inst.equals_bytes(prev_inst) and repeated:
            inst_acc.append(inst)

        prev_inst = inst

    folded_instructions.pop()
    instructions.pop()

    return folded_instructions


def emit_asm(section: DecodedSection, fold: bool = True, fold_threshold: int = 15, colored: bool = False) -> None:
    instructions = section.to_instructions()

    if fold:
        instructions = fold_instructions(instructions, fold_threshold)

    for inst in instructions:
        print(inst.emit(colored))
