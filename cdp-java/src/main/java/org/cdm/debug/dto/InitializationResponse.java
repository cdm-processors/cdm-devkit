package org.cdm.debug.dto;

import java.util.List;

public class InitializationResponse extends SuccessResponse {
    public final String action = MessageActions.INIT;

    boolean supportsExceptions;
    List<String> registerNames;
    List<Integer> registerSizes;
    int ramSize;

    public InitializationResponse(boolean supportsExceptions, List<String> registerNames, List<Integer> registerSizes, int ramSize) {
        this.supportsExceptions = supportsExceptions;
        this.registerNames = registerNames;
        this.registerSizes = registerSizes;
        this.ramSize = ramSize;
    }
}
