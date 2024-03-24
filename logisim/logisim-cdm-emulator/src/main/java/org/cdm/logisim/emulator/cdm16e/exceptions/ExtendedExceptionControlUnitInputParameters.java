package org.cdm.logisim.emulator.cdm16e.exceptions;

import lombok.Value;
import lombok.experimental.Accessors;

@Value
@Accessors(fluent = true)
public class ExtendedExceptionControlUnitInputParameters {
    boolean exc_trig_sp;
    boolean exc_trig_pc;
    boolean exc_trig_invalid_inst;
    boolean exc_trig_privilege_violation;
    boolean exc_trig_ext;
    boolean double_fault;
    boolean exc_latch;
    boolean intInstruction;
    boolean rtiInstruction;
    boolean irq;
    boolean int_en;
    boolean fetch;
}
