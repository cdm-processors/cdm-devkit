package org.cdm.cocoemu.server.debug;

import org.cdm.cocoemu.server.adapter.ProcessorAdapter;
import org.cdm.cocoemu.server.emulator.CdmEmulator;

public class DebugEnvironment<T> {
    private final ProcessorAdapter<T> processorAdapter;
    private final CdmEmulator<T> emulator;
    protected DebugEnvironment(ProcessorAdapter<T> processorAdapter, CdmEmulator<T> emulator) {
        this.processorAdapter = processorAdapter;
        this.emulator = emulator;
    }

    public ProcessorAdapter<T> getProcessorAdapter() {
        return processorAdapter;
    }

    public CdmEmulator<T> getEmulator() {
        return emulator;
    }
}
