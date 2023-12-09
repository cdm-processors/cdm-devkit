package org.cdm.logisim.emulator.cdm16;

import com.cburch.logisim.data.Value;
import com.cburch.logisim.instance.InstanceData;
import com.cburch.logisim.instance.StdAttr;

public class ProcessorClockState {
    private Value irqLastClock;
    private Value excLastClock;
    private Value clkLastClock;
    private Value clkBeforeLastClock = Value.FALSE;

    public ProcessorClockState() {
        this.irqLastClock = Value.FALSE;
        this.excLastClock = Value.FALSE;
        this.clkLastClock = Value.FALSE;
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
                this.clkBeforeLastClock = this.clkLastClock;
                this.clkLastClock = newClock;
                break;
            }
        }

        if (trigger == null) {
            return oldClock == Value.FALSE && newClock == Value.TRUE;
        }

        if (trigger == StdAttr.TRIG_FALLING) {
            return oldClock == Value.TRUE && newClock == Value.FALSE;
        } else if (trigger == StdAttr.TRIG_HIGH) {
            return newClock == Value.TRUE;
        } else if (trigger == StdAttr.TRIG_LOW) {
            return newClock == Value.FALSE;
        } else {
            return oldClock == Value.FALSE && newClock == Value.TRUE;
        }
    }

    public boolean checkClockFalling(Value newClock) {
        return clkBeforeLastClock == Value.TRUE && newClock == Value.FALSE;
    }

    public enum ClockType {
        EXC, CLK, IRQ
    }
}