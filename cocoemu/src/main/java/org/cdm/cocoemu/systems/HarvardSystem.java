package org.cdm.cocoemu.systems;

import org.cdm.cocoemu.components.memory.BankedRam;
import org.cdm.cocoemu.components.memory.BankedRom;
import org.cdm.cocoemu.components.processors.cdm16.Cdm16;
import org.cdm.cocoemu.core.Component;
import org.cdm.cocoemu.core.image.Image;
import org.cdm.cocoemu.core.primitives.Bus;

public class HarvardSystem implements Component {
    public static final int MEMORY_SIZE = 65536;

    public Cdm16 cdm16;
    public BankedRom rom;
    public BankedRam ram = new BankedRam(MEMORY_SIZE);
    public Bus addressBus = new Bus("addr", 16);
    public Bus dataBus = new Bus("data", 16);

    public boolean mem = false;
    public boolean read = false;
    public boolean word = false;

    public boolean inst = false;
    public boolean data = false;

    public HarvardSystem(Cdm16 processor, Image image) {
        cdm16 = processor;

        image.pad(MEMORY_SIZE, 0);
        rom = new BankedRom(image);

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

        data = mem && cdm16.outputs.data;
        inst = mem && !cdm16.outputs.data;

        addressBus.setValue(cdm16.outputs.address);

        if (!read) {
            dataBus.setValue(cdm16.outputs.data_out);
        }

        rom.inputs.address = addressBus.getValue();
        rom.inputs.select = inst;
        rom.inputs.word = word;
        rom.update();

        if (rom.inputs.select) {
            dataBus.setValue(rom.outputs.data_out);
        }

        ram.inputs.data_in = dataBus.getValue();
        ram.inputs.select = data;
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
