package org.cdm.logisim.runner;

import com.cburch.hex.HexModel;
import com.cburch.logisim.circuit.Analyze;
import com.cburch.logisim.circuit.Circuit;
import com.cburch.logisim.circuit.CircuitState;
import com.cburch.logisim.circuit.Propagator;
import com.cburch.logisim.comp.Component;
import com.cburch.logisim.file.LoadFailedException;
import com.cburch.logisim.file.Loader;
import com.cburch.logisim.file.LogisimFile;
import com.cburch.logisim.instance.Instance;
import com.cburch.logisim.instance.InstanceState;
import com.cburch.logisim.proj.Project;
import com.cburch.logisim.std.memory.Rom;
import com.cburch.logisim.std.wiring.Pin;
import com.google.gson.Gson;
import com.google.gson.JsonElement;
import org.cdm.logisim.memory.BankedMemState;
import org.cdm.logisim.memory.BankedRAM;

import java.io.File;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.OutputStreamWriter;
import java.nio.charset.StandardCharsets;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.Properties;
import java.util.stream.Collectors;

public class Runner {
    private static final int IMG_FILE = 0;
    private static final int CIRCUIT_FILE = 1;
    private static final int OUTPUT_FILE = 2;
    private static final int CONFIG_FILE = 3;
    private static final int TIMEOUT = 4;

    public Runner() {
    }

    public static void main(String[] args) {
        Runner runner = new Runner();
        File imgFile = new File(args[IMG_FILE]);
        File circuitFile = new File(args[CIRCUIT_FILE]);
        File configFile = new File(args[CONFIG_FILE]);
        if (!imgFile.exists()) {
            System.err.println("Cannot find image file");
            System.exit(1);
        } else if (!circuitFile.exists()) {
            System.err.println("Cannot find circuit file");
            System.exit(1);
        } else if (!configFile.exists()) {
            System.err.println("Cannot find config file");
            System.exit(1);
        } else if (!(new File(args[OUTPUT_FILE])).exists()) {
            System.err.println("Cannot find output file");
            System.exit(1);
        }

        OutputStreamWriter outputStreamWriter = null;

        try {
            outputStreamWriter = new OutputStreamWriter(
                    new FileOutputStream(args[OUTPUT_FILE]),
                    StandardCharsets.UTF_8);
        } catch (IOException e) {
            System.err.println("Failed to open OutputFile");
            System.exit(1);
        }

        int timeout = Integer.parseInt(args[TIMEOUT]);
        JsonElement res = runner.run(imgFile, circuitFile, configFile, timeout);

        try {
            System.out.println(res);
            outputStreamWriter.write(res.toString());
            outputStreamWriter.close();
        } catch (IOException e) {
            System.err.println("Failed to write to output file");
            System.exit(1);
        }

        System.exit(0);
    }

    private int getPinValue(CircuitState circuitState, Instance pin) {
        InstanceState state = circuitState.getInstanceState(pin);
        return Pin.FACTORY.getValue(state).toIntValue();
    }

    public JsonElement run(File inputFile, File circuitFile, File configFile, int timeout) {
        Properties configProperties = new Properties();

        try {
            configProperties.load(new FileInputStream(configFile));
        } catch (IllegalArgumentException | IOException var27) {
            System.err.println("Cannot find config file");
            System.exit(1);
        }

        List<String> pin_names = Arrays.stream(
                        configProperties.getProperty("pin_names").split(","))
                .map(String::trim)
                .toList();
        String halt_pin = configProperties.getProperty("halt_pin");
        Loader logisimLoader = new Loader(null);
        InputStream stream = null;

        try {
            stream = new FileInputStream(circuitFile);
        } catch (FileNotFoundException e) {
            System.err.println("Cannot find circuit file");
            System.exit(1);
        }

        LogisimFile logisimFile = null;

        try {
            logisimFile = logisimLoader.openLogisimFile(stream);
        } catch (IOException | LoadFailedException e) {
            System.err.println("unable to open logisim file");
            System.exit(1);
        }

        Project logisimProject = new Project(logisimFile);
        Circuit circuit = logisimFile.getMainCircuit();
        Map<String, Instance> outputPins = Analyze
                .getPinLabels(circuit)
                .entrySet()
                .stream()
                .filter(x -> !Pin.FACTORY.isInputPin(x.getKey()))
                .collect(Collectors.toMap(Map.Entry::getValue, Map.Entry::getKey));
        Instance haltPin = outputPins.get(halt_pin);
        if (haltPin == null) {
            throw new NullPointerException();
        } else {
            CircuitState circuitState = new CircuitState(logisimProject, circuit);
            Propagator propagator = circuitState.getPropagator();
            Component romComponent = circuit
                    .getNonWires()
                    .stream()
                    .filter(x -> x.getFactory() instanceof Rom)
                    .findFirst()
                    .orElse(null);
            if (romComponent == null) {
                System.err.println("there is no ROM found");
                System.exit(1);
            }

            propagator.propagate();

            try {
                ((Rom) romComponent.getFactory())
                        .loadImage(circuitState.getInstanceState(romComponent), inputFile);
            } catch (IOException e) {
                System.err.println("Failed to load image");
                System.exit(1);
            }

            propagator.propagate();

            int ticks;
            for (ticks = 0; ticks < timeout && this.getPinValue(circuitState, haltPin) == 0; ++ticks) {
                propagator.tick();
                propagator.propagate();
                ++ticks;
            }

            if (ticks == timeout) {
                System.err.println("Timeout");
                System.exit(1);
            }

            Map<String, Integer> registersValues = new HashMap<>();
            for (String pin : pin_names) {
                registersValues.put(pin, getPinValue(circuitState, outputPins.get(pin)));
            }

            HexModel contents = this.altGetRamContents(circuit, circuitState);
            List<Integer> r = new ArrayList<>();

            for (long i = 0L; i < contents.getLastOffset(); ++i) {
                r.add(contents.get(i));
            }

            Gson gson = new Gson();
            JsonElement g = gson.toJsonTree(registersValues);
            g.getAsJsonObject().add("mem", gson.toJsonTree(r));
            return g;
        }
    }

    private HexModel altGetRamContents(Circuit circuit, CircuitState circuitState) {
        Component ramComponent = circuit
                .getNonWires()
                .stream()
                .filter(x -> x.getFactory() instanceof BankedRAM)
                .findFirst()
                .orElseThrow();
        BankedMemState ramState = ((BankedRAM) ramComponent.getFactory())
                .getState(circuitState.getInstanceState(ramComponent));
        return ramState.getContents();
    }
}
