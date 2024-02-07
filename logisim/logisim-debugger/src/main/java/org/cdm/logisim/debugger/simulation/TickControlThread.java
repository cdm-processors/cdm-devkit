package org.cdm.logisim.debugger.simulation;

import com.cburch.hex.HexModel;
import com.cburch.logisim.circuit.Circuit;
import com.cburch.logisim.circuit.CircuitState;
import com.cburch.logisim.comp.Component;
import com.cburch.logisim.proj.Project;
import com.google.gson.Gson;
import org.cdm.logisim.debugger.DebuggerComponent;
import org.cdm.logisim.debugger.adapters.ProcessorAdapter;
import org.cdm.logisim.debugger.adapters.ProcessorAdapterFactory;
import org.cdm.logisim.debugger.adapters.ProcessorState;
import org.cdm.logisim.debugger.dto.ActionResponse;
import org.cdm.logisim.debugger.dto.BreakpointsMessage;
import org.cdm.logisim.debugger.dto.BytesLoadMessage;
import org.cdm.logisim.debugger.dto.DebugEvent;
import org.cdm.logisim.debugger.dto.DebuggerMessage;
import org.cdm.logisim.debugger.dto.DebuggerResponse;
import org.cdm.logisim.debugger.dto.FailResponse;
import org.cdm.logisim.debugger.dto.GetMemoryMessage;
import org.cdm.logisim.debugger.dto.GetMemoryResponse;
import org.cdm.logisim.debugger.dto.GetRegistersResponse;
import org.cdm.logisim.debugger.dto.GetTunnelMessage;
import org.cdm.logisim.debugger.dto.GetTunnelResponse;
import org.cdm.logisim.debugger.dto.InitializationMessage;
import org.cdm.logisim.debugger.dto.InitializationResponse;
import org.cdm.logisim.debugger.dto.LineLocationsMessage;
import org.cdm.logisim.debugger.dto.LoadMessage;
import org.cdm.logisim.debugger.dto.MemoryConfiguratons;
import org.cdm.logisim.debugger.dto.MessageActions;
import org.cdm.logisim.debugger.dto.PathLoadMessage;
import org.cdm.logisim.debugger.dto.RunMessage;
import org.cdm.logisim.debugger.dto.SetMemoryMessage;
import org.cdm.logisim.debugger.logisim.MemoryAdapter;
import org.cdm.logisim.debugger.logisim.TunnelAdapter;

import java.io.File;
import java.lang.reflect.InvocationTargetException;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.concurrent.BlockingQueue;
import java.util.function.Consumer;

import static org.cdm.logisim.debugger.logisim.MemoryAdapter.getMemoryContents;
import static org.cdm.logisim.debugger.logisim.MemoryAdapter.locateRamComponent;
import static org.cdm.logisim.debugger.logisim.MemoryAdapter.locateRomComponent;

public class TickControlThread extends Thread {
    private final BlockingQueue<DebuggerMessage> messageQueue;
    private final Consumer<String> sendMessageCallback;

    private List<Integer> lineLocations = new ArrayList<>();
    private List<Integer> breakpoints = new ArrayList<>();

    private ProcessorState lastProcessorState;

    private boolean simulationRunning = false;

    private Component romComponent = null;
    private Component ramComponent = null;

    public TickControlThread(BlockingQueue<DebuggerMessage> messageQueue, Consumer<String> sendMessageCallback) {
        this.messageQueue = messageQueue;
        this.sendMessageCallback = sendMessageCallback;
    }

    private void sendMessage(String message) {
        if (sendMessageCallback != null) {
            sendMessageCallback.accept(message);
        }
    }

    private void sendDebugEvent(String eventType) {
        sendMessage(
                new Gson().toJson(
                        new DebugEvent(eventType)
                )
        );
    }

    private void sendResponse(DebuggerResponse response) {
        sendMessage(
                new Gson().toJson(response)
        );
    }

    private void sendFailResponse(String message) {
        sendMessage(
                new Gson().toJson(
                        new FailResponse(message)
                )
        );
    }

    @Override
    public void run() {
        while (!this.isInterrupted()) {
            handleMessage(true);
        }
    }

