package org.cdm.cocoemu.processors;

import org.cdm.cocoemu.image.LogisimImage;

public class MicrocodeLoader {
    private static final int MICROCODE_LENGTH = 1024;

    public static int[] loadFromResources(String filename) {
        int[] microcode;

        try {
            microcode = new LogisimImage().loadFromResources(filename).getIntegers();

            if (microcode.length != MICROCODE_LENGTH) {
                throw new RuntimeException(String.format(
                        "Microcode file (%s) has wrong length: %d, expected: %d",
                        filename, microcode.length, MICROCODE_LENGTH
                ));
            }
        } catch (Exception e) {
            throw new RuntimeException("Can't load microcode", e);
        }

        return microcode;
    }
}
