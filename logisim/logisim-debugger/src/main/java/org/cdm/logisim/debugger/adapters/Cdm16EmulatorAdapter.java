package org.cdm.logisim.debugger.adapters;

import com.cburch.logisim.circuit.Circuit;
import com.cburch.logisim.circuit.CircuitState;
import com.cburch.logisim.comp.Component;
import com.cburch.logisim.data.Value;
import com.cburch.logisim.instance.InstanceData;
import com.cburch.logisim.instance.InstanceState;
import org.cdm.logisim.debugger.DebuggerComponent;

import java.lang.reflect.Method;
import java.util.Arrays;
import java.util.List;
import java.util.stream.Collectors;

public class Cdm16EmulatorAdapter implements ProcessorAdapter {

    private Component processorComponent = null;

    @Override
    public String getDisplayName() {
        return "CdM-16 (Emulator)";
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

    @Override
    public Component locateComponent(Circuit circuit) {
        return circuit
                .getNonWires()
                .stream()
                .filter(x -> x.getFactory().getName().equals("CdM-16"))
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
                PinNumbers.R4, PinNumbers.R5, PinNumbers.R6, PinNumbers.FP,
                PinNumbers.PC, PinNumbers.SP, PinNumbers.PS
        );

        List<Integer> registerValues = registerPinNumbers.stream()
                .map(processorState::getPort)
                .map(Value::toIntValue)
                .collect(Collectors.toList());

        InstanceData processorData = processorState.getData();

        boolean exceptionHappened;
        int exceptionNumber;

        try {
            Method exceptionHappenedMethod =
                    processorData.getClass().getMethod("exceptionHappened");

            exceptionHappened = (boolean) exceptionHappenedMethod.invoke(processorData);

            Method exceptionNumberMethod =
                    processorData.getClass().getMethod("exceptionNumber", InstanceState.class);

            exceptionNumber = (int) exceptionNumberMethod.invoke(processorData, processorState);
        } catch (Exception e) {
            exceptionHappened = false;
            exceptionNumber = 0;
        }

        boolean finalExceptionHappened = exceptionHappened;
        int finalExceptionNumber = exceptionNumber;

        return new ProcessorState() {
            @Override
            public boolean isFetching() {
                int processorFetch = processorState.getPort(PinNumbers.FETCH).toIntValue();
                return processorFetch == 1;
            }

            @Override
            public boolean isHalted() {
                int processorStatus = processorState.getPort(PinNumbers.STATUS).toIntValue();
                return processorStatus >= 2; // halt, fault
            }

            @Override
            public int getProgramCounter() {
                return registerValues.get(8);
            }

            @Override
            public List<Integer> getRegisters() {
                return registerValues;
            }

            @Override
            public boolean exceptionHappened() {
                return finalExceptionHappened;
            }

            @Override
            public int getExceptionNumber() {
                return finalExceptionNumber;
            }
        };
    }

    private static class PinNumbers {
        private static final int R0 = 14;
        private static final int R1 = 15;
        private static final int R2 = 16;
        private static final int R3 = 17;
        private static final int R4 = 18;
        private static final int R5 = 19;
        private static final int R6 = 20;
        private static final int FP = 21;
        private static final int PC = 22;
        private static final int SP = 23;
        private static final int PS = 24;

        private static final int FETCH = 25;
        private static final int STATUS = 13;
    }
}