    public void runSimulation(StopConditions stopConditions) {
        if (simulationRunning) {
            return;
        } else {
            simulationRunning = true;
        }

        try {
            lastProcessorState = DebuggerComponent.getSimulationTicker().tickUntil((state) -> {
                handleMessage(false);

                StopConditions chekedStopConditions =
                        StopConditions.check(state, stopConditions, breakpoints, lineLocations);

                return !simulationRunning || state.isHalted()
                        || chekedStopConditions.stopOnFetch()
                        || chekedStopConditions.stopOnBreakpoint()
                        || chekedStopConditions.stopOnLine()
                        || chekedStopConditions.stopOnException();
            });
        } catch (InterruptedException e) {
            throw new RuntimeException(e);
        }

        StopConditions chekedStopConditions =
                StopConditions.check(lastProcessorState, stopConditions, breakpoints, lineLocations);

        String reason = DebugEvent.REASON_UNKNOWN;

        if (chekedStopConditions.stopOnFetch()) {
            reason = DebugEvent.REASON_FETCH;
        }

        if (chekedStopConditions.stopOnLine()) {
            reason = DebugEvent.REASON_LINE;
        }

        if (chekedStopConditions.stopOnBreakpoint()) {
            reason = DebugEvent.REASON_BREAKPOINT;
        }

        if (chekedStopConditions.stopOnException()) {
            reason = DebugEvent.REASON_EXCEPTION;
        }

        if (lastProcessorState.isHalted()) {
            reason = DebugEvent.REASON_HALT;
        }

        if (!simulationRunning) {
            reason = DebugEvent.REASON_PAUSE;
        }

        simulationRunning = false;
        sendDebugEvent(reason);
    }

    public void stopSimulation() {
        simulationRunning = false;
    }

    public void handleMessage(boolean block) {
        if (!block && messageQueue.isEmpty()) {
            return;
        }

        DebuggerMessage message;

        try {
            message = messageQueue.take();
        } catch (InterruptedException e) {
            throw new RuntimeException(e);
        }

        System.out.printf("%s %s\n", message.action, message.data);

        switch (message.action) {
            case MessageActions.PING:
                sendMessage("Pong");
                break;
            case MessageActions.SET_BREAKPOINTS:
                handleBreakpointsMessage(
                        new Gson().fromJson(message.data, BreakpointsMessage.class)
                );
                break;
            case MessageActions.SET_LINE_LOCATIONS:
                handleLineLocationsMessage(
                        new Gson().fromJson(message.data, LineLocationsMessage.class)
                );
                break;
            case MessageActions.STEP:
                handleStepMessage();
                break;
            case MessageActions.RUN:
                handleRunMessage(
                        new Gson().fromJson(message.data, RunMessage.class)
                );
                break;
            case MessageActions.PAUSE:
                handlePauseMessage();
                break;
            case MessageActions.RESET:
                handleResetMessage();
                break;
            case MessageActions.LOAD:
                String source = new Gson().fromJson(
                        message.data.get(LoadMessage.SOURCE_FIELD),
                        String.class
                );

                switch (source) {
                    case PathLoadMessage.SOURCE:
                        handlePathLoadMessage(
                                new Gson().fromJson(message.data, PathLoadMessage.class)
                        );
                        break;
                    case BytesLoadMessage.SOURCE:
                        handleBytesLoadMessage(
                                new Gson().fromJson(message.data, BytesLoadMessage.class)
                        );
                        break;
                    default:
                        sendFailResponse("Unknown source: " + source);
                        return;
                }
                break;
            case MessageActions.INIT:
                handleInitMessage(
                        new Gson().fromJson(message.data, InitializationMessage.class)
                );
                break;
            case MessageActions.GET_REGISTERS:
                handleGetRegistersMessage();
                break;
            case MessageActions.GET_MEMORY:
                handleGetMemoryMessage(
                        new Gson().fromJson(message.data, GetMemoryMessage.class)
                );
                break;
            case MessageActions.SET_MEMORY:
                handleSetMemoryMessage(
                        new Gson().fromJson(message.data, SetMemoryMessage.class)
                );
                break;
            case MessageActions.GET_TUNNEL:
                handleGetTunnelMessage(
                        new Gson().fromJson(message.data, GetTunnelMessage.class)
                );
                break;
            default:
                sendFailResponse("Unknown action: " + message.action);
        }
    }

