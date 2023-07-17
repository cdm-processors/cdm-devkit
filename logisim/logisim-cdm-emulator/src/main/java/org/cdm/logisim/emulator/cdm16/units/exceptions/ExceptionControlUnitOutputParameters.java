package org.cdm.logisim.emulator.cdm16.units.exceptions;

public record ExceptionControlUnitOutputParameters(
        int exc_internal_vec_reg_output,
        boolean exc_internal_vec_reg_en,
        boolean exc_triggered,
        boolean critical_fault,
        boolean exc_latch_output,
        boolean int_ack,
        boolean latch_int,
        boolean reset_exc
) {}
