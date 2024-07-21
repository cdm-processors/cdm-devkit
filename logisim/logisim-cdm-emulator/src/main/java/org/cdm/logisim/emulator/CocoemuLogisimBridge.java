package org.cdm.logisim.emulator;

import com.cburch.logisim.data.Value;

public class CocoemuLogisimBridge {
    protected static final int DELAY = 1;

    public static boolean valueToBoolean(Value value) {
        return value == Value.TRUE;
    }

    public static Value booleanToValue(boolean value) {
        return value ? Value.TRUE : Value.FALSE;
    }
}
