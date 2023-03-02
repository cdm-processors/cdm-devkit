package org.cdm.logisim.emulator.cdm16;

public class StatusRegister extends Register {

    private static final int MAX_FLAGS = 0xf;
    public StatusRegister() {
        super("ps");
    }

    public int getWord() {
        return value;
    }

    public int getFlags() {
        return value & MAX_FLAGS;
    }

    public void setWord(int value) {
        this.value = normalize(value);
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
