package org.cdm.logisim.emulator.cdm16e.exceptions;

import org.cdm.logisim.emulator.cdm16.Cdm16Processor.ExceptionNumbers;
import org.cdm.logisim.emulator.cdm16.units.exceptions.ExceptionControlUnitOutputParameters;
import org.cdm.logisim.emulator.cdm16e.Cdm16eProcessor.ExtendedExceptionNumbers;

import java.util.ArrayList;
import java.util.List;

public class ExtendedExceptionControlUnit {
    public static ExceptionControlUnitOutputParameters compute(ExtendedExceptionControlUnitInputParameters parameters) {
        List<Integer> triggeredExceptions = new ArrayList<>();

        if (parameters.exc_trig_sp()) {
            triggeredExceptions.add(ExceptionNumbers.UNALIGNED_SP);
        }
        if (parameters.exc_trig_pc()) {
            triggeredExceptions.add(ExceptionNumbers.UNALIGNED_PC);
        }
        if (parameters.exc_trig_invalid_inst()) {
            triggeredExceptions.add(ExceptionNumbers.INVALID_INST);
        }
        if (parameters.exc_trig_privilege_violation()) {
            triggeredExceptions.add(ExtendedExceptionNumbers.PRIVILEGE_VIOLATION);
        }
        if (parameters.exc_trig_ext()) {
            triggeredExceptions.add(ExceptionNumbers.EXTERNAL_EXC);
        }

        boolean gotException = true;

        Integer excNumber = triggeredExceptions
                .stream()
                .max(Integer::compareTo)
                .orElse(-1);

        if (excNumber == -1) {
            gotException = false;
        }

        boolean unrecoverableInstruction = parameters.rtiInstruction() || parameters.intInstruction();

        boolean internalExceptionHappened =
                parameters.exc_trig_sp()
                        || parameters.exc_trig_pc()
                        || parameters.exc_trig_invalid_inst()
                        || parameters.exc_trig_privilege_violation();

        boolean multipleInstructionsOnSamePhase =
                internalExceptionHappened && parameters.exc_trig_ext();

        boolean multipleInstructionsAcrossPhases =
                (internalExceptionHappened || parameters.exc_trig_ext()) && parameters.exc_latch();

        boolean latch_double_fault =
                unrecoverableInstruction
                        || multipleInstructionsOnSamePhase
                        || multipleInstructionsAcrossPhases;

        int exc_internal_vec_reg_output;

        if (latch_double_fault) {
            exc_internal_vec_reg_output = ExceptionNumbers.DOUBLE_FAULT;
        } else {
            exc_internal_vec_reg_output = excNumber;
        }

        boolean exc_internal_vec_reg_en = gotException;

        boolean exc_triggered = gotException || parameters.exc_latch();

        boolean exc_latch_output = gotException;

        boolean critical_fault = gotException && parameters.double_fault();

        boolean interruptGranted = parameters.int_en() && parameters.irq();

        boolean int_ack = interruptGranted && parameters.fetch();

        boolean latch_int = interruptGranted || exc_triggered;

        boolean reset_exc = exc_triggered && parameters.fetch();

        return new ExceptionControlUnitOutputParameters(
                exc_internal_vec_reg_output,
                exc_internal_vec_reg_en,
                exc_triggered,
                critical_fault,
                exc_latch_output,
                int_ack,
                latch_int,
                reset_exc,
                latch_double_fault
        );
    }
}
