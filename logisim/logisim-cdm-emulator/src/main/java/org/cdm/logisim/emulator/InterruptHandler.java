package org.cdm.logisim.emulator;

import com.cburch.logisim.instance.InstanceState;

public interface InterruptHandler {
    void externalInterrupt(InstanceState state, int interruptNumber);
}
