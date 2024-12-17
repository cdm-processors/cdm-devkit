package org.cdm.cocoemu.server.adapter;

import org.cdm.debug.dto.MemoryConfiguratons;

public enum ProcessorType {
    CDM8,
    CDM8E,
    CDM16,
    CDM16E;

    @Override
    public String toString() {
        return Factory.getDebugEnvironment(this, MemoryConfiguratons.VON_NEUMANN).getProcessorAdapter().getDisplayName();
    }
}
