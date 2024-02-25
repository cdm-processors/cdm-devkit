package org.cdm.logisim.debugger.adapters;

import com.cburch.logisim.circuit.Circuit;
import com.cburch.logisim.circuit.CircuitState;
import com.cburch.logisim.comp.Component;

import java.util.List;

public interface ProcessorAdapter {
    String getDisplayName();
    int getMemorySize();
    List<String> getRegisterNames();
    List<Integer> getRegisterSizes();
    boolean supportsExceptions();

    Component locateComponent(Circuit circuit);
    ProcessorState getState(CircuitState circuitState);
}
