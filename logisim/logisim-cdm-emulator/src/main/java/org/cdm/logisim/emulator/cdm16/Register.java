package org.cdm.logisim.emulator.cdm16;

import org.cdm.logisim.emulator.NamedValuePrimitive;

public class Register extends NamedValuePrimitive {

    private static final int REGISTER_BITS = 16;

    public Register(String name) {
        super(name, REGISTER_BITS);
    }

    public Register(String name, int bits) {
        super(name, bits);
    }
}
