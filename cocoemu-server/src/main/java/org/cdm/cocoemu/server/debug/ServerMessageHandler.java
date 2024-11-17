package org.cdm.cocoemu.server.debug;

import org.cdm.cocoemu.components.processors.cdm16.Cdm16;
import org.cdm.cocoemu.server.app.Emulator;
import org.cdm.debug.MessageHandler;
import org.cdm.debug.dto.*;
import org.cdm.debug.runtime.ProcessorState;
import org.cdm.debug.runtime.StopConditions;

import java.util.*;

public class ServerMessageHandler extends MessageHandler {
    private final Emulator emulator;

    private final Map<Integer, List<Integer>> lineLocations = new HashMap<>();
    private final Map<Integer, List<Integer>> breakpoints = new HashMap<>();

    public ServerMessageHandler(Emulator emulator) {
        this.emulator = emulator;
    }

    private boolean tickPredicate(ProcessorState state, StopConditions stopConditions) {
        handleMessage(false);

        int ps = emulator.getSystem().outputs.ps;
        int context = (ps >> 4) & 0xFF;

        List<Integer> currentBreakpoints = breakpoints.getOrDefault(context, Collections.emptyList());
        List<Integer> currentLineLocations = lineLocations.getOrDefault(context, Collections.emptyList());

        StopConditions chekedStopConditions =
                StopConditions.check(state, ,stopConditions, currentBreakpoints, currentLineLocations);

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
        } while (!tickPredicate(getProcessorState(), stopConditions));
        processorState = getProcessorState();

        int ps = emulator.getSystem().outputs.ps;
        int context = (ps >> 4) & 0xFF;

        List<Integer> currentBreakpoints = breakpoints.getOrDefault(context, Collections.emptyList());
        List<Integer> currentLineLocations = lineLocations.getOrDefault(context, Collections.emptyList());

        StopConditions chekedStopConditions =
                StopConditions.check(processorState, ,stopConditions, currentBreakpoints, currentLineLocations);

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

        CoconutEmulatorApplication.requestUpdateMemoryViews();
    }

    public ProcessorState getProcessorState() {
        Cdm16 processor = emulator.getSystem();

        return new ProcessorState() {
            @Override
            public boolean isFetching() {
                return processor.outputs.fetch;
            }

            @Override
            public boolean isHalted() {
                return processor.outputs.status == 2;
            }

            @Override
            public int getProgramCounter() {
                return processor.outputs.pc;
            }

            @Override
            public List<Integer> getRegisters() {
                List<Integer> registers = new ArrayList<>();
                for (int registerValue : processor.outputs.gpRegisters) {
                    registers.add(registerValue);
                }
                registers.add(processor.outputs.pc);
                registers.add(processor.outputs.sp);
                registers.add(processor.outputs.ps);

                return registers;
            }

            @Override
            public boolean exceptionHappened() {
                return processor.exceptionHappened();
            }

            @Override
            public int getExceptionNumber() {
                return processor.exceptionNumber();
            }
        };
    }

    @Override
    protected DebuggerResponse handleBreakpointsMessage(BreakpointsMessage breakpointsMessage) {
        breakpoints.put(breakpointsMessage.context, breakpointsMessage.breakpoints);

        return new ActionResponse(MessageActions.SET_BREAKPOINTS);
    }

    @Override
    protected DebuggerResponse handleLineLocationsMessage(LineLocationsMessage lineLocationsMessage) {
        lineLocations.put(lineLocationsMessage.context, lineLocationsMessage.lineLocations);

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
        emulator.getSystem().reset();
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
