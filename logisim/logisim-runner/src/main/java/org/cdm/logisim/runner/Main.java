package org.cdm.logisim.runner;

import java.io.File;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.OutputStreamWriter;
import java.nio.charset.StandardCharsets;

public class Main {
    private static final int IMG_FILE = 0;
    private static final int CIRCUIT_FILE = 1;
    private static final int OUTPUT_FILE = 2;
    private static final int CONFIG_FILE = 3;
    private static final int TIMEOUT = 4;

    public static void main(String[] args) {
        System.setProperty("java.awt.headless", "true");

        File imgFile = new File(args[IMG_FILE]);
        File circuitFile = new File(args[CIRCUIT_FILE]);
        File configFile = new File(args[CONFIG_FILE]);

        if (!imgFile.exists()) {
            System.out.println("Cannot find image file");
            System.exit(1);
        } else if (!circuitFile.exists()) {
            System.out.println("Cannot find circuit file");
            System.exit(1);
        } else if (!configFile.exists()) {
            System.out.println("Cannot find config file");
            System.exit(1);
        } else if (!(new File(args[OUTPUT_FILE]).exists())){
            System.out.println("Cannot find output file");
            System.exit(1);
        }

        OutputStreamWriter outputStreamWriter = null;
        try {
            outputStreamWriter = new OutputStreamWriter(
                    new FileOutputStream(args[OUTPUT_FILE]),
                    StandardCharsets.UTF_8
            );
        } catch (IOException e){
            System.out.println("Failed to open OutputFile");
            System.exit(1);
        }
        int timeout = Integer.parseInt(args[TIMEOUT]);

        Runner runner = new Runner();
        String res = runner.run(imgFile, circuitFile, configFile, timeout);

        try {
            outputStreamWriter.write(res);
            outputStreamWriter.close();
        } catch (IOException e) {
            System.out.println("Failed to write to output file");
            System.exit(1);
        }

        System.exit(0);
    }
}
