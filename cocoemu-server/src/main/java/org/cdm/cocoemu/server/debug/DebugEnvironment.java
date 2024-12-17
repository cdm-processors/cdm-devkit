package org.cdm.cocoemu.server.debug;

import lombok.Getter;
import org.cdm.cocoemu.core.Component;
import org.cdm.cocoemu.server.adapter.ProcessorAdapter;

@Getter
public class DebugEnvironment<T extends Component> {
    private final ProcessorAdapter<T> processorAdapter;
    private final Component system;
    protected DebugEnvironment(ProcessorAdapter<T> processorAdapter, Component system) {
        this.processorAdapter = processorAdapter;
        this.system = system;
    }
}
