package org.cdm.cocoemu.server.emulator;

public interface CdmEmulator<T> {
    T getSystem();

    boolean isRunning();

    void shutdown();

    void setShouldRun(boolean shouldRun);

    void doFullCycle();

    void reset();

    void update();
}
