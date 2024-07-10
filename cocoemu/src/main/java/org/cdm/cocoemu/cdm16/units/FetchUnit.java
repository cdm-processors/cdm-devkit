package org.cdm.cocoemu.cdm16.units;

import org.cdm.cocoemu.cdm16.Cdm16;

public class FetchUnit {
    public static int fetchInstruction(
            int dataBusValue,
            int int_vec,
            int exc_internal_vec,
            int exc_vec,
            int direct_exc_vec,
            boolean latch_double_fault,
            boolean exc_trig_ext,
            boolean exc_triggered,
            boolean latch_int,
            boolean startup
    ) {
        int instruction;

        if (startup) {
            instruction = 0x8200;  // reset 0
        } else {
            if (latch_int) {
                if (exc_triggered) {
                    if (exc_trig_ext) {
                        if (latch_double_fault) {
                            instruction = Cdm16.ExceptionNumbers.DOUBLE_FAULT;
                        } else {
                            instruction = direct_exc_vec;
                        }
                    } else {
                        if (exc_internal_vec == Cdm16.ExceptionNumbers.EXTERNAL_EXC) {
                            instruction = exc_vec;
                        } else {
                            instruction = exc_internal_vec;
                        }
                    }
                } else {
                    instruction = int_vec;
                }

                instruction |= 0x8000;
            } else {
                instruction = dataBusValue;
            }
        }

        return instruction;
    }
}
