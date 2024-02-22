package org.cdm.logisim.debugger.dto;

import lombok.Value;

@Value
public class GetExceptionMetadataResponse extends DebuggerResponse {
    public String action = MessageActions.GET_EXCEPTION_METADATA;

    public int exceptionNumber;
}
