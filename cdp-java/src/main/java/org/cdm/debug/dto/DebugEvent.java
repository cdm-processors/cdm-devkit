package org.cdm.debug.dto;

public class DebugEvent extends SuccessResponse {
    public static final String REASON_FETCH = "fetch";
    public static final String REASON_BREAKPOINT = "breakpoint";
    public static final String REASON_LINE = "line";
    public static final String REASON_EXCEPTION = "exception";
    public static final String REASON_HALT = "halt";
    public static final String REASON_PAUSE = "pause";
    public static final String REASON_UNKNOWN = "unknown";

    public String action = "debugEvent";

    String reason;

    public DebugEvent(String reason) {
        this.reason = reason;
    }
}
