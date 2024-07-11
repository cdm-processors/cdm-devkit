package org.cdm.cocoemu.primitives;

import org.cdm.cocoemu.processors.cdm16.Cdm16;

public class Bus extends IntegerNamedValue {
    private boolean isSet = false;

    private final boolean checkMultipleAssertion;

    public Bus(String name, int bits) {
        super(name, bits);

        checkMultipleAssertion = false;
    }

    public Bus(String name, int bits, boolean checkMultipleAssertion) {
        super(name, bits);

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
