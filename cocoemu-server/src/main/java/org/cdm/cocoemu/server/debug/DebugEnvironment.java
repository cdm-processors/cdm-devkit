package org.cdm.cocoemu.server.debug;

import lombok.Getter;
import org.cdm.cocoemu.core.Component;
import org.cdm.cocoemu.server.adapters.SystemAdapter;

@Getter
public class DebugEnvironment {
    private final SystemAdapter systemAdapter;
    private final Component system;

    public DebugEnvironment(Component system, SystemAdapter systemAdapter) {
        this.systemAdapter = systemAdapter;
        this.system = system;
    }
}
