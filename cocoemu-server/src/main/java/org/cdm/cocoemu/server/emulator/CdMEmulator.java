package org.cdm.cocoemu.server.emulator;

public interface CdMEmulator<T> {
    T getSystem();

    boolean isRunning();

    void shutdown();

    void setShouldRun(boolean shouldRun);

    void doFullCycle();
}
