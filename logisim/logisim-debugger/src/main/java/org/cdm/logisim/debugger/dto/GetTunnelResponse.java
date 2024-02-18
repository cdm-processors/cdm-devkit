package org.cdm.logisim.debugger.dto;

import lombok.Value;

@Value
public class GetTunnelResponse extends DebuggerResponse {
    public String action = MessageActions.GET_TUNNEL;
    public Integer value;
}
