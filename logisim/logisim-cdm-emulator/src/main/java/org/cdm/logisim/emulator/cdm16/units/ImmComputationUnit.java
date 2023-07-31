package org.cdm.logisim.emulator.cdm16.units;

import org.cdm.logisim.emulator.cdm16.Processor;

public class ImmComputationUnit {
    public static int computeImmediate(
            int imm_d,
            int microcommand,
            int imm_type,
            boolean intInstruction,
            int phase
    ) {
        int imm = imm_d;

        if (Processor.MicrocodeSignals.check(microcommand, Processor.MicrocodeSignals.IMM_EXTEND_NEGATIVE)) {
            if (imm_type == Processor.IMM_Type.IMM_6) {
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
            if (Processor.MicrocodeSignals.check(microcommand, Processor.MicrocodeSignals.IMM_SHIFT)) {
                imm <<= 1;
            }
        }

        return imm;
    }
}
