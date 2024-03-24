package org.cdm.logisim.emulator.cdm16e.exceptions;

import lombok.Value;
import lombok.experimental.Accessors;

@Value
@Accessors(fluent = true)
public class ExtendedExceptionCheckerInputParameters {
    int microcommand;
    int extensionMicrocommand;
    boolean virtualInstruction;
    int dataBusValue;
    int instructionRegisterValue;
    boolean exc_latch;
    boolean processor_mode;
}
