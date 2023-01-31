package org.cdm.logisim.emulator;

import com.cburch.logisim.data.Value;
import com.cburch.logisim.instance.InstanceData;
import com.cburch.logisim.instance.StdAttr;

public class ProcessorClockState implements Cloneable, InstanceData {
    private Value irqLastClock;
    private Value excLastClock;
    private Value clkLastClock;

    public ProcessorClockState() {
        this.irqLastClock = Value.FALSE;
        this.excLastClock = Value.FALSE;
        this.clkLastClock = Value.FALSE;
    }

    public ProcessorClockState clone() {
        try {
            return (ProcessorClockState) super.clone();
        } catch (CloneNotSupportedException var2) {
            return null;
        }
    }

    public boolean updateClock(Value newClock, Object trigger, ClockType type) {
        Value oldClock = null;
        switch (type) {
            case IRQ: {
                oldClock = this.irqLastClock;
                this.irqLastClock = newClock;
                break;
            }
            case EXC: {
                oldClock = this.excLastClock;
                this.excLastClock = newClock;
                break;
            }
            case CLK: {
                oldClock = this.clkLastClock;
                this.clkLastClock = newClock;
                break;
            }
        }
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

    public enum ClockType {
        EXC, CLK, IRQ
    }
}