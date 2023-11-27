package org.cdm.logisim.debugger.adapters;

import com.cburch.logisim.circuit.Circuit;
import org.cdm.logisim.debugger.DebuggerComponent;

import java.util.Arrays;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class ProcessorAdapterFactory {

    private static final Map<String, List<ProcessorType>> supportedTargets = new HashMap<>();

    static {
        supportedTargets.put(
                "cdm16",
                Arrays.asList(ProcessorType.CDM16_CIRCUIT, ProcessorType.CDM16_EMU)
        );
    }

    public static ProcessorAdapter getProcessorAdapter(ProcessorType processorType) {
        switch (processorType) {
            case CDM8:
                throw new UnsupportedOperationException();
            case CDM8E:
                throw new UnsupportedOperationException();
            case CDM16_CIRCUIT:
                return new Cdm16CircuitAdapter();
            case CDM16_EMU:
                return new Cdm16CircuitAdapter();
            default:
                throw new UnsupportedOperationException();
        }
    }

    public static ProcessorAdapter getProcessorAdapter(String targetId) {
        if (!supportedTargets.containsKey(targetId)) {
            return null;
        }

        List<ProcessorType> supportedProcessorTypes = supportedTargets.get(targetId);
        Circuit currentCircuit = DebuggerComponent.getDebuggerCircuit();

        ProcessorAdapter targetProcessorAdapter = null;
        for (ProcessorType processorType : supportedProcessorTypes) {
            ProcessorAdapter currentProcessorAdapter = ProcessorAdapterFactory.getProcessorAdapter(processorType);

            if (currentProcessorAdapter.locateComponent(currentCircuit) != null) {
                targetProcessorAdapter = currentProcessorAdapter;
                break;
            }
        }

        return targetProcessorAdapter;
    }
}
