package org.cdm.cocoemu.core.primitives;

public class RegisterCounter extends Register implements Cloneable {

    public RegisterCounter(String name, int bits) {
        super(name, bits);
    }

    public void inc() {
        inc(1);
    }

    public void inc(int value) {
        this.value = normalize(this.value + value);
    }

    public void dec() {
        dec(1);
    }

    public void dec(int value) {
        this.value = normalize(this.value - value);
    }

    @Override
    public RegisterCounter clone() {
        try {
            return (RegisterCounter) super.clone();
        } catch (CloneNotSupportedException e) {
            throw new AssertionError();
        }
    }
}
