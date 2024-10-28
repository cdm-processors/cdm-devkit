package org.cdm.cocoemu.components.processors.cdm16;

import lombok.ToString;
import org.cdm.cocoemu.core.primitives.Register;

@ToString
public class RegisterFile {

    public static final int R0 = 0;
    public static final int R1 = 1;
    public static final int R2 = 2;
    public static final int R3 = 3;
    public static final int R4 = 4;
    public static final int R5 = 5;
    public static final int R6 = 6;
    public static final int R7 = 7;
    public static final int FP = 7;

    private final Register[] registers = new Register[]{
            new Register("r0", Cdm16.BIT_WIDTH),
            new Register("r1", Cdm16.BIT_WIDTH),
            new Register("r2", Cdm16.BIT_WIDTH),
            new Register("r3", Cdm16.BIT_WIDTH),
            new Register("r4", Cdm16.BIT_WIDTH),
            new Register("r5", Cdm16.BIT_WIDTH),
            new Register("r6", Cdm16.BIT_WIDTH),
            new Register("r7", Cdm16.BIT_WIDTH)
    };

    public int getRegisterValue(int register) {
        return registers[register].getValue();
    }

    public void setRegisterValue(int register, int value) {
        registers[register].setValue(value);
    }

    public Register getFramePointer() {
        return registers[FP];
    }

    public int getRegisterCount() {
        return registers.length;
    }
}
