package org.cdm.cocoemu.cdm16.units.decoder;

import lombok.Value;
import lombok.experimental.Accessors;

@Value
@Accessors(fluent = true)
public class InstructionDecoderOutputParameters {
    int microcodeAddress;
    int shift_count_d;

    int rs0;
    int rs1;
    int rd;

    int alu_op_type;

    boolean br_rel_nop;

    boolean arith_carry;

    int alu_func;

    int imm_type;
    int imm_d;

    boolean intInstruction;
    boolean jsrInstruction;
    boolean rtiInstruction;
    boolean haltInstruction;
    boolean waitInstruction;
    boolean eiInstruction;
    boolean diInstruction;
}
