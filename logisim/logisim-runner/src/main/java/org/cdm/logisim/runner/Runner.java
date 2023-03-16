package org.cdm.logisim.runner;

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
import com.cburch.logisim.std.wiring.Pin;
import com.google.gson.Gson;
import com.google.gson.JsonElement;
import org.cdm.logisim.memory.BankedRAM;
import org.cdm.logisim.memory.BankedROM;

import java.io.File;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.io.InputStream;
import java.util.Arrays;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.Properties;
import java.util.stream.Collectors;

public class Runner {
    public int getPinValue(CircuitState circuitState, Instance pin) {
        InstanceState state = circuitState.getInstanceState(pin);
        return Pin.FACTORY.getValue(state).toIntValue();
    }

    public String run(File inputFile, File circuitFile, File configFile, int timeout){
        System.out.println("Loading file...");

        Properties configProperties = new Properties();

        try {
            configProperties.load(new FileInputStream(configFile));
        } catch (IOException|IllegalArgumentException e){
            System.out.println("Cannot find config file");
            System.exit(1);
        }

        List<String> pin_names = Arrays
                .stream(configProperties
                        .getProperty("pin_names")
                        .split(","))
                .map(String::trim)
                .toList();

        String halt_pin = configProperties.getProperty("halt_pin");

        Loader logisimLoader = new Loader(null);

        InputStream stream = null;
        try {
            stream = new FileInputStream(circuitFile);
        } catch (FileNotFoundException e){
            System.out.println("Cannot find circuit file");
            System.exit(1);
        }
        LogisimFile logisimFile = null;
        try {
            logisimFile = logisimLoader.openLogisimFile(stream);
        } catch (LoadFailedException|IOException e){
            System.out.println("unable to open logisim file");
            System.exit(1);
        }
        Project logisimProject = new Project(logisimFile);
        Circuit circuit = logisimFile.getMainCircuit();

        Map<String, Instance> outputPins = Analyze
                .getPinLabels(circuit)
                .entrySet()
                .stream()
                .filter(x -> Pin.FACTORY.isInputPin(x.getKey()))
                .collect(
                        Collectors.toMap(Map.Entry::getValue, Map.Entry::getKey)
                );

        Instance haltPin = outputPins.get(halt_pin);
        if (haltPin == null) {
            throw new NullPointerException();
        }
        CircuitState circuitState = new CircuitState(logisimProject, circuit);
        Propagator propagator = circuitState.getPropagator();
        Component romComponent = circuit
                .getNonWires()
                .stream()
                .filter(x -> x.getFactory() instanceof BankedROM)
                .findFirst()
                .orElse(null);

        if (romComponent == null){
            System.out.println("there is no ROM found");
            System.exit(1);
        }

        propagator.propagate();
        if (romComponent.getFactory() instanceof BankedROM) {
            try {
                ((BankedROM) romComponent.getFactory())
                        .loadImage(
                                circuitState
                                        .getInstanceState(romComponent),
                                inputFile);
            } catch (IOException e){
                System.out.println("Failed to load image");
                System.exit(1);
            }
        }
        propagator.propagate();

        System.out.println("Starting simulation");
        int ticks;
        for (ticks = 0; ticks < timeout; ticks++) {
            if (getPinValue(circuitState, haltPin) != 0) {
                break;
            }
            propagator.tick();
            propagator.propagate();
            ticks++;
        }
        if (ticks == timeout) {
            System.out.println("Timeout");
            System.exit(1);
        }
        System.out.println("Simulation done");

        Map<String, Integer> registersValues = new HashMap<>();
        for (String pin : pin_names) {
            registersValues.put(pin, getPinValue(circuitState, outputPins.get(pin)));
        }

        var contents = getRamContents(circuit, circuitState);

        if (contents == null){
            System.out.println("there is no RAM found");
            return "";
        }

        var ramData = contents
                .stream()
                .flatMap(List::stream)
                .collect(Collectors.toList());

        var gson = new Gson();

        JsonElement g = gson.toJsonTree(registersValues);
        g.getAsJsonObject().add("mem", gson.toJsonTree(ramData));
        return g.toString();
    }

    private List<List<Integer>> getRamContents(Circuit circuit, CircuitState circuitState) {
        Component ramComponent = circuit
                .getNonWires()
                .stream()
                .filter(x -> x.getFactory() instanceof BankedRAM)
                .findFirst()
                .orElse(null);

        if (ramComponent == null){
            return null;
        }

        return ((BankedRAM) ramComponent.getFactory())
                .getPrettyContent(circuitState.getInstanceState(ramComponent));
    }
}
