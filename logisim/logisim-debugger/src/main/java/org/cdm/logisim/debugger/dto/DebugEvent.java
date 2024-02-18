package org.cdm.logisim.debugger.dto;

import lombok.Value;

@Value
public class DebugEvent extends DebuggerResponse {
    public static final String REASON_FETCH = "fetch";
    public static final String REASON_BREAKPOINT = "breakpoint";
    public static final String REASON_LINE = "line";
    public static final String REASON_EXCEPTION = "exception";
    public static final String REASON_HALT = "halt";
    public static final String REASON_PAUSE = "pause";
    public static final String REASON_UNKNOWN = "unknown";

    public String action = "debugEvent";

    String reason;
}
