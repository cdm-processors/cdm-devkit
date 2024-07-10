package org.cdm.cocoemu.cdm16;

import org.cdm.cocoemu.NamedValuePrimitive;

public class Bus extends NamedValuePrimitive {

    private static final int BUS_BITS = 16;

    private boolean isSet = false;

    private final boolean checkMultipleAssertion;

    public Bus(String name) {
        super(name, BUS_BITS);

        checkMultipleAssertion = false;
    }

    public Bus(String name, boolean checkMultipleAssertion) {
        super(name, BUS_BITS);

        this.checkMultipleAssertion = checkMultipleAssertion;
    }

    @Override
    public int getValue() {
        if (!isSet) {
            // These are tied to ground
            return 0;
        }

        return super.getValue();
    }

    @Override
    public void setValue(int value) {
        if (isSet && checkMultipleAssertion) {
            System.err.println("Multiple assertion on " + name + " new value: " + value);
        }

        super.setValue(value);
        this.isSet = true;
    }

    public boolean isSet() {
        return isSet;
    }

    @Override
    public void clear() {
        super.clear();
        isSet = false;
    }
}
