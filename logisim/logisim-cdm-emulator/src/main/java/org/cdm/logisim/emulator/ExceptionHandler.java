package org.cdm.logisim.emulator;

import com.cburch.logisim.instance.InstanceState;

public interface ExceptionHandler {
    void externalException(InstanceState state, int exceptionNumber);
}
