package org.cdm.cocoemu.server.adapter;

import org.cdm.cocoemu.components.processors.cdm16.Cdm16;
import org.cdm.cocoemu.server.emulator.CdM16Emulator;
import org.cdm.cocoemu.server.debug.DebugEnvironment;

import java.util.*;

public class Factory {
    private static final Map<String, List<ProcessorType>> supportedTargets = new HashMap<>();
    static {
        supportedTargets.put(
                "cdm8",
                Collections.singletonList(ProcessorType.CDM8)
        );

        supportedTargets.put(
                "cdm8e",
                Collections.singletonList(ProcessorType.CDM8E)
        );

        supportedTargets.put(
                "cdm16",
                Arrays.asList(ProcessorType.CDM16, ProcessorType.CDM16E)
        );
    }

    public static DebugEnvironment<?> getDebugEnvironment(ProcessorType processorType) {
        switch (processorType) {
            case CDM8:
//                return new Cdm8CircuitAdapter();
            case CDM8E:
//                return new Cdm8eCircuitAdapter();
            case CDM16:
                Cdm16 processor = new Cdm16();
                return new DebugEnvironment<>(new Cdm16Adapter(processor), new CdM16Emulator(processor)) {};
            case CDM16E:
//                return new Cdm16EmulatorAdapter();
            default:
                throw new UnsupportedOperationException();
        }
    }
}


