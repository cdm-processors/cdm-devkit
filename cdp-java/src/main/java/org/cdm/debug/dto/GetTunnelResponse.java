package org.cdm.debug.dto;

public class GetTunnelResponse extends SuccessResponse {
    public String action = MessageActions.GET_TUNNEL;
    public Integer value;

    public GetTunnelResponse(Integer value) {
        this.value = value;
    }
}
