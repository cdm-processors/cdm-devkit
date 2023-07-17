package org.cdm.logisim.emulator.cdm16.units.exceptions;

public record ExceptionCheckerOutputParameters(
    boolean exc_trig_sp,
    boolean exc_trig_pc,
    boolean exc_trig_invalid_inst,
    boolean double_fault
) {}
