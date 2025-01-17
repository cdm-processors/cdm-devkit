package org.cdm.debug.dto;

public class ActionResponse extends SuccessResponse {
    public String action;

    public ActionResponse(String action) {
        this.action = action;
    }
}
