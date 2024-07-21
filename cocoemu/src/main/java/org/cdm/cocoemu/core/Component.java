package org.cdm.cocoemu.core;

public interface Component {
    default void clockRising() {
    }

    default void clockFalling() {
    }

    void update();
}
