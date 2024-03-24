package org.cdm.logisim.emulator.cdm16;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOError;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;

public class MicrocodeLoader {
    private static final int MICROCODE_LENGTH = 1024;

    public static int[] loadFromFile(String filename) {

        int[] mc = new int[MICROCODE_LENGTH];

        try {
            BufferedReader reader = new BufferedReader(new FileReader(filename));

            reader.readLine();

            for (int i = 0; i < MICROCODE_LENGTH; ++i) {
                mc[i] = Integer.parseInt(reader.readLine(), 16);
            }
        } catch (IOException e) {
            throw new IOError(e);
        }


        return mc;
    }

    public static int[] loadFromResources(String filename) {
        InputStream inputStream = MicrocodeLoader.class.getResourceAsStream(filename);

        if (inputStream == null) {
            throw new IOError(new IOException());
        }

        InputStreamReader inputStreamReader = new InputStreamReader(inputStream);

        int[] mc = new int[MICROCODE_LENGTH];

        try {
            BufferedReader reader = new BufferedReader(inputStreamReader);

            reader.readLine();

            for (int i = 0; i < MICROCODE_LENGTH; ++i) {
                mc[i] = Integer.parseInt(reader.readLine(), 16);
            }
        } catch (IOException e) {
            throw new IOError(e);
        }


        return mc;
    }
}
