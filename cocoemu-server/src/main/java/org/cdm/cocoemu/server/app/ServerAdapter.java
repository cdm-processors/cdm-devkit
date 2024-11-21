package org.cdm.cocoemu.server.app;

import org.cdm.cocoemu.components.processors.cdm16.Cdm16;
import org.cdm.cocoemu.systems.HarvardSystem;
import org.cdm.debug.runtime.ProcessorInfo;

import java.util.List;

public class ServerAdapter extends Cdm16 {

    Cdm16 cdm16;

    ServerAdapter(Cdm16 cdm16) {
        this.cdm16 = cdm16;
    }

    public ProcessorInfo getProcessorInfo() {
        return new ProcessorInfo() {
            @Override
            public String getDisplayName() {
                return "Cdm-16";
            }

            @Override
            public int getMemorySize() {
                return HarvardSystem.MEMORY_SIZE;
            }

            @Override
            public List<String> getRegisterNames() {
                return ServerAdapter.super.registerFile;
            }

            @Override
            public List<Integer> getRegisterSizes() {
                return List.of();
            }

            @Override
            public boolean supportsExceptions() {
                return false;
            }
        }
    }
}
