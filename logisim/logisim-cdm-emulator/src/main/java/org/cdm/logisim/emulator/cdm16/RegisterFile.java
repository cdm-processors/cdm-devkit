package org.cdm.logisim.emulator.cdm16;

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
            new Register("r0"),
            new Register("r1"),
            new Register("r2"),
            new Register("r3"),
            new Register("r4"),
            new Register("r5"),
            new Register("r6"),
            new Register("r7")
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
