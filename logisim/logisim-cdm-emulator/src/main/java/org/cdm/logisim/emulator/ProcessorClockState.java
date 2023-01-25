package org.cdm.logisim.emulator;

import com.cburch.logisim.data.Value;
import com.cburch.logisim.instance.StdAttr;

class ProcessorClockState implements Cloneable {
    private Value lastClock;

    public ProcessorClockState() {
        this.lastClock = Value.FALSE;
    }

    public ProcessorClockState clone() {
        try {
            return (ProcessorClockState)super.clone();
        } catch (CloneNotSupportedException var2) {
            return null;
        }
    }

    public boolean updateClock(Value newClock, Object trigger) {
        Value oldClock = this.lastClock;
        this.lastClock = newClock;
        if (trigger != null && trigger != StdAttr.TRIG_RISING) {
            if (trigger == StdAttr.TRIG_FALLING) {
                return oldClock == Value.TRUE && newClock == Value.FALSE;
            } else if (trigger == StdAttr.TRIG_HIGH) {
                return newClock == Value.TRUE;
            } else if (trigger == StdAttr.TRIG_LOW) {
                return newClock == Value.FALSE;
            } else {
                return oldClock == Value.FALSE && newClock == Value.TRUE;
            }
        } else {
            return oldClock == Value.FALSE && newClock == Value.TRUE;
        }
    }
}

