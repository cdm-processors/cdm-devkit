package org.cdm.logisim.emulator;

public abstract class NamedValuePrimitive {

    protected int value = 0;

    protected final String name;

    protected final int maxValue;

    public NamedValuePrimitive(String name, int bits) {
        this.name = name;
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
}
