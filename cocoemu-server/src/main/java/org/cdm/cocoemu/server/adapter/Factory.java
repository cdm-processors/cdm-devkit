package org.cdm.cocoemu.server.adapter;

import org.cdm.cocoemu.components.processors.cdm16.Cdm16;
import org.cdm.cocoemu.core.image.Image;
import org.cdm.cocoemu.server.debug.DebugEnvironment;
import org.cdm.cocoemu.systems.HarvardSystem;
import org.cdm.cocoemu.systems.VonNeumannSystem;
import org.cdm.debug.dto.MemoryConfiguratons;

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

    public static DebugEnvironment<?> getDebugEnvironment(ProcessorType processorType, String memoryConfiguration) {
        switch (processorType) {
            case CDM8:
//                return new Cdm8CircuitAdapter();
            case CDM8E:
//                return new Cdm8eCircuitAdapter();
            case CDM16:
                Cdm16 processor = new Cdm16();
                if (memoryConfiguration.equals(MemoryConfiguratons.VON_NEUMANN)) {
                    return new DebugEnvironment<>(new Cdm16VonNeumannSystemAdapter(new VonNeumannSystem(processor, new Image())), processor) {};
                } else if (memoryConfiguration.equals(MemoryConfiguratons.HARVARD)) {
                    return new DebugEnvironment<>(new Cdm16HarvardSystemAdapter(new HarvardSystem(processor, new Image())), processor) {};
                } else {
                    throw new UnsupportedOperationException();
                }
            case CDM16E:
//                return new Cdm16EmulatorAdapter();
            default:
                throw new UnsupportedOperationException();
        }
    }
}


