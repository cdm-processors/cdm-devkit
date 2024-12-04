package org.cdm.cocoemu.server.debug;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import org.cdm.cocoemu.server.adapter.Cdm16ServerAdapter;
import org.cdm.cocoemu.server.app.Emulator;
import org.cdm.debug.MessageHandler;
import org.cdm.debug.dto.*;
import org.cdm.debug.runtime.ProcessorInfo;
import org.cdm.debug.runtime.ProcessorState;
import org.cdm.debug.runtime.StopConditions;

public class ServerMessageHandler extends MessageHandler {
    private final Emulator emulator;

    private List<Integer> lineLocations = new ArrayList<>();
    private List<Integer> breakpoints = new ArrayList<>();

    public ServerMessageHandler(Emulator emulator) {
        this.emulator = emulator;
    }

    private boolean tickPredicate(ProcessorState state, ProcessorInfo info, StopConditions stopConditions) {
        handleMessage(false);

        int ps = emulator.getSystem().cdm16.outputs.ps;
        int context = (ps >> 4) & 0xFF;

        List<Integer> currentBreakpoints = breakpoints;
        List<Integer> currentLineLocations = lineLocations;

        StopConditions chekedStopConditions =
                StopConditions.check(state, info, stopConditions, currentBreakpoints, currentLineLocations);

        return state.isHalted()
                || chekedStopConditions.stopOnFetch()
                || chekedStopConditions.stopOnBreakpoint()
                || chekedStopConditions.stopOnLine()
                || chekedStopConditions.stopOnException();
    }

    public void runSimulation(StopConditions stopConditions) {

        ProcessorState processorState;
        do {
            emulator.doFullCycle();
        } while (!tickPredicate(getProcessorState(), new Cdm16ServerAdapter(), stopConditions));
        processorState = getProcessorState();

        int ps = emulator.getSystem().cdm16.outputs.ps;
        int context = (ps >> 4) & 0xFF;

        List<Integer> currentBreakpoints = breakpoints;
        List<Integer> currentLineLocations = lineLocations;

        StopConditions chekedStopConditions =
                StopConditions.check(processorState, new Cdm16ServerAdapter() ,stopConditions, currentBreakpoints, currentLineLocations);

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
        emulator.getSystem().cdm16.reset();
        /* Добавить DmaController */
        emulator.getSystem().update();
        return new ActionResponse(MessageActions.RESET);
    }

    @Override
    protected DebuggerResponse handleInitMessage(InitializationMessage initializationMessage) {
        lineLocations.clear();
        breakpoints.clear();

        return new InitializationResponse(true,
                Arrays.asList("r0", "r1", "r2", "r3", "r4", "r5", "r6", "fp", "pc", "sp", "ps"),
                Arrays.asList(16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16),
                1_048_576
        );
    }

    @Override
    protected DebuggerResponse handleGetRegistersMessage() {
        return new GetRegistersResponse(getProcessorState().getRegisters());
    }

    @Override
    protected DebuggerResponse handleGetMemoryMessage(GetMemoryMessage getMemoryMessage) {
        return new GetMemoryResponse(new ArrayList<>());
    }

    @Override
    protected DebuggerResponse handlePathLoadMessage(PathLoadMessage pathLoadMessage) {
        return null;
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
