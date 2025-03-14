package org.cdm.cocoemu.components.processors.cdm16.units.exceptions;

import lombok.Value;
import lombok.experimental.Accessors;

@Value
@Accessors(fluent = true)
public class ExceptionCheckerOutputParameters {
    boolean exc_trig_sp;
    boolean exc_trig_pc;
    boolean exc_trig_invalid_inst;
    boolean double_fault;
}
