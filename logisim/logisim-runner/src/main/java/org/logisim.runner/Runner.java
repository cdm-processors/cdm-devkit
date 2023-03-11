package org.logisim.runner;

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
import com.cburch.logisim.std.memory.Ram;
import com.cburch.logisim.std.memory.Rom;
//import com.cburch.logisim.std.memory.MemState;
import com.cburch.logisim.std.wiring.Pin;
import com.google.gson.Gson;

import java.io.File;
import java.io.IOException;
import java.io.InputStream;
import java.lang.reflect.InvocationTargetException;
import java.lang.reflect.Method;
import java.util.Arrays;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.stream.Collectors;
import java.util.stream.LongStream;

public class Runner {
    private final List<String> PIN_NAMES = List.of("r0", "r1", "r2", "r3", "pc", "ps", "sp");
    private final String HALT_PIN = "halt";

    public int getPinValue(CircuitState circuitState, Instance pin){
        InstanceState state = circuitState.getInstanceState(pin);
        return Pin.FACTORY.getValue(state).toIntValue();
    }

    public String run(File inputFile, int timeout) throws IOException, LoadFailedException, ClassNotFoundException, InvocationTargetException, IllegalAccessException {
        System.out.println("Loading file...");
        Loader logisimLoader = new Loader(null);
        InputStream stream = Runner.class.getResourceAsStream("/runner.circ");
        LogisimFile logisimFile = logisimLoader.openLogisimFile(stream);
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

        Instance haltPin = outputPins.get(HALT_PIN);
        if (haltPin == null){
            throw new NullPointerException();
        }
        CircuitState circuitState = new CircuitState(logisimProject, circuit);
        Propagator propagator = circuitState.getPropagator();
        Component romComponent = circuit
                .getNonWires()
                .stream()
                .filter(x -> x.getFactory() instanceof Rom)
                .findFirst()
                .get();

        propagator.propagate();
        if (romComponent.getFactory() instanceof Rom){
            ((Rom) romComponent.getFactory())
                    .loadImage(
                            circuitState
                                    .getInstanceState(romComponent),
                            inputFile);
        }
        propagator.propagate();

        long start = System.currentTimeMillis();

        System.out.println("Starting simulation");
        while (true) {
            if (start + timeout < System.currentTimeMillis()) {
                System.out.println("Timeout");
                System.exit(1);
            }
            if (getPinValue(circuitState, haltPin) != 0) {
                break;
            }
            propagator.tick();
            propagator.propagate();
        }
        System.out.println("Simulation done");

        Map<String, Integer> registersValues = new HashMap<>();
        for (String pin : PIN_NAMES){
            registersValues.put(pin, getPinValue(circuitState, outputPins.get(pin)));
        }

        var contents = getRamContents(circuit, circuitState);

        LongStream ramData = LongStream
                .iterate(0, i -> i+1)
                .limit(contents.getLastOffset())
                .map(contents::get);

//        logisimLoader.

        var gson = new Gson();

        var g = gson.toJsonTree(registersValues);
        g.getAsJsonObject().add("mem", gson.toJsonTree(ramData));
        return g.toString();
    }

    private HexModel getRamContents(Circuit circuit, CircuitState circuitState) throws InvocationTargetException, IllegalAccessException, ClassNotFoundException {
        Component ramComponent = circuit
                .getNonWires()
                .stream()
                .filter(x -> x.getFactory() instanceof Ram)
                .findFirst()
                .get();
        Method getStateMethod = Arrays
                .stream(
                        ramComponent
                                .getFactory()
                                .getClass()
                                .getMethods())
                .filter(it -> it.getName().equals("getState") && it.getParameterCount() == 2)
                .findFirst()
                .orElse(null);
        getStateMethod.isAccessible();
        var ramState = getStateMethod.invoke(
                ramComponent.getFactory(),
                circuitState.getInstanceState(ramComponent));
        var contentsProperty = Arrays.stream(Class
                .forName("com.cburch.logisim.std.memory.MemState")
                .getMethods())
                .filter(it -> it.getName().equals("contents"))
                .findFirst()
                .get();
        return null;
    }
}
