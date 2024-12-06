package org.cdm.cocoemu.server.emulator;

import org.cdm.cocoemu.components.processors.cdm16.Cdm16;

public class CdM16Emulator implements CdMEmulator<Cdm16> {
    private final Cdm16 system;
    private boolean shouldRun = true;

    public CdM16Emulator(Cdm16 system) {
        this.system = system;
    }

    @Override
    public Cdm16 getSystem() {
        return system;
    }

    @Override
    public boolean isRunning() {
        return shouldRun;
    }

    @Override
    public void shutdown() {
        system.reset();
    }

    @Override
    public void setShouldRun(boolean shouldRun) {
        this.shouldRun = shouldRun;
    }

    @Override
    public void doFullCycle() {
        system.clockRising();
        system.clockFalling();
        system.update();
    }

    @Override
    public void reset() {
        system.reset();
    }

    @Override
    public void update() {
        system.update();
    }

}
