package org.cdm.cocoemu.cdm16.units.exceptions;

import org.cdm.cocoemu.cdm16.Cdm16;

import static org.cdm.cocoemu.cdm16.Arithmetic.toBoolean;

public class ExceptionChecker {
    public static ExceptionCheckerOutputParameters compute(ExceptionCheckerInputParameters parameters) {
        boolean oddDataBusValue = toBoolean(parameters.dataBusValue() & 1);

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
