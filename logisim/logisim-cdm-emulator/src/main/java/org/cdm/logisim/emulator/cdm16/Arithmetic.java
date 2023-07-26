package org.cdm.logisim.emulator.cdm16;

import com.cburch.logisim.data.Value;

public class Arithmetic {

    public static final int MAX_INT = 0xFFFF;

    public static int signExtend(int value) {
        if ((value & 0xFF) >= 0x80) {
            return value | 0xFF00;
        } else {
            return value & 0xFF;
        }
    }

    public static boolean testBit(int value, int bitPosition) {
        return toBoolean((value >> bitPosition) & 1);
    }

    public static int normalize(int value) {
        return value & MAX_INT;
    }

    public static int toInteger(boolean value) {
        return value ? 1 : 0;
    }

    public static boolean toBoolean(int value) {
        return value != 0;
    }
    public static boolean toBoolean(Value value) {
        return value == Value.TRUE;
    }
}
