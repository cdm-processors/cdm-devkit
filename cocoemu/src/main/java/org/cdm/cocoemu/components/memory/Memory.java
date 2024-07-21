package org.cdm.cocoemu.components.memory;

import org.cdm.cocoemu.core.PortedComponentBase;
import org.cdm.cocoemu.core.image.Image;

public abstract class Memory extends PortedComponentBase {
    protected int[] memory;

    public Memory(int size) {
        memory = new int[size];
    }

    public Memory(Image image) {
        memory = image.getIntegers();
    }

    public int size() {
        return memory.length;
    }

    public int[] getMemory() {
        return memory;
    }

    public Image getImage() {
        return new Image(memory);
    }
}
