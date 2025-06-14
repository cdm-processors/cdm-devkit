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
import com.cburch.logisim.std.wiring.Pin;
import org.cdm.logisim.memory.BankedMemState;
import org.cdm.logisim.memory.BankedRAM;
import org.cdm.logisim.memory.BankedROM;

import java.io.File;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.io.InputStream;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.Properties;
import java.util.stream.Collectors;

public class Runner {

    public RunnerState run(
            File inputFile,
            File circuitFile,
            File configFile,
            int timeout)
            throws RunnerException, TimeoutException {

        Properties configProperties = new Properties();

        try {
            configProperties.load(new FileInputStream(configFile));
        } catch (IllegalArgumentException | IOException var27) {
            throw new RunnerException("Cannot find config file");
        }

        List<String> pin_names = Arrays.stream(
                        configProperties.getProperty("pin_names").split(","))
                .map(String::trim)
                .toList();
        String halt_pin = configProperties.getProperty("halt_pin");
        Loader logisimLoader = new Loader(null);
        InputStream stream;

        try {
            stream = new FileInputStream(circuitFile);
        } catch (FileNotFoundException e) {
            throw new RunnerException("Cannot find circuit file");
        }

        LogisimFile logisimFile;

        try {
            logisimFile = logisimLoader.openLogisimFile(stream);
        } catch (IOException | LoadFailedException e) {
            throw new RunnerException("Unable to open Logisim file");
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
            throw new RunnerException("Unable to find halt pin");
        } else {
            CircuitState circuitState = new CircuitState(logisimProject, circuit);

            Propagator propagator = circuitState.getPropagator();
            propagator.propagate();

            switch (getMemoryArchitecture(configProperties)) {
                case HARVARD:
                    loadRom(inputFile, circuit, circuitState);
                    break;
                case VON_NEUMANN:
                    loadRam(inputFile, circuit, circuitState);
                    break;
            }

            propagator.propagate();

            int ticks;
            for (ticks = 0; ticks < timeout && this.getPinValue(circuitState, haltPin) == 0; ++ticks) {
                propagator.tick();
                propagator.propagate();
            }

            if (ticks == timeout) {
                throw new TimeoutException();
            }

            Map<String, Integer> registersValues = new HashMap<>();
            for (String pin : pin_names) {
                registersValues.put(pin, getPinValue(circuitState, outputPins.get(pin)));
            }

            HexModel contents = this.getRamContents(circuit, circuitState);
            List<Integer> memoryContent = new ArrayList<>();

            for (long i = 0L; i <= contents.getLastOffset(); ++i) {
                memoryContent.add(contents.get(i));
            }

            return new RunnerState(registersValues, memoryContent, ticks);
        }
    }

    private int getPinValue(CircuitState circuitState, Instance pin) {
        InstanceState state = circuitState.getInstanceState(pin);
        return Pin.FACTORY.getValue(state).toIntValue();
    }

    private Component getComponent(Circuit circuit, Class cls) {
        return circuit
                .getNonWires()
                .stream()
                .filter(x -> cls.isInstance(x.getFactory()))
                .findFirst()
                .orElse(null);
    }

    private void loadRam(File inputFile, Circuit circuit, CircuitState circuitState) throws RunnerException {
        Component ramComponent = getComponent(circuit, BankedRAM.class);
        if (ramComponent == null) {
            throw new RunnerException("Unable to find BankedRAM");
        }

        try {
            ((BankedRAM) ramComponent.getFactory())
                    .loadImage(circuitState.getInstanceState(ramComponent), inputFile);
        } catch (IOException e) {
            throw new RunnerException("Failed to load image");
        }
    }

    private void loadRom(File inputFile, Circuit circuit, CircuitState circuitState) throws RunnerException {
        Component romComponent = getComponent(circuit, BankedROM.class);
        if (romComponent == null) {
            throw new RunnerException("Unable to find BankedROM");
        }

        try {
            ((BankedROM) romComponent.getFactory())
                    .loadImage(circuitState.getInstanceState(romComponent), inputFile);
        } catch (IOException e) {
            throw new RunnerException("Failed to load image");
        }
    }

    private HexModel getRamContents(Circuit circuit, CircuitState circuitState) throws RunnerException {
        Component ramComponent = getComponent(circuit, BankedRAM.class);
        if (ramComponent == null) {
            throw new RunnerException("Unable to find BankedRAM");
        }

        BankedMemState ramState = ((BankedRAM) ramComponent.getFactory())
                .getState(circuitState.getInstanceState(ramComponent));
        return ramState.getContents();
    }

    private MemoryArchitecture getMemoryArchitecture(Properties configProperties) throws RunnerException {
        String memoryArchitectureProperty = configProperties.getProperty("memory_architecture");
        if (memoryArchitectureProperty == null) {
            memoryArchitectureProperty = "hv";
        }

        MemoryArchitecture memoryArchitecture =
                MemoryArchitecture.fromString(memoryArchitectureProperty);
        if (memoryArchitecture == null) {
            throw new RunnerException("Invalid memory architecture " + memoryArchitectureProperty);
        }

        return memoryArchitecture;
    }
}
