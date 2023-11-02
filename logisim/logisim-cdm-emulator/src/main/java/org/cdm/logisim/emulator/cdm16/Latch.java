package org.cdm.logisim.emulator.cdm16;

public class Latch {
    private boolean value;

    public Latch() {
        value = false;
    }

    public void setValue(boolean value) {
        this.value = value;
    }

    public boolean getValue() {
        return value;
    }

    public void set() {
        value = true;
    }

    public void reset() {
        value = false;
    }
}
