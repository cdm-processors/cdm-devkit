package org.cdm.cocoemu.components.memory;

import lombok.AccessLevel;
import lombok.ToString;
import lombok.experimental.FieldDefaults;
import org.cdm.cocoemu.core.image.Image;
import org.cdm.cocoemu.core.ports.InputsClass;
import org.cdm.cocoemu.core.ports.InputsField;
import org.cdm.cocoemu.core.ports.OutputsClass;
import org.cdm.cocoemu.core.ports.OutputsField;

public class Rom extends Memory {

    @InputsField
    public Rom.Inputs inputs;
    @OutputsField
    public Rom.Outputs outputs;

    public Rom(int size) {
        super(size);
    }

    public Rom(Image image) {
        super(image);
    }


    @Override
    public void update() {
        if (inputs.select) {
            outputs.data_out = memory[inputs.address % memory.length];
        }
    }

    @ToString
    @FieldDefaults(level = AccessLevel.PUBLIC)
    @InputsClass
    public static class Inputs {
        int address;
        boolean select;
    }

    @ToString
    @FieldDefaults(level = AccessLevel.PUBLIC)
    @OutputsClass
    public static class Outputs {
        int data_out;
    }
}
