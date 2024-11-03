package org.cdm.debug.runtime;

import java.util.List;

public interface ProcessorInfo {
    String getDisplayName();
    int getMemorySize();
    List<String> getRegisterNames();
    List<Integer> getRegisterSizes();
    boolean supportsExceptions();
}
