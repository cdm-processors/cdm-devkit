package org.cdm.debug.dto;

public class FailResponse implements DebuggerResponse {
    public String status = "FAIL";
    public String message;

    public FailResponse(String message) {
        this.message = message;
    }
}
