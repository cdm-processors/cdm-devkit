package org.cdm.logisim.debugger.dto;

import lombok.Value;

import java.util.List;

@Value
public class GetRegistersResponse extends DebuggerResponse {
    public String action = MessageActions.GET_REGISTERS;
    public List<Integer> registers;
}
