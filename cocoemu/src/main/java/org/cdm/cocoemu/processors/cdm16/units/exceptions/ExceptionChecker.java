package org.cdm.cocoemu.processors.cdm16.units.exceptions;

import org.cdm.cocoemu.processors.cdm16.Arithmetic;
import org.cdm.cocoemu.processors.cdm16.Cdm16;

public class ExceptionChecker {
    public static ExceptionCheckerOutputParameters compute(ExceptionCheckerInputParameters parameters) {
        boolean oddDataBusValue = Arithmetic.toBoolean(parameters.dataBusValue() & 1);

        return new ExceptionCheckerOutputParameters(
                oddDataBusValue && Cdm16.MicrocodeSignals.check(
                        parameters.microcommand(),
                        Cdm16.MicrocodeSignals.SP_LATCH
                ),
                oddDataBusValue && Cdm16.MicrocodeSignals.check(
                        parameters.microcommand(),
                        Cdm16.MicrocodeSignals.PC_LATCH
                ),
                parameters.microcommand() == 0 && !parameters.exc_latch(),
                parameters.instructionRegisterValue() == 0x8004
        );
    }
}
