package org.cdm.cocoemu.components.memory;

import lombok.AccessLevel;
import lombok.ToString;
import lombok.experimental.FieldDefaults;
import org.cdm.cocoemu.core.image.Image;
import org.cdm.cocoemu.core.ports.InputsClass;
import org.cdm.cocoemu.core.ports.InputsField;
import org.cdm.cocoemu.core.ports.OutputsClass;
import org.cdm.cocoemu.core.ports.OutputsField;

public class BankedRom extends Rom {
    @InputsField
    public BankedRom.Inputs inputs;
    @OutputsField
    public BankedRom.Outputs outputs;

    public BankedRom(int size) {
        super(size);
    }

    public BankedRom(Image image) {
        super(image);
    }

    @Override
    public void update() {
        if (inputs.select) {
            if (inputs.word) {
                if (inputs.address % 2 == 0) {
                    outputs.data_out = memory[inputs.address % memory.length]
                            + (memory[(inputs.address + 1) % memory.length] << 8);
                } else {
                    outputs.data_out = 0;
                }
            } else {
                super.update();
            }
        }
    }

    @ToString(callSuper = true)
    @FieldDefaults(level = AccessLevel.PUBLIC)
    @InputsClass
    public static class Inputs extends Rom.Inputs {
        boolean word;
    }

    @ToString(callSuper = true)
    @FieldDefaults(level = AccessLevel.PUBLIC)
    @OutputsClass
    public static class Outputs extends Rom.Outputs {
    }
}
