package org.cdm.cocoemu.primitives;

public abstract class IntegerNamedValue {

    protected int value = 0;

    protected final String name;

    protected final int bits;
    protected final int maxValue;

    public IntegerNamedValue(String name, int bits) {
        this.name = name;
        this.bits = bits;
        this.maxValue = ~((-1) << bits);
    }

    public String getName() {
        return name;
    }

    public int getValue() {
        return value;
    }

    public void setValue(int value) {
        this.value = normalize(value);
    }

    public void clear() {
        value = 0;
    }

    protected int normalize(int value) {
        return value & maxValue;
    }

    @Override
    public String toString() {
        return String.format("%s %s: %d", getClass().getSimpleName(), name, value);
    }
}
