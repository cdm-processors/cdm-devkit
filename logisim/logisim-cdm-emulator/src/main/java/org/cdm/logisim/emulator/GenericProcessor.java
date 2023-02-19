package org.cdm.logisim.emulator;

public interface GenericProcessor {
    void clockRising();

    void clockFalling();

    void update();
}
