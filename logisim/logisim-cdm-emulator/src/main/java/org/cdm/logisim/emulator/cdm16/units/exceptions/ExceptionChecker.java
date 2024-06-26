package org.cdm.logisim.emulator.cdm16.units.exceptions;

import org.cdm.logisim.emulator.cdm16.Cdm16Processor;

import static org.cdm.logisim.emulator.cdm16.Arithmetic.toBoolean;

public class ExceptionChecker {
    public static ExceptionCheckerOutputParameters compute(ExceptionCheckerInputParameters parameters) {
        boolean oddDataBusValue = toBoolean(parameters.dataBusValue() & 1);

        return new ExceptionCheckerOutputParameters(
                oddDataBusValue && Cdm16Processor.MicrocodeSignals.check(
                        parameters.microcommand(),
                        Cdm16Processor.MicrocodeSignals.SP_LATCH
                ),
                oddDataBusValue && Cdm16Processor.MicrocodeSignals.check(
                        parameters.microcommand(),
                        Cdm16Processor.MicrocodeSignals.PC_LATCH
                ),
                parameters.microcommand() == 0 && !parameters.exc_latch(),
                parameters.instructionRegisterValue() == 0x8004
        );
    }
}