    private void handleBreakpointsMessage(BreakpointsMessage message) {
        System.out.println("Break");
        breakpoints = message.breakpoints;

        sendResponse(new ActionResponse(MessageActions.SET_BREAKPOINTS));
    }

    private void handleLineLocationsMessage(LineLocationsMessage message) {
        System.out.println("LLoc");
        lineLocations = message.lineLocations;

        sendResponse(new ActionResponse(MessageActions.SET_LINE_LOCATIONS));
    }

    private void handleStepMessage() {
        System.out.println("Step");
        runSimulation(new StopConditions().all());

        sendResponse(new ActionResponse(MessageActions.STEP));
    }

    private void handleRunMessage(RunMessage message) {
        System.out.println("Run");

        runSimulation(
                StopConditions.fromStrings(message.stopConditions)
        );

//        runSimulation(
//                new StopConditions()
//                        .exception()
//                        .breakpoint()
//        );

        sendResponse(new ActionResponse(MessageActions.RUN));
    }

    private void handlePauseMessage() {
        System.out.println("Pause");
        stopSimulation();

        sendResponse(new ActionResponse(MessageActions.PAUSE));
    }

    private void handleResetMessage() {
        System.out.println("Reset");

        DebuggerComponent
                .getSimulationTicker()
                .getProject()
                .getSimulator()
                .requestReset();

        System.out.println("Sleep " + DebuggerComponent.getResetTimeout() + " ms");
        try {
            sleep(DebuggerComponent.getResetTimeout());
        } catch (InterruptedException ignored) {

        }

        sendResponse(new ActionResponse(MessageActions.RESET));
    }

    private void handleInitMessage(InitializationMessage message) {
        System.out.println("Init with " + message.target);

        ProcessorAdapter processorAdapter = ProcessorAdapterFactory.getProcessorAdapter(message.target);
        if (processorAdapter == null) {
            sendFailResponse("Processor component not found for target " + message.target);
            return;
        }

        DebuggerComponent.setProcessorAdapter(processorAdapter);

        Circuit debuggerCircuit = DebuggerComponent.getDebuggerCircuit();
        ramComponent = locateRamComponent(debuggerCircuit);

        if (ramComponent == null) {
            sendFailResponse("RAM is not found");
            return;
        }

        if (message.memoryConfiguration.equals(MemoryConfiguratons.VON_NEUMANN)) {
            romComponent = ramComponent;
        } else if (message.memoryConfiguration.equals(MemoryConfiguratons.HARVARD)) {
            romComponent = locateRomComponent(debuggerCircuit);

            if (romComponent == null) {
                sendFailResponse("ROM is not found");
                return;
            }
        } else {
            sendFailResponse("Invalid memory configuration " + message.memoryConfiguration);
            return;
        }

        System.out.println("Init with " + message.memoryConfiguration);

        DebuggerComponent.setServerStatus("Debug active"/* + processorAdapter.getDisplayName()*/);

        sendResponse(
                InitializationResponse.builder()
                        .registerNames(processorAdapter.getRegisterNames())
                        .registerSizes(processorAdapter.getRegisterSizes())
                        .ramSize(processorAdapter.getMemorySize())
                        .supportsExceptions(processorAdapter.supportsExceptions())
                        .build()
        );
    }

    private void handleGetRegistersMessage() {
        System.out.println("Get registers");

        if (lastProcessorState == null) {
            sendFailResponse("No active processor state");
            return;
        }

        sendResponse(new GetRegistersResponse(lastProcessorState.getRegisters()));
    }

