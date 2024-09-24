package org.cdm.cocoemu.components.processors.cdm16.units.exceptions;

import lombok.Value;
import lombok.experimental.Accessors;

@Value
@Accessors(fluent = true)
public class ExceptionCheckerInputParameters {
    int microcommand;
    int dataBusValue;
    int instructionRegisterValue;
    boolean exc_latch;
}
