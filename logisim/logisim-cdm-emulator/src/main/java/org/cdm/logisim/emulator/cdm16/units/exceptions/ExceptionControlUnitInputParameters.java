package org.cdm.logisim.emulator.cdm16.units.exceptions;

public record ExceptionControlUnitInputParameters(
    boolean exc_trig_sp,
    boolean exc_trig_pc,
    boolean exc_trig_invalid_inst,
    boolean exc_trig_ext,
    boolean double_fault,
    boolean exc_latch,
    boolean intInstruction,
    boolean rtiInstruction,
    boolean irq,
    boolean int_en,
    boolean fetch
) {}
