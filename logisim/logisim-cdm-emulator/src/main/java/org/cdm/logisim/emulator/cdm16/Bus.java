package org.cdm.logisim.emulator.cdm16;

import org.cdm.logisim.emulator.NamedValuePrimitive;

public class Bus extends NamedValuePrimitive {

    private static final int BUS_BITS = 16;

    private boolean isSet = false;

    public Bus(String name) {
        super(name, BUS_BITS);
    }

    @Override
    public void setValue(int value) {

        if (isSet) {
            System.err.println("Multiple assertion on " + name + " new value: " + value);
        }

        this.value = value;
        this.isSet = true;
    }

    @Override
    public void clear() {
        super.clear();
        isSet = false;
    }
}
