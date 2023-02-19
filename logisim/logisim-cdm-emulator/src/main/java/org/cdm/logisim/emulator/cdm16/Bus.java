package org.cdm.logisim.emulator.cdm16;

import org.cdm.logisim.emulator.NamedValuePrimitive;

public class Bus extends NamedValuePrimitive {

    private boolean isSet = false;

    public Bus(String name, int bits) {
        super(name, bits);
    }

    @Override
    public void setValue(int value) {

        if (isSet) {
            System.err.println("Multiple assertion on " + name);
        }

        this.value = value;
        this.isSet = true;
    }
}
