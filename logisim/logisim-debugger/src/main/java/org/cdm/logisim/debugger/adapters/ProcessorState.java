package org.cdm.logisim.debugger.adapters;

import java.util.List;

public interface ProcessorState {
    boolean isFetching();
    boolean isHalted();
    int getProgramCounter();
    List<Integer> getRegisters();
    default boolean exceptionHappened() {
        throw new UnsupportedOperationException();
    }
    default int getExceptionNumber() {
        throw new UnsupportedOperationException();
    }
}
