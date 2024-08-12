package org.cdm.cocoemu.components.memory;

import lombok.AccessLevel;
import lombok.ToString;
import lombok.experimental.FieldDefaults;
import org.cdm.cocoemu.core.image.Image;
import org.cdm.cocoemu.core.ports.InputsClass;
import org.cdm.cocoemu.core.ports.InputsField;
import org.cdm.cocoemu.core.ports.OutputsClass;
import org.cdm.cocoemu.core.ports.OutputsField;

import java.nio.ByteBuffer;

public class Ram extends Rom {

    @InputsField
    public Ram.Inputs inputs;
    @OutputsField
    public Ram.Outputs outputs;

    public Ram(int size) {
        super(size);
    }

    public Ram(Image image) {
        super(image);
    }

    public Ram(ByteBuffer buffer) {
        super(buffer);
    }

    @Override
    public void clockRising() {
        if (inputs.select) {
            if (!inputs.rw) {
                buffer.put(inputs.address, (byte) inputs.data_in);
            }
        }
    }

    @ToString(callSuper = true)
    @FieldDefaults(level = AccessLevel.PUBLIC)
    @InputsClass
    public static class Inputs extends Rom.Inputs {
        public int data_in;
        public boolean rw;
    }

    @ToString(callSuper = true)
    @FieldDefaults(level = AccessLevel.PUBLIC)
    @OutputsClass
    public static class Outputs extends Rom.Outputs {
    }
}
