package org.cdm.logisim.debugger.adapters;

import com.cburch.logisim.circuit.Circuit;
import com.cburch.logisim.circuit.CircuitState;
import com.cburch.logisim.circuit.SubcircuitFactory;
import com.cburch.logisim.comp.Component;
import com.cburch.logisim.data.Value;
import com.cburch.logisim.instance.InstanceState;
import org.cdm.logisim.debugger.DebuggerComponent;

import java.util.Arrays;
import java.util.List;
import java.util.stream.Collectors;

import static org.cdm.logisim.debugger.logisim.TunnelAdapter.getTunnelValue;

public class Cdm8eCircuitAdapter implements ProcessorAdapter {
    private Component processorComponent = null;

    @Override
    public String getDisplayName() {
        return "CdM-8e (Circuit)";
    }

    @Override
    public int getMemorySize() {
        return 256;
    }

    @Override
    public List<String> getRegisterNames() {
        return Arrays.asList("r0", "r1", "r2", "r3", "pc", "sp", "ps");
    }

    @Override
    public List<Integer> getRegisterSizes() {
        return Arrays.asList(8, 8, 8, 8, 16, 8, 8);
    }

    @Override
    public boolean supportsExceptions() {
        return false;
    }

    @Override
    public Component locateComponent(Circuit circuit) {
        return circuit
                .getNonWires()
                .stream()
                .filter(x -> x.getFactory() instanceof SubcircuitFactory && x.getFactory().getName().equals("CdM_8_mark5"))
                .findAny()
                .orElse(null);
    }

    @Override
    public ProcessorState getState(CircuitState circuitState) {
        Circuit currentCircuit = DebuggerComponent.getDebuggerCircuit();

        if (processorComponent == null) {
            processorComponent = locateComponent(currentCircuit);
        }

        if (processorComponent == null) {
            return null;
        }

        InstanceState processorState = circuitState.getInstanceState(processorComponent);

        List<Integer> registerPinNumbers = Arrays.asList(
                PinNumbers.R0, PinNumbers.R1, PinNumbers.R2, PinNumbers.R3,
                PinNumbers.PC, PinNumbers.SP, PinNumbers.PS
        );

        List<Integer> registerValues = registerPinNumbers.stream()
                .map(processorState::getPort)
                .map(Value::toIntValue)
                .collect(Collectors.toList());

        Circuit processorSubcircuit =
                ((SubcircuitFactory) processorComponent.getFactory()).getSubcircuit();

        CircuitState processorSubcircuitState =
                processorSubcircuit.getSubcircuitFactory().getSubstate(circuitState, processorComponent);

        Integer fetchTunnel =
                getTunnelValue("fetch", processorSubcircuit, processorSubcircuitState);

        Integer stopTunnel =
                getTunnelValue("stop", processorSubcircuit, processorSubcircuitState);

        if (fetchTunnel == null || stopTunnel == null) {
            return null;
        }

        return new ProcessorState() {
            @Override
            public boolean isFetching() {
                return fetchTunnel == 1;
            }

            @Override
            public boolean isHalted() {
                return stopTunnel == 1;
            }

            @Override
            public int getProgramCounter() {
                return registerValues.get(4);
            }

            @Override
            public List<Integer> getRegisters() {
                return registerValues;
            }
        };
    }

    private static class PinNumbers {
        private static final int R0 = 3;
        private static final int R1 = 4;
        private static final int R2 = 6;
        private static final int R3 = 7;
        private static final int PC = 9;
        private static final int SP = 10;
        private static final int PS = 11;
    }

}
