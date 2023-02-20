package org.cdm.logisim.emulator.cdm16;

import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.io.InputStream;

public class MicrocodeLoader {
    public static int[] loadFromFile(String filename) {

        int[] mc = new int[1024];

        try {
            BufferedReader reader = new BufferedReader(new FileReader(filename));

            reader.readLine();

            for (int i = 0; i < 1024; ++i) {
                mc[i] = Integer.parseInt(reader.readLine(), 16);
            }
        } catch (FileNotFoundException e) {
            throw new RuntimeException(e);
        } catch (IOException e) {
            throw new RuntimeException(e);
        }


        return mc;
    }
}
