package org.cdm.cocoemu.cdm16.units.exceptions;

import lombok.Value;
import lombok.experimental.Accessors;

@Value
@Accessors(fluent = true)
public class ExceptionControlUnitInputParameters {
    boolean exc_trig_sp;
    boolean exc_trig_pc;
    boolean exc_trig_invalid_inst;
    boolean exc_trig_ext;
    boolean double_fault;
    boolean exc_latch;
    boolean intInstruction;
    boolean rtiInstruction;
    boolean irq;
    boolean int_en;
    boolean fetch;
}
