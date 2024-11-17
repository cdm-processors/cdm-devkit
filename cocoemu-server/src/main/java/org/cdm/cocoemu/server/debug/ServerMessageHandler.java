package org.cdm.cocoemu.server.debug;

import org.cdm.cocoemu.components.processors.cdm16e.Cdm16e;
import org.cdm.cocoemu.server.app.EmulatorThread;
import org.cdm.debug.MessageHandler;
import org.cdm.debug.dto.*;
import org.cdm.debug.runtime.ProcessorState;
import org.cdm.debug.runtime.StopConditions;

import java.util.*;

public class ServerMessageHandler extends MessageHandler {
    private final EmulatorThread emulatorThread;

    private final Map<Integer, List<Integer>> lineLocations = new HashMap<>();
    private final Map<Integer, List<Integer>> breakpoints = new HashMap<>();

    public ServerMessageHandler(EmulatorThread emulatorThread) {
        this.emulatorThread = emulatorThread;
    }

    private boolean tickPredicate(ProcessorState state, StopConditions stopConditions) {
        handleMessage(false);

        int ps = emulatorThread.getSystem().outputs.ps;
        int context = (ps >> 4) & 0xFF;

        List<Integer> currentBreakpoints = breakpoints.getOrDefault(context, Collections.emptyList());
        List<Integer> currentLineLocations = lineLocations.getOrDefault(context, Collections.emptyList());

        StopConditions chekedStopConditions =
                StopConditions.check(state, stopConditions, currentBreakpoints, currentLineLocations);

        return !emulatorThread.isExternalTicker() || state.isHalted()
                || chekedStopConditions.stopOnFetch()
                || chekedStopConditions.stopOnBreakpoint()
                || chekedStopConditions.stopOnLine()
                || chekedStopConditions.stopOnException();
    }

    public void runSimulation(StopConditions stopConditions) {
        if (emulatorThread.isExternalTicker()) {
            return;
        } else {
            emulatorThread.setExternalTicker(true);
        }

        ProcessorState processorState;
        do {
            emulatorThread.doFullCycle();
        } while (!tickPredicate(getProcessorState(), stopConditions));
        processorState = getProcessorState();

        int ps = emulatorThread.getSystem().outputs.ps;
        int context = (ps >> 4) & 0xFF;

        List<Integer> currentBreakpoints = breakpoints.getOrDefault(context, Collections.emptyList());
        List<Integer> currentLineLocations = lineLocations.getOrDefault(context, Collections.emptyList());

        StopConditions chekedStopConditions =
                StopConditions.check(processorState, stopConditions, currentBreakpoints, currentLineLocations);

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

        if (!emulatorThread.isExternalTicker()) {
            reason = DebugEvent.REASON_PAUSE;
        }

        emulatorThread.setExternalTicker(false);

        sendDebugEvent(reason);

        CoconutEmulatorApplication.requestUpdateMemoryViews();
    }

    public ProcessorState getProcessorState() {
        Cdm16e processor = emulatorThread.getSystem().cdm16e;

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
        return null;
    }

    @Override
    protected DebuggerResponse handleLineLocationsMessage(LineLocationsMessage lineLocationsMessage) {
        return null;
    }

    @Override
    protected DebuggerResponse handleStepMessage() {
        return null;
    }

    @Override
    protected DebuggerResponse handleRunMessage(RunMessage runMessage) {
        return null;
    }

    @Override
    protected DebuggerResponse handlePauseMessage() {
        return null;
    }

    @Override
    protected DebuggerResponse handleResetMessage() {
        return null;
    }

    @Override
    protected DebuggerResponse handleInitMessage(InitializationMessage initializationMessage) {
        lineLocations.clear;

    }

    @Override
    protected DebuggerResponse handleGetRegistersMessage() {
        return null;
    }

    @Override
    protected DebuggerResponse handleGetMemoryMessage(GetMemoryMessage getMemoryMessage) {
        return null;
    }

    @Override
    protected DebuggerResponse handlePathLoadMessage(PathLoadMessage pathLoadMessage) {
        return null;
    }

    @Override
    protected DebuggerResponse handleBytesLoadMessage(BytesLoadMessage bytesLoadMessage) {
        return null;
    }

    @Override
    protected DebuggerResponse handleSetMemoryMessage(SetMemoryMessage setMemoryMessage) {
        return null;
    }

    @Override
    protected DebuggerResponse handleGetTunnelMessage(GetTunnelMessage getTunnelMessage) {
        return null;
    }
}
