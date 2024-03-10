package org.cdm.logisim.emulator.cdm16e.exceptions;

import org.cdm.logisim.emulator.cdm16.Cdm16Processor;
import org.cdm.logisim.emulator.cdm16e.Cdm16eProcessor;

import static org.cdm.logisim.emulator.cdm16.Arithmetic.toBoolean;

public class ExtendedExceptionChecker {
    public static ExtendedExceptionCheckerOutputParameters compute(ExtendedExceptionCheckerInputParameters parameters) {
        boolean oddDataBusValue = toBoolean(parameters.dataBusValue() & 1);

        return new ExtendedExceptionCheckerOutputParameters(
                oddDataBusValue && Cdm16Processor.MicrocodeSignals.check(
                        parameters.microcommand(),
                        Cdm16Processor.MicrocodeSignals.SP_LATCH
                ),
                oddDataBusValue && Cdm16Processor.MicrocodeSignals.check(
                        parameters.microcommand(),
                        Cdm16Processor.MicrocodeSignals.PC_LATCH
                ),
                parameters.microcommand() == 0 && !parameters.exc_latch(),
                !parameters.virtualInstruction()
                        && parameters.instructionRegisterValue() != 0x8007
                        && parameters.processor_mode() && Cdm16eProcessor.ExtensionMicrocodeSignals.check(
                        parameters.extensionMicrocommand(),
                        Cdm16eProcessor.ExtensionMicrocodeSignals.PRIVILEGED
                ),
                parameters.instructionRegisterValue() == 0x8004
        );
    }
}