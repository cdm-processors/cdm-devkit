package org.cdm.logisim.debugger.dto;

import lombok.Value;

@Value
public class FailResponse {
    public String status = "FAIL";
    public String message;
}
