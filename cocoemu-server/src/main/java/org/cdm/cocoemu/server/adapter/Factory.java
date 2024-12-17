package org.cdm.cocoemu.server.adapter;

import org.cdm.cocoemu.components.processors.cdm16.Cdm16;
import org.cdm.cocoemu.core.Component;
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
                Collections.singletonList(ProcessorType.CDM16)
        );

        supportedTargets.put(
                "cdm16e",
                Collections.singletonList(ProcessorType.CDM16E)
        );
    }

    public static DebugEnvironment<? extends Component> getDebugEnvironment(ProcessorType processorType, String memoryConfiguration) {
        switch (processorType) {
            case CDM8:
//                return new Cdm8CircuitAdapter();
            case CDM8E:
//                return new Cdm8eCircuitAdapter();
            case CDM16:
                Cdm16 processor = new Cdm16();
                if (memoryConfiguration.equals(MemoryConfiguratons.VON_NEUMANN)) {
                    VonNeumannSystem system = new VonNeumannSystem(processor, new Image());
                    return new DebugEnvironment<>(new Cdm16VonNeumannSystemAdapter(system), system) {};
                } else if (memoryConfiguration.equals(MemoryConfiguratons.HARVARD)) {
                    HarvardSystem system = new HarvardSystem(processor, new Image());
                    return new DebugEnvironment<>(new Cdm16HarvardSystemAdapter(system), system) {};
                } else {
                    throw new UnsupportedOperationException();
                }
            case CDM16E:
//                return new Cdm16EmulatorAdapter();
            default:
                throw new UnsupportedOperationException();
        }
    }

    public static DebugEnvironment<? extends Component> getDebugEnvironment(String target, String memoryConfiguration) {
        if (!supportedTargets.containsKey(target)) {
            return null;
        }

        List<ProcessorType> processors = supportedTargets.get(target);
        DebugEnvironment<? extends Component> environment = null;
        for (ProcessorType processorType : processors) {
             environment = Factory.getDebugEnvironment(processorType, memoryConfiguration);
        }
        return environment;
    }
}


