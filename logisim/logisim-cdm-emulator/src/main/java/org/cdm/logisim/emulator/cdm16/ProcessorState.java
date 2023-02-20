package org.cdm.logisim.emulator.cdm16;

public class ProcessorState {

    private static final int R0 = 0;
    private static final int R1 = 1;
    private static final int R2 = 2;
    private static final int R3 = 3;
    private static final int R4 = 4;
    private static final int R5 = 5;
    private static final int R6 = 6;
    private static final int R7 = 7;
    private static final int FP = 7;

    public final Register[] registers = new Register[]{
            new Register("r0"),
            new Register("r1"),
            new Register("r2"),
            new Register("r3"),
            new Register("r4"),
            new Register("r5"),
            new Register("r6"),
            new Register("r7")
    };

    public Register fp = registers[FP];

    public RegisterCounter pc = new RegisterCounter("pc");
    public RegisterCounter sp = new RegisterCounter("sp");
    public StatusRegister ps = new StatusRegister();
}
