package org.cdm.cocoemu.server.debug;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

import org.cdm.cocoemu.components.memory.Memory;
import org.cdm.cocoemu.core.Component;
import org.cdm.cocoemu.core.image.Image;
import org.cdm.cocoemu.core.image.ImageLoader;
import org.cdm.cocoemu.server.adapter.Factory;
import org.cdm.cocoemu.server.adapter.ProcessorAdapter;
import org.cdm.debug.MessageHandler;
import org.cdm.debug.dto.*;
import org.cdm.debug.runtime.ProcessorInfo;
import org.cdm.debug.runtime.ProcessorState;
import org.cdm.debug.runtime.StopConditions;

public class ServerMessageHandler extends MessageHandler {
    private Component processor;
    private ProcessorAdapter<?> adapter;
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

        ProcessorState processorState;
        do {
            processor.clockRising();
            processor.clockFalling();
            processor.update();
        } while (!tickPredicate(adapter.getProcessorState(), adapter, stopConditions));
//        processorState = adapter.getProcessorState();

        StopConditions chekedStopConditions =
                StopConditions.check(processorState = adapter.getProcessorState(), adapter ,stopConditions, breakpoints, lineLocations);

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
        return new ActionResponse(MessageActions.PAUSE);
    }

    @Override
    protected DebuggerResponse handleResetMessage() {
        processor.update();
        return new ActionResponse(MessageActions.RESET);
    }

    @Override
    protected DebuggerResponse handleInitMessage(InitializationMessage initializationMessage) {
        lineLocations.clear();
        breakpoints.clear();

        DebugEnvironment<?> environment = Factory.getDebugEnvironment(initializationMessage.target, initializationMessage.memoryConfiguration);
        if (environment == null) {
            return new FailResponse("No such system found");
        }
        this.processor = environment.getSystem();
        this.adapter = environment.getProcessorAdapter();

        return new InitializationResponse(true,
                Arrays.asList("r0", "r1", "r2", "r3", "r4", "r5", "r6", "fp", "pc", "sp", "ps"),
                Arrays.asList(16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16),
                1_048_576
        );
    }

    @Override
    protected DebuggerResponse handleGetRegistersMessage() {
        return new GetRegistersResponse(adapter.getProcessorState().getRegisters());
    }

    @Override
    protected DebuggerResponse handleGetMemoryMessage(GetMemoryMessage getMemoryMessage) {
        return new GetMemoryResponse(adapter.getBankedRam().getImage().getValues());
    }

    @Override
    protected DebuggerResponse handlePathLoadMessage(PathLoadMessage pathLoadMessage) {
        Image i;
        try {
            i = ImageLoader.loadFromFile(pathLoadMessage.path);
        } catch (Exception e) {
            return new FailResponse(e.toString());
        }
        Memory rom = adapter.getBankedRom();
        i.pad(rom.size(), 0);

        rom.getBuffer().clear();
        rom.getBuffer().put(i.getBytes(), 0, rom.size());
        rom.getBuffer().flip();

        return new ActionResponse(MessageActions.LOAD);
    }

    @Override
    protected DebuggerResponse handleBytesLoadMessage(BytesLoadMessage bytesLoadMessage) {
        return new ActionResponse(MessageActions.LOAD);
    }

    @Override
    protected DebuggerResponse handleSetMemoryMessage(SetMemoryMessage setMemoryMessage) {
        return new ActionResponse(MessageActions.SET_MEMORY);
    }

    @Override
    protected DebuggerResponse handleGetTunnelMessage(GetTunnelMessage getTunnelMessage) {
        return new GetTunnelResponse(0);
    }
}
