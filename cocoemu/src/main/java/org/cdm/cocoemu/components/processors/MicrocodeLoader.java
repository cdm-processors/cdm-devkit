package org.cdm.cocoemu.components.processors;

import org.cdm.cocoemu.core.image.ImageLoader;

public class MicrocodeLoader {
    public static int[] loadFromResources(String filename, int microcodeLength) {
        int[] microcode;

        try {
            microcode = ImageLoader.loadFromResources(filename).getIntegers();

            if (microcode.length != microcodeLength) {
                throw new RuntimeException(String.format(
                        "Microcode file (%s) has wrong length: %d, expected: %d",
                        filename, microcode.length, microcodeLength
                ));
            }
        } catch (Exception e) {
            throw new RuntimeException("Can't load microcode", e);
        }

        return microcode;
    }
}
