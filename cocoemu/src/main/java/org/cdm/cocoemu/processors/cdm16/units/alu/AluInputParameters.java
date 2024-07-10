package org.cdm.cocoemu.processors.cdm16.units.alu;

import lombok.Value;
import lombok.experimental.Accessors;

@Value
@Accessors(fluent = true)
public class AluInputParameters {
    int A;
    int B;
    boolean cIn;
    int alu_func;
    int alu_op_type;
    int shift_count_d;
}
