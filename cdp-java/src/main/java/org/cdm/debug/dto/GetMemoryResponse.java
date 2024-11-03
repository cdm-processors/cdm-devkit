package org.cdm.debug.dto;

import java.util.List;

public class GetMemoryResponse extends SuccessResponse {
    public String action = MessageActions.GET_MEMORY;
    public List<Integer> bytes;

    public GetMemoryResponse(List<Integer> bytes) {
        this.bytes = bytes;
    }
}
