package org.cdm.cocoemu.cdm16e.exceptions;

import org.cdm.cocoemu.cdm16.Cdm16;
import org.cdm.cocoemu.cdm16e.Cdm16e;

import static org.cdm.cocoemu.cdm16.Arithmetic.toBoolean;

public class ExtendedExceptionChecker {
    public static ExtendedExceptionCheckerOutputParameters compute(ExtendedExceptionCheckerInputParameters parameters) {
        boolean oddDataBusValue = toBoolean(parameters.dataBusValue() & 1);

        return new ExtendedExceptionCheckerOutputParameters(
                oddDataBusValue && Cdm16.MicrocodeSignals.check(
                        parameters.microcommand(),
                        Cdm16.MicrocodeSignals.SP_LATCH
                ),
                oddDataBusValue && Cdm16.MicrocodeSignals.check(
                        parameters.microcommand(),
                        Cdm16.MicrocodeSignals.PC_LATCH
                ),
                parameters.microcommand() == 0 && !parameters.exc_latch(),
                !parameters.virtualInstruction()
                        && parameters.instructionRegisterValue() != 0x8007
                        && parameters.processor_mode() && Cdm16e.ExtensionMicrocodeSignals.check(
                        parameters.extensionMicrocommand(),
                        Cdm16e.ExtensionMicrocodeSignals.PRIVILEGED
                ),
                parameters.instructionRegisterValue() == 0x8004
        );
    }
}