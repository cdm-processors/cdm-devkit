package org.cdm.logisim.emulator.cdm16.units.alu;

public record AluInputParameters(
        int A,
        int B,
        boolean cIn,
        int alu_func,
        int alu_op_type,
        int shift_count_d
) {}
