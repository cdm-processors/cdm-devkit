package org.cdm.debug.dto;

public class PingResponse extends SuccessResponse {
    public String action = MessageActions.PING;
    public String message;

    public PingResponse(String message) {
        this.message = message;
    }
}
