package org.cdm.cocoemu.server.adapters.systems;

import org.cdm.cocoemu.components.memory.Memory;
import org.cdm.cocoemu.server.adapters.SystemAdapter;
import org.cdm.cocoemu.server.adapters.processors.Cdm16ProcessorAdapter;
import org.cdm.cocoemu.systems.VonNeumannSystem;

public class Cdm16VonNeumannSystemAdapter extends SystemAdapter {
    public VonNeumannSystem system;

    public Cdm16VonNeumannSystemAdapter(VonNeumannSystem system) {
        super(new Cdm16ProcessorAdapter(system.cdm16));
        this.system = system;
    }

    @Override
    public Memory getRam() {
        return system.ram;
    }

    @Override
    public Memory getRom() {
        return system.ram;
    }
}
