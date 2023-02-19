package org.cdm.logisim.emulator;

import com.cburch.logisim.instance.InstanceState;

public interface GenericProcessor {
    void clockRising(InstanceState state);

    void clockFalling(InstanceState state);

    void update(InstanceState state);
}
