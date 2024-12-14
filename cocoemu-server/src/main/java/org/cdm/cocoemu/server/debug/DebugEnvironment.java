package org.cdm.cocoemu.server.debug;

import lombok.Getter;
import org.cdm.cocoemu.core.Component;
import org.cdm.cocoemu.server.adapter.ProcessorAdapter;

@Getter
public class DebugEnvironment<T> {
    private final ProcessorAdapter<T> processorAdapter;
    private final Component processor;
    protected DebugEnvironment(ProcessorAdapter<T> processorAdapter, Component processor) {
        this.processorAdapter = processorAdapter;
        this.processor = processor;
    }
}
