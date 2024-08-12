package org.cdm.cocoemu.components.memory;

import org.cdm.cocoemu.core.PortedComponentBase;
import org.cdm.cocoemu.core.image.Image;

import java.nio.ByteBuffer;
import java.nio.ByteOrder;
import java.util.ArrayList;
import java.util.List;

public abstract class Memory extends PortedComponentBase {
    protected ByteBuffer buffer;

    public Memory(int size) {
        buffer = ByteBuffer.allocate(size);

        buffer.order(ByteOrder.LITTLE_ENDIAN);
    }

    public Memory(Image image) {
        buffer = ByteBuffer.wrap(image.getBytes());

        buffer.order(ByteOrder.LITTLE_ENDIAN);
    }

    public Memory(ByteBuffer buffer) {
        this.buffer = buffer;
    }

    public int size() {
        return buffer.capacity();
    }

    public ByteBuffer getBuffer() {
        return buffer;
    }

    public Image getImage() {
        List<Integer> array = new ArrayList<>(buffer.capacity());

        for (int i = 0; i < buffer.capacity(); i++) {
            array.add(Byte.toUnsignedInt(buffer.get(i)));
        }

        return new Image(array);
    }
}
