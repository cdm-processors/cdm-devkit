package org.cdm.logisim.emulator;

import com.cburch.logisim.data.Value;

public class ProcessorClockState {
    private Value lastClock = Value.FALSE;
    private Value currentClock = Value.FALSE;

    public void update(Value newClock) {
        lastClock = currentClock;
        currentClock = newClock;
    }

    public boolean isClockRising() {
        return lastClock.equals(Value.FALSE) && currentClock.equals(Value.TRUE);
    }

    public boolean isClockFalling() {
        return lastClock.equals(Value.TRUE) && currentClock.equals(Value.FALSE);
    }
}
