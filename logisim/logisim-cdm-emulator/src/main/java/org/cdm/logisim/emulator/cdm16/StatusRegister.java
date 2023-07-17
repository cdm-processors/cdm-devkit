package org.cdm.logisim.emulator.cdm16;

public class StatusRegister extends Register {

    private static final int MAX_FLAGS = 0xf;
    public StatusRegister(String name) {
        super(name);
    }

    public int getFlags() {
        return value & MAX_FLAGS;
    }

    public boolean getInterruptStatus() {
        return (value & (1 << 15)) != 0;
    }

    public boolean getCarry() {
        return (value & (1 << 3)) != 0;
    }

    public void setFlags(int value) {
        this.value &= maxValue & (~MAX_FLAGS);
        this.value |= value & MAX_FLAGS;
    }

    public void setInterrupt() {
        value |= (1 << 15);
    }

    public void clearInterrupt() {
        value &= ~(1 << 15);
    }
}
