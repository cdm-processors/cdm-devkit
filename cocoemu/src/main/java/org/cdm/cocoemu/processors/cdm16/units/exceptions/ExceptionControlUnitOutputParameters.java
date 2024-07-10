package org.cdm.cocoemu.processors.cdm16.units.exceptions;

import lombok.Value;
import lombok.experimental.Accessors;

@Value
@Accessors(fluent = true)
public class ExceptionControlUnitOutputParameters {
    int exc_internal_vec_reg_output;
    boolean exc_internal_vec_reg_en;
    boolean exc_triggered;
    boolean critical_fault;
    boolean exc_latch_output;
    boolean int_ack;
    boolean latch_int;
    boolean reset_exc;
    boolean latch_double_fault;
}
