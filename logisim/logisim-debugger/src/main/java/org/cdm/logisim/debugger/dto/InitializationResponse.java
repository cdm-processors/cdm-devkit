package org.cdm.logisim.debugger.dto;

import lombok.Builder;

import java.util.List;

@Builder
public class InitializationResponse extends DebuggerResponse {
    public final String action = MessageActions.INIT;

    boolean supportsExceptions;
    List<String> registerNames;
    List<Integer> registerSizes;
    int ramSize;
}
