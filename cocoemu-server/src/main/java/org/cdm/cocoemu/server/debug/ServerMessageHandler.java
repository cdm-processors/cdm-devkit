package org.cdm.cocoemu.server.debug;

import org.cdm.cocoemu.components.memory.Memory;
import org.cdm.cocoemu.core.image.Image;
import org.cdm.cocoemu.core.image.ImageLoader;
import org.cdm.cocoemu.server.adapters.SystemAdapter;
import org.cdm.debug.MessageHandler;
import org.cdm.debug.dto.*;
import org.cdm.debug.runtime.ProcessorInfo;
import org.cdm.debug.runtime.ProcessorState;
import org.cdm.debug.runtime.StopConditions;

import java.util.ArrayList;
import java.util.List;

public class ServerMessageHandler extends MessageHandler {
    private DebugEnvironment debugEnvironment;

    private List<Integer> lineLocations = new ArrayList<>();
    private List<Integer> breakpoints = new ArrayList<>();

    private boolean tickPredicate(ProcessorState state, ProcessorInfo info, StopConditions stopConditions) {
        handleMessage(false);

        StopConditions chekedStopConditions =
                StopConditions.check(state, info, stopConditions, breakpoints, lineLocations);

        return state.isHalted()
                || chekedStopConditions.stopOnFetch()
                || chekedStopConditions.stopOnBreakpoint()
                || chekedStopConditions.stopOnLine()
                || chekedStopConditions.stopOnException();
    }

    public void runSimulation(StopConditions stopConditions) {
        SystemAdapter adapter = debugEnvironment.getSystemAdapter();

        ProcessorState processorState;
        do {
            debugEnvironment.getSystem().clockRising();
            debugEnvironment.getSystem().clockFalling();
            debugEnvironment.getSystem().update();
        } while (!tickPredicate(adapter.getProcessorState(), adapter.getProcessorInfo(), stopConditions));

        StopConditions chekedStopConditions =
                StopConditions.check(processorState = adapter.getProcessorState(), adapter.getProcessorInfo(), stopConditions, breakpoints, lineLocations);

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

        if (processorState.isHalted()) {
            reason = DebugEvent.REASON_HALT;
        }

        sendDebugEvent(reason);
    }

    @Override
    protected DebuggerResponse handleBreakpointsMessage(BreakpointsMessage breakpointsMessage) {
        breakpoints = breakpointsMessage.breakpoints;

        return new ActionResponse(MessageActions.SET_BREAKPOINTS);
    }

    @Override
    protected DebuggerResponse handleLineLocationsMessage(LineLocationsMessage lineLocationsMessage) {
        lineLocations = lineLocationsMessage.lineLocations;

        return new ActionResponse(MessageActions.SET_LINE_LOCATIONS);
    }

    @Override
    protected DebuggerResponse handleStepMessage() {
        runSimulation(new StopConditions().all());

        return new ActionResponse(MessageActions.STEP);
    }

    @Override
    protected DebuggerResponse handleRunMessage(RunMessage runMessage) {
        runSimulation(StopConditions.fromStrings(runMessage.stopConditions));

        return new ActionResponse(MessageActions.RUN);
    }

    @Override
    protected DebuggerResponse handlePauseMessage() {
        return new FailResponse("Pause request is not implemented");
    }

    @Override
    protected DebuggerResponse handleResetMessage() {
        debugEnvironment.getSystemAdapter().resetSystem();
        debugEnvironment.getSystem().update();

        return new ActionResponse(MessageActions.RESET);
    }

    @Override
    protected DebuggerResponse handleInitMessage(InitializationMessage initializationMessage) {
        lineLocations.clear();
        breakpoints.clear();

        DebugEnvironment environment = DebugEnvironmentFactory.getDebugEnvironment(
                initializationMessage.target,
                initializationMessage.memoryConfiguration
        );
        if (environment == null) {
            return new FailResponse(String.format(
                    "Can't create debug environment with processor %s and memory configuration %s",
                    initializationMessage.target,
                    initializationMessage.memoryConfiguration
            ));
        }
        this.debugEnvironment = environment;

        ProcessorInfo processorInfo = debugEnvironment.getSystemAdapter().getProcessorInfo();

        return new InitializationResponse(
                processorInfo.supportsExceptions(),
                processorInfo.getRegisterNames(),
                processorInfo.getRegisterSizes(),
                processorInfo.getMemorySize()
        );
    }

    @Override
    protected DebuggerResponse handleGetRegistersMessage() {
        return new GetRegistersResponse(debugEnvironment.getSystemAdapter().getProcessorState().getRegisters());
    }

    @Override
    protected DebuggerResponse handleGetMemoryMessage(GetMemoryMessage getMemoryMessage) {
        return new GetMemoryResponse(debugEnvironment.getSystemAdapter().getRam().getImage().getValues());
    }

    @Override
    protected DebuggerResponse handlePathLoadMessage(PathLoadMessage pathLoadMessage) {
        Image i;
        try {
            i = ImageLoader.loadFromFile(pathLoadMessage.path);
        } catch (Exception e) {
            return new FailResponse(e.toString());
        }
        Memory rom = debugEnvironment.getSystemAdapter().getRom();
        i.pad(rom.size(), 0);

        rom.getBuffer().clear();
        rom.getBuffer().put(i.getBytes(), 0, rom.size());
        rom.getBuffer().flip();

        return new ActionResponse(MessageActions.LOAD);
    }

    @Override
    protected DebuggerResponse handleBytesLoadMessage(BytesLoadMessage bytesLoadMessage) {
        return new FailResponse("BytesLoad request is not implemented");
    }

    @Override
    protected DebuggerResponse handleSetMemoryMessage(SetMemoryMessage setMemoryMessage) {
        return new FailResponse("SetMemory request is not implemented");
    }

    @Override
    protected DebuggerResponse handleGetTunnelMessage(GetTunnelMessage getTunnelMessage) {
        return new FailResponse("GetTunnel request is not implemented");
    }
}
