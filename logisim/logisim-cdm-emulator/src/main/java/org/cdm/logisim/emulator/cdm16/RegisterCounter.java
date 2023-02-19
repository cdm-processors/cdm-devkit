package org.cdm.logisim.emulator.cdm16;

public class RegisterCounter extends Register {

    public RegisterCounter(String name) {
        super(name);
    }

    public void inc() {
        value = normalize(value + 1);
    }

    public void inc(int value) {
        this.value = normalize(this.value + value);
    }

    public void dec() {
        value = normalize(value - 1);
    }

    public void dec(int value) {
        this.value = normalize(this.value - value);
    }

}
