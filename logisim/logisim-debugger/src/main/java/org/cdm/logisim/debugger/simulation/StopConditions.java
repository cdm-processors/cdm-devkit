package org.cdm.logisim.debugger.simulation;

import org.cdm.logisim.debugger.DebuggerComponent;
import org.cdm.logisim.debugger.adapters.ProcessorState;
import org.cdm.logisim.debugger.dto.DebugEvent;

import java.util.List;

public class StopConditions {
    private boolean stopOnException = false;
    private boolean stopOnLine = false;
    private boolean stopOnBreakpoint = false;
    private boolean stopOnFetch = false;

    public StopConditions exception() {
        stopOnException = true;

        return this;
    }

    public StopConditions line() {
        stopOnLine = true;

        return this;
    }

    public StopConditions breakpoint() {
        stopOnBreakpoint = true;

        return this;
    }

    public StopConditions fetch() {
        stopOnFetch = true;

        return this;
    }

    public StopConditions all() {
        stopOnBreakpoint = true;
        stopOnLine = true;
        stopOnException = true;
        stopOnFetch = true;

        return this;
    }

    public boolean stopOnBreakpoint() {
        return stopOnBreakpoint;
    }

    public boolean stopOnLine() {
        return stopOnLine;
    }

    public boolean stopOnException() {
        return stopOnException;
    }

    public boolean stopOnFetch() {
        return stopOnFetch;
    }

    public static StopConditions fromStrings(List<String> strings) {
        StopConditions stopConditions = new StopConditions();

        stopConditions.stopOnFetch = strings.contains(DebugEvent.REASON_FETCH);
        stopConditions.stopOnLine = strings.contains(DebugEvent.REASON_LINE);
        stopConditions.stopOnBreakpoint = strings.contains(DebugEvent.REASON_BREAKPOINT);
        stopConditions.stopOnException = strings.contains(DebugEvent.REASON_EXCEPTION);

        return stopConditions;
    }

    public static StopConditions check(
            ProcessorState state,
            StopConditions stopConditions,
            List<Integer> breakpoints,
            List<Integer> lineLocations
    ) {
        StopConditions checkedStopConditions = new StopConditions();

        checkedStopConditions.stopOnFetch = state.isFetching() && stopConditions.stopOnFetch();

        checkedStopConditions.stopOnBreakpoint = state.isFetching() && stopConditions.stopOnBreakpoint()
                && breakpoints.contains(state.getProgramCounter());

        checkedStopConditions.stopOnLine = state.isFetching() && stopConditions.stopOnLine()
                && lineLocations.contains(state.getProgramCounter());

        if (DebuggerComponent.getProcessorAdapter().supportsExceptions()) {
            checkedStopConditions.stopOnException = state.isFetching() && stopConditions.stopOnException()
                    && state.exceptionHappened();
        } else {
            checkedStopConditions.stopOnException = false;
        }

        return checkedStopConditions;
    }
}