    private void handleGetMemoryMessage(GetMemoryMessage message) {
        System.out.printf("Get %d bytes at %d\n", message.size, message.offset);

        Project project = DebuggerComponent.getSimulationTicker().getProject();
        Circuit currentCircuit = DebuggerComponent.getDebuggerCircuit();
        CircuitState currentCircuitState = project.getCircuitState(currentCircuit);

        if (ramComponent == null) {
            sendFailResponse("RAM is not found");
            return;
        }

        HexModel contents;
        try {
            contents = getMemoryContents(ramComponent.getFactory(), currentCircuitState.getInstanceState(ramComponent));
        } catch (NoSuchMethodException | IllegalAccessException | InvocationTargetException e) {
            throw new RuntimeException(e);
        }

        List<Integer> ramData = new ArrayList<>();

        long firstOffset = contents.getFirstOffset();
        long lastOffset = contents.getLastOffset();

        if (message.offset < firstOffset || message.offset + message.size > lastOffset) {
            sendFailResponse("Invalid memory range");
            return;
        }

        for (long i = message.offset; i < message.offset + message.size; ++i) {
            ramData.add(contents.get(i));
        }

        sendResponse(
                new GetMemoryResponse(ramData)
        );
    }

    private void handlePathLoadMessage(PathLoadMessage message) {
        System.out.println("Load path " + message.path);

        Project project = DebuggerComponent.getSimulationTicker().getProject();
        Circuit currentCircuit = DebuggerComponent.getDebuggerCircuit();
        CircuitState currentCircuitState = project.getCircuitState(currentCircuit);

        if (romComponent == null) {
            sendFailResponse("ROM is not found");
            return;
        }

        File imageFile = new File(message.path);

        try {
            MemoryAdapter.loadImage(imageFile, romComponent.getFactory(), currentCircuitState.getInstanceState(romComponent));
        } catch (NoSuchMethodException | InvocationTargetException | IllegalAccessException e) {
            sendFailResponse("Failed to load an image");
            e.printStackTrace();
            System.err.println("Failed to load an image");
            return;
        }

        sendResponse(new ActionResponse(MessageActions.LOAD));
    }

    private void handleBytesLoadMessage(BytesLoadMessage message) {
        System.out.println("Load bytes " + Arrays.toString(message.bytes));

        Project project = DebuggerComponent.getSimulationTicker().getProject();
        Circuit currentCircuit = DebuggerComponent.getDebuggerCircuit();
        CircuitState currentCircuitState = project.getCircuitState(currentCircuit);

        if (romComponent == null) {
            sendFailResponse("ROM is not found");
            return;
        }

        HexModel contents;
        try {
            contents = getMemoryContents(romComponent.getFactory(), currentCircuitState.getInstanceState(romComponent));
        } catch (NoSuchMethodException | IllegalAccessException | InvocationTargetException e) {
            throw new RuntimeException(e);
        }

        if (message.bytes.length - 1 > contents.getLastOffset()) {
            sendFailResponse("Invalid memory range");
            return;
        }

        contents.set(0, message.bytes);

        sendResponse(new ActionResponse(MessageActions.LOAD));
    }

    private void handleSetMemoryMessage(SetMemoryMessage message) {
        System.out.printf("Store %d at %d\n", message.value, message.offset);

        Project project = DebuggerComponent.getSimulationTicker().getProject();
        Circuit currentCircuit = DebuggerComponent.getDebuggerCircuit();
        CircuitState currentCircuitState = project.getCircuitState(currentCircuit);

        if (ramComponent == null) {
            sendFailResponse("RAM is not found");
            return;
        }

        HexModel contents;
        try {
            contents = getMemoryContents(ramComponent.getFactory(), currentCircuitState.getInstanceState(ramComponent));
        } catch (NoSuchMethodException | IllegalAccessException | InvocationTargetException e) {
            throw new RuntimeException(e);
        }

        if (message.offset > contents.getLastOffset()) {
            sendFailResponse("Invalid memory range");
            return;
        }

        contents.set(message.offset, message.value);

        sendResponse(new ActionResponse(MessageActions.SET_MEMORY));
    }

    private void handleGetTunnelMessage(GetTunnelMessage message) {
        System.out.println("Get tunnel " + message.name);

        Project project = DebuggerComponent.getSimulationTicker().getProject();
        Circuit currentCircuit = DebuggerComponent.getDebuggerCircuit();
        CircuitState currentCircuitState = project.getCircuitState(currentCircuit);

        Integer tunnelValue = TunnelAdapter.getTunnelValue(message.name, currentCircuit, currentCircuitState);

        if (tunnelValue == null) {
            sendFailResponse(String.format("Tunnel %s not found", message.name));
            return;
        }

        sendResponse(new GetTunnelResponse(tunnelValue));
    }
}
