package org.cdm.cocoemu.systems;

import org.cdm.cocoemu.components.memory.BankedRam;
import org.cdm.cocoemu.components.processors.cdm16.Cdm16;
import org.cdm.cocoemu.core.Component;
import org.cdm.cocoemu.core.image.Image;
import org.cdm.cocoemu.core.primitives.Bus;

public class VonNeumannSystem implements Component {
    public static final int MEMORY_SIZE = 65536;

    public Cdm16 cdm16;
    public BankedRam ram;
    public Bus addressBus = new Bus("addr", 16);
    public Bus dataBus = new Bus("data", 16);

    public boolean mem = false;
    public boolean read = false;
    public boolean word = false;


    public VonNeumannSystem(Cdm16 processor, Image image) {
        cdm16 = processor;

        image.pad(MEMORY_SIZE, 0);
        ram = new BankedRam(image);
        update();
    }

    @Override
    public void clockRising() {
        ram.clockRising();
    }

    @Override
    public void clockFalling() {
        cdm16.clockFalling();
    }

    @Override
    public void update() {
        cdm16.update();

        mem = cdm16.outputs.mem;
        read = cdm16.outputs.read;
        word = cdm16.outputs.word;

        addressBus.setValue(cdm16.outputs.address);

        if (!read) {
            dataBus.setValue(cdm16.outputs.data_out);
        }

        ram.inputs.data_in = dataBus.getValue();
        ram.inputs.select = mem;
        ram.inputs.rw = read;
        ram.inputs.word = word;
        ram.inputs.address = addressBus.getValue();
        ram.update();

        if (ram.inputs.select && ram.inputs.rw) {
            dataBus.setValue(ram.outputs.data_out);
        }

        cdm16.inputs.data_in = dataBus.getValue();
    }
}
