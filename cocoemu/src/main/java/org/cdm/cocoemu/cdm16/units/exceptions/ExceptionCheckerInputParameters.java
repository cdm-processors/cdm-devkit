package org.cdm.cocoemu.cdm16.units.exceptions;

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
