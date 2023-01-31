package org.cdm.logisim.emulator;

import com.cburch.logisim.data.BitWidth;
import com.cburch.logisim.data.Bounds;
import com.cburch.logisim.data.Direction;
import com.cburch.logisim.instance.InstanceFactory;
import com.cburch.logisim.instance.InstancePainter;
import com.cburch.logisim.instance.InstanceState;
import com.cburch.logisim.instance.Port;
import com.cburch.logisim.instance.StdAttr;
import com.cburch.logisim.util.GraphicsUtil;
import com.cburch.logisim.util.LocaleManager;
import com.cburch.logisim.util.StringGetter;
import com.cburch.logisim.util.StringUtil;

import java.awt.*;

public class Processor {

    public Processor() {

    }

    public void externalInterrupt(int interruptNumber) {

    }

    public void externalException(int exceptionNumber) {

    }

    public void clockRising() {

    }

    public void clockFalling() {

    }

    public void update() {

    }

    public enum ClockType {
        EXC, CLK, IRQ
    }

}
