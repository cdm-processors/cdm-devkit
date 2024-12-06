package org.cdm.cocoemu.server.debug;

import org.cdm.cocoemu.server.adapter.ProcessorAdapter;
import org.cdm.cocoemu.server.emulator.CdMEmulator;

public class DebugEnvironment<T> {
    ProcessorAdapter<T> processorAdapter;
    CdMEmulator<T> emulator;
    protected DebugEnvironment(ProcessorAdapter<T> processorAdapter, CdMEmulator<T> emulator) {
        this.processorAdapter = processorAdapter;
        this.emulator = emulator;
    }
}
