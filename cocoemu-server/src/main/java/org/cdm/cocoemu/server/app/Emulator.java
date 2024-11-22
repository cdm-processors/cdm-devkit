package org.cdm.cocoemu.server.app;

import org.cdm.cocoemu.components.processors.cdm16.Cdm16;
import org.cdm.cocoemu.core.image.Image;
import org.cdm.cocoemu.systems.VonNeumannSystem;

public class Emulator {
    private final VonNeumannSystem system;

    private boolean shouldRun = true;

    public Emulator() {
        system = new VonNeumannSystem(new Cdm16(), new Image());
    }

    public VonNeumannSystem getSystem() {
        return system;
    }

    public boolean isRunning() {
        return shouldRun;
    }

    public void shutdown() {
        system.cdm16.reset();

    }

    public void setShouldRun(boolean shouldRun) {
        this.shouldRun = shouldRun;
    }

    public void doFullCycle() {
        system.clockRising();
        system.clockFalling();
        system.update();
    }


}
