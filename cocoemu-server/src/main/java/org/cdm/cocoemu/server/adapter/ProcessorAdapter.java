package org.cdm.cocoemu.server.adapter;

import org.cdm.debug.runtime.ProcessorInfo;
import org.cdm.debug.runtime.ProcessorState;

public abstract class ProcessorAdapter<T> implements ProcessorInfo {
    protected final T processor;
    public ProcessorAdapter(T processor) {
        this.processor = processor;
    }
    public abstract ProcessorState getProcessorState();
}
