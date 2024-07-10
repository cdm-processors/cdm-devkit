package org.cdm.cocoemu.processors.cdm16.units;

import org.cdm.cocoemu.processors.cdm16.Cdm16;

public class ImmComputationUnit {
    public static int computeImmediate(
            int imm_d,
            int microcommand,
            int imm_type,
            boolean intInstruction,
            int phase
    ) {
        int imm = imm_d;

        if (Cdm16.MicrocodeSignals.check(microcommand, Cdm16.MicrocodeSignals.IMM_EXTEND_NEGATIVE)) {
            if (imm_type == Cdm16.IMM_Type.IMM_6) {
                imm |= 0b1111111111000000;
            } else {
                imm |= 0b1111111000000000;
            }
        }

        if (intInstruction) {
            imm <<= 2;

            if (phase % 2 == 1) {
                imm |= 2;
            }
        } else {
            if (Cdm16.MicrocodeSignals.check(microcommand, Cdm16.MicrocodeSignals.IMM_SHIFT)) {
                imm <<= 1;
            }
        }

        return imm;
    }
}
