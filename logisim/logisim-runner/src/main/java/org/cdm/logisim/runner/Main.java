package org.cdm.logisim.runner;

import com.google.gson.Gson;
import com.google.gson.JsonObject;

import java.io.File;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.OutputStreamWriter;

public class Main {

    private static final int EXIT_SUCCESS = 0;
    private static final int EXIT_FAILURE = 1;
    private static final int EXIT_TIMEOUT = 13;

    private static final int IMG_FILE = 0;
    private static final int CIRCUIT_FILE = 1;
    private static final int OUTPUT_FILE = 2;
    private static final int CONFIG_FILE = 3;
    private static final int TIMEOUT = 4;

    public static void main(String[] args) {
        if (args.length < 5) {
            System.err.println("Invalid arguments");
            System.err.println("Usage: logisim-runner.jar " +
                    "[programImage] [circuit] [outputImage] [config] [timeout]"
            );
            System.exit(EXIT_FAILURE);
        }

        Runner runner = new Runner();

        File imgFile = new File(args[IMG_FILE]);
        File circuitFile = new File(args[CIRCUIT_FILE]);
        File configFile = new File(args[CONFIG_FILE]);

        if (!imgFile.exists()) {
            System.err.println("Cannot find image file");
            System.exit(EXIT_FAILURE);
        } else if (!circuitFile.exists()) {
            System.err.println("Cannot find circuit file");
            System.exit(EXIT_FAILURE);
        } else if (!configFile.exists()) {
            System.err.println("Cannot find config file");
            System.exit(EXIT_FAILURE);
        }

        OutputStreamWriter outputStreamWriter = null;

        try {
            outputStreamWriter = new OutputStreamWriter(
                    new FileOutputStream(args[OUTPUT_FILE])
            );
        } catch (IOException e) {
            System.err.println("Failed to open output file");
            System.exit(EXIT_FAILURE);
        }

        int timeout = Integer.parseInt(args[TIMEOUT]);

        RunnerState result = null;

        try {
            result = runner.run(imgFile, circuitFile, configFile, timeout);
        } catch (RunnerException e) {
            System.err.println(e.getMessage());
            System.exit(EXIT_FAILURE);
        } catch (TimeoutException e) {
            System.err.println("Timeout");
            System.exit(EXIT_TIMEOUT);
        }

        Gson gson = new Gson();

        JsonObject root = new JsonObject();

        root.add("registers", gson.toJsonTree(result.registers()));
        root.add("ticks", gson.toJsonTree(result.ticks()));
        root.add("image_size", gson.toJsonTree(result.memory().size()));

        System.out.println(root);

        try {
            outputStreamWriter.write(gson.toJsonTree(result.memory()).toString());
            outputStreamWriter.close();
        } catch (IOException e) {
            System.err.println("Failed to write to output file");
            System.exit(EXIT_FAILURE);
        }

        System.exit(EXIT_SUCCESS);
    }
}
