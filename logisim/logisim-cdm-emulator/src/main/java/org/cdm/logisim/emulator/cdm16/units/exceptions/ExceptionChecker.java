package org.cdm.logisim.emulator.cdm16.units.exceptions;

import org.cdm.logisim.emulator.cdm16.Processor;

import static org.cdm.logisim.emulator.cdm16.Arithmetic.toBoolean;

public class ExceptionChecker {
    public static ExceptionCheckerOutputParameters compute(ExceptionCheckerInputParameters parameters) {
        boolean oddDataBusValue = toBoolean(parameters.dataBusValue() & 1);

        return new ExceptionCheckerOutputParameters(
                oddDataBusValue && Processor.MicrocodeSignals.check(
                        parameters.microcommand(),
                        Processor.MicrocodeSignals.SP_LATCH
                ),
                oddDataBusValue && Processor.MicrocodeSignals.check(
                        parameters.microcommand(),
                        Processor.MicrocodeSignals.PC_LATCH
                ),
                parameters.microcommand() == 0 && !parameters.exc_latch(),
                parameters.instructionRegisterValue() == 0x8004
        );
    }
}
