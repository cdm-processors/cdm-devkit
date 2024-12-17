package org.cdm.cocoemu.server.adapter;

import org.cdm.cocoemu.components.memory.Memory;
import org.cdm.cocoemu.core.Component;
import org.cdm.debug.runtime.ProcessorInfo;
import org.cdm.debug.runtime.ProcessorState;

public abstract class ProcessorAdapter<T extends Component> implements ProcessorInfo {
    protected final T system;

    public ProcessorAdapter(T system) {
        this.system = system;
    }

    public abstract ProcessorState getProcessorState();

    public abstract Memory getBankedRam();

    public abstract Memory getBankedRom();
}
