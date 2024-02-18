package org.cdm.logisim.debugger.adapters;

import com.cburch.logisim.circuit.Circuit;
import com.cburch.logisim.circuit.CircuitState;
import com.cburch.logisim.comp.Component;

import java.util.List;

public class DefaultAdapter implements ProcessorAdapter {

    @Override
    public String getDisplayName() {
        return "Default adapter";
    }

    @Override
    public int getMemorySize() {
        return 0;
    }

    @Override
    public Component locateComponent(Circuit circuit) {
        return null;
    }

    @Override
    public ProcessorState getState(CircuitState circuitState) {
        return null;
    }

    @Override
    public List<String> getRegisterNames() {
        return null;
    }

    @Override
    public List<Integer> getRegisterSizes() {
        return null;
    }

    @Override
    public boolean supportsExceptions() {
        return false;
    }
}
