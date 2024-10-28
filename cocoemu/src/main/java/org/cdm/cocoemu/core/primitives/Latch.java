package org.cdm.cocoemu.core.primitives;

import lombok.ToString;

@ToString
public class Latch {
    private boolean value;

    private final String name;

    public Latch(String name) {
        this.name = name;

        value = false;
    }

    public void setValue(boolean value) {
        this.value = value;
    }

    public boolean getValue() {
        return value;
    }

    public String getName() {
        return name;
    }

    public void set() {
        value = true;
    }

    public void reset() {
        value = false;
    }
}
