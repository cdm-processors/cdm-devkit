package org.cdm.logisim.debugger.dto;

import lombok.Value;

@Value
public class ActionResponse extends DebuggerResponse {
    public String action;
}
