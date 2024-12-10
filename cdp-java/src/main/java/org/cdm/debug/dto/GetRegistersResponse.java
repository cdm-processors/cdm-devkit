package org.cdm.debug.dto;

import java.util.List;

public class GetRegistersResponse extends SuccessResponse {
    public String action = MessageActions.GET_REGISTERS;
    public List<Integer> registers;

    public GetRegistersResponse(List<Integer> registers) {
        this.registers = registers;
    }
}
