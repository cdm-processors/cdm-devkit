package org.cdm.cocoemu.server.adapters.systems;

import org.cdm.cocoemu.components.memory.Memory;
import org.cdm.cocoemu.server.adapters.SystemAdapter;
import org.cdm.cocoemu.server.adapters.processors.Cdm16ProcessorAdapter;
import org.cdm.cocoemu.systems.HarvardSystem;

public class Cdm16HarvardSystemAdapter extends SystemAdapter {
    public HarvardSystem system;

    public Cdm16HarvardSystemAdapter(HarvardSystem system) {
        super(new Cdm16ProcessorAdapter(system.cdm16));
        this.system = system;
    }

    @Override
    public void resetSystem() {
        system.cdm16.reset();
    }

    @Override
    public Memory getRam() {
        return system.ram;
    }

    @Override
    public Memory getRom() {
        return system.rom;
    }
}
