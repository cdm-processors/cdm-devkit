package org.cdm.cocoemu.server.debug;

import org.cdm.cocoemu.components.processors.cdm16.Cdm16;
import org.cdm.cocoemu.core.image.Image;
import org.cdm.cocoemu.server.adapters.systems.Cdm16HarvardSystemAdapter;
import org.cdm.cocoemu.server.adapters.systems.Cdm16VonNeumannSystemAdapter;
import org.cdm.cocoemu.systems.HarvardSystem;
import org.cdm.cocoemu.systems.VonNeumannSystem;

import static org.cdm.debug.dto.MemoryConfigurations.HARVARD;
import static org.cdm.debug.dto.MemoryConfigurations.VON_NEUMANN;
import static org.cdm.debug.dto.ProcessorTypes.*;

public class DebugEnvironmentFactory {
    public static DebugEnvironment getDebugEnvironment(String processorType, String memoryConfiguration) {
        switch (processorType) {
            case CDM16:
                Cdm16 processor = new Cdm16();

                switch (memoryConfiguration) {
                    case HARVARD: {
                        HarvardSystem system = new HarvardSystem(processor, new Image());
                        return new DebugEnvironment(system, new Cdm16HarvardSystemAdapter(system));
                    }
                    case VON_NEUMANN: {
                        VonNeumannSystem system = new VonNeumannSystem(processor, new Image());
                        return new DebugEnvironment(system, new Cdm16VonNeumannSystemAdapter(system));
                    }
                    default:
                        return null;
                }

            case CDM8:
            case CDM8E:
            case CDM16E:
            default:
                return null;
        }
    }
}
