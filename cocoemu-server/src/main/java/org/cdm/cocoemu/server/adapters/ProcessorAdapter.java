package org.cdm.cocoemu.server.adapters;

import org.cdm.debug.runtime.ProcessorInfo;
import org.cdm.debug.runtime.ProcessorState;

public interface ProcessorAdapter {
    ProcessorInfo getProcessorInfo();

    ProcessorState getProcessorState();
}
