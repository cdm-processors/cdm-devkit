package org.cdm.cocoemu.server.app;

import org.cdm.debug.runtime.ProcessorInfo;

import java.util.Arrays;
import java.util.List;

public class Cdm16ServerAdapter implements ProcessorInfo {
    @Override
    public String getDisplayName() {
        return "CdM-16";
    }

    @Override
    public int getMemorySize() {
        return 65536;
    }

    @Override
    public List<String> getRegisterNames() {
        return Arrays.asList("r0", "r1", "r2", "r3", "r4", "r5", "r6", "fp", "pc", "sp", "ps");
    }

    @Override
    public List<Integer> getRegisterSizes() {
        return Arrays.asList(16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16);
    }

    @Override
    public boolean supportsExceptions() {
        return true;
    }
}
