package org.cdm.cocoemu.server.app;

import org.cdm.cocoemu.components.processors.cdm16.Cdm16;

public class EmulatorThread extends Thread {
    private final Cdm16 system;

    private boolean shouldShutdown = false;
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

        shouldShutdown = true;
    }

    public boolean isExternalTicker() {
        return externalTicker;
    }

    public void setExternalTicker(boolean externalTicker) {
        this.externalTicker = externalTicker;
    }

    public void setShouldRun(boolean shouldRun) {
        this.shouldRun = shouldRun;
    }

    public void doFullCycle() {
        system.clockRising();
        system.clockFalling();
        system.update();
    }

    @Override
    public void run() {
        while (!shouldShutdown) {
            if (shouldRun && !externalTicker) {
                doFullCycle();
            } else {
                try {
                    Thread.sleep(100);
                } catch (InterruptedException e) {
                    throw new RuntimeException(e);
                }
            }
        }
    }
}
