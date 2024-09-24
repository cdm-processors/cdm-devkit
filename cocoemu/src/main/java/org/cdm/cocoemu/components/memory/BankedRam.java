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

public class BankedRam extends BankedRom {
    @InputsField
    public BankedRam.Inputs inputs;
    @OutputsField
    public BankedRam.Outputs outputs;

    public BankedRam(int size) {
        super(size);
    }

    public BankedRam(Image image) {
        super(image);
    }

    public BankedRam(ByteBuffer buffer) {
        super(buffer);
    }

    @Override
    public void clockRising() {
        if (inputs.select) {
            if (!inputs.rw) {
                if (inputs.word && inputs.address % 2 == 0) {
                    buffer.putShort(inputs.address, (short) inputs.data_in);
                } else {
                    buffer.put(inputs.address, (byte) inputs.data_in);
                }
            }
        }
    }

    @ToString(callSuper = true)
    @FieldDefaults(level = AccessLevel.PUBLIC)
    @InputsClass
    public static class Inputs extends BankedRom.Inputs {
        public int data_in;
        public boolean rw;
    }

    @ToString(callSuper = true)
    @FieldDefaults(level = AccessLevel.PUBLIC)
    @OutputsClass
    public static class Outputs extends BankedRom.Outputs {
    }
}
