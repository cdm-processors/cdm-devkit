package org.cdm.logisim.debugger.adapters;

import com.cburch.logisim.circuit.Circuit;
import com.cburch.logisim.circuit.CircuitState;
import com.cburch.logisim.comp.Component;

import java.util.List;

public interface ProcessorAdapter {
    String getDisplayName();
    int getMemorySize();
    Component locateComponent(Circuit circuit);
    ProcessorState getState(CircuitState circuitState);
    List<String> getRegistersOrder();

    boolean supportsExceptions();
}
