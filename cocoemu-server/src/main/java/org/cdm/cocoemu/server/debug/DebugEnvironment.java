package org.cdm.cocoemu.server.debug;

import org.cdm.cocoemu.server.adapter.ProcessorAdapter;
import org.cdm.cocoemu.server.emulator.CdMEmulator;

public class DebugEnvironment<T> {
    private final ProcessorAdapter<T> processorAdapter;
    private final CdMEmulator<T> emulator;
    protected DebugEnvironment(ProcessorAdapter<T> processorAdapter, CdMEmulator<T> emulator) {
        this.processorAdapter = processorAdapter;
        this.emulator = emulator;
    }

    public ProcessorAdapter<T> getProcessorAdapter() {
        return processorAdapter;
    }

    public CdMEmulator<T> getEmulator() {
        return emulator;
    }
}
