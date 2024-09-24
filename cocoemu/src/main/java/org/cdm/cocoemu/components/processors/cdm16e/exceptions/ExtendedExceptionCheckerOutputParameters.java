package org.cdm.cocoemu.components.processors.cdm16e.exceptions;

import lombok.Value;
import lombok.experimental.Accessors;

@Value
@Accessors(fluent = true)
public class ExtendedExceptionCheckerOutputParameters {
    boolean exc_trig_sp;
    boolean exc_trig_pc;
    boolean exc_trig_invalid_inst;
    boolean exc_privilege_violation;
    boolean double_fault;
}
