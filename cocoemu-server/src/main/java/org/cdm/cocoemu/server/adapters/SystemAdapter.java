package org.cdm.cocoemu.server.adapters;

import org.cdm.cocoemu.components.memory.Memory;
import org.cdm.debug.runtime.ProcessorInfo;
import org.cdm.debug.runtime.ProcessorState;

public abstract class SystemAdapter {
    protected ProcessorAdapter processorAdapter;

    protected SystemAdapter(ProcessorAdapter processorAdapter) {
        this.processorAdapter = processorAdapter;
    }

    public ProcessorInfo getProcessorInfo() {
        return processorAdapter.getProcessorInfo();
    }

    public ProcessorState getProcessorState() {
        return processorAdapter.getProcessorState();
    }

    public abstract void resetSystem();

    public abstract Memory getRam();

    public abstract Memory getRom();
}
