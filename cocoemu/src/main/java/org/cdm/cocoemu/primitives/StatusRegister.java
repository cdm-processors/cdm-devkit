package org.cdm.cocoemu.primitives;

public class StatusRegister extends Register {

    private static final int MAX_FLAGS = 0xF;
    private static final int CARRY_BIT_POS = 3;

    private final int interruptBitPos;

    public StatusRegister(String name, int bits, int interruptBitPos) {
        super(name, bits);
        this.interruptBitPos = interruptBitPos;
    }

    public int getFlags() {
        return value & MAX_FLAGS;
    }

    public boolean getInterruptStatus() {
        return (value & (1 << interruptBitPos)) != 0;
    }

    public boolean getCarry() {
        return (value & (1 << CARRY_BIT_POS)) != 0;
    }

    public void setFlags(int value) {
        this.value &= maxValue & (~MAX_FLAGS);
        this.value |= value & MAX_FLAGS;
    }

    public void setInterrupt() {
        value |= (1 << interruptBitPos);
    }

    public void clearInterrupt() {
        value &= ~(1 << interruptBitPos);
    }
}
