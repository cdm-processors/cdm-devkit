package org.cdm.logisim.emulator.cdm16;

public class NamedValuePrimitive {

    protected int value = 0;

    protected final String name;

    protected final int maxValue;

    public NamedValuePrimitive(String name, int bits) {
        this.name = name;
        this.maxValue = ~((-1) << bits);

        System.out.println(maxValue);
    }

    public String getName() {
        return name;
    }

    public int getValue() {
        return value;
    }

    public void setValue(int value) {
        this.value = value & maxValue;
    }
}
