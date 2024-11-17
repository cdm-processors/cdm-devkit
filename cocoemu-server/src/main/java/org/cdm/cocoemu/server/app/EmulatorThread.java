package org.cdm.cocoemu.server.app;

import org.cdm.cocoemu.components.processors.cdm16.Cdm16;

public class EmulatorThread {
    private final Cdm16 system;

    private boolean shouldRun = true;
    private boolean externalTicker = false;

    public EmulatorThread() {
        system = new Cdm16();
    }

    public Cdm16 getSystem() {
        return system;
    }

    public boolean isRunning() {
        return shouldRun || externalTicker;
    }

    public void shutdown() {
        system.reset();

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
