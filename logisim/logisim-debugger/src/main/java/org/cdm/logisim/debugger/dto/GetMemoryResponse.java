package org.cdm.logisim.debugger.dto;

import lombok.Value;

import java.util.List;

@Value
public class GetMemoryResponse extends DebuggerResponse {
    public String action = MessageActions.GET_MEMORY;
    public List<Integer> bytes;
}
