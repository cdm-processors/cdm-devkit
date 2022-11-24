package ru.miqqra;

/* Copyright (c) 2010, Carl Burch. License information is located in the
 * com.cburch.logisim.Main source code and at www.cburch.com/logisim/. */

import com.cburch.logisim.data.Value;
import com.cburch.logisim.instance.StdAttr;

class BankedClockState implements Cloneable {
    private Value lastClock;

    public BankedClockState() {
        lastClock = Value.FALSE;
    }

    @Override
    public BankedClockState clone() {
        try {
            return (BankedClockState) super.clone();
        } catch (CloneNotSupportedException e) { return null; }
    }

    public boolean updateClock(Value newClock, Object trigger) {
        Value oldClock = lastClock;
        lastClock = newClock;
        if (trigger == null || trigger == StdAttr.TRIG_RISING) {
            return oldClock == Value.FALSE && newClock == Value.TRUE;
        } else if (trigger == StdAttr.TRIG_FALLING) {
            return oldClock == Value.TRUE && newClock == Value.FALSE;
        } else if (trigger == StdAttr.TRIG_HIGH) {
            return newClock == Value.TRUE;
        } else if (trigger == StdAttr.TRIG_LOW) {
            return newClock == Value.FALSE;
        } else {
            return oldClock == Value.FALSE && newClock == Value.TRUE;
        }
    }
}

