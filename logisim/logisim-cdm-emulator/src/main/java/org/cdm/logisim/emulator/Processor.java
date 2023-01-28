package org.cdm.logisim.emulator;

import com.cburch.logisim.instance.InstanceFactory;
import com.cburch.logisim.instance.InstancePainter;
import com.cburch.logisim.instance.InstanceState;
import com.cburch.logisim.instance.Port;
import com.cburch.logisim.instance.StdAttr;
import com.cburch.logisim.util.LocaleManager;
import com.cburch.logisim.util.StringGetter;

public class Processor extends InstanceFactory {
    private static final LocaleManager source = new LocaleManager("resources/logisim", "std");

    public static StringGetter getter(String key) {
        return source.getter(key);
    }
    public Processor() {
        super("Processor");
        Port[] ps = new Port[]{
                new Port(0, 0, "input", 16),
                new Port(10, 0, "output", 16),
                new Port(20, 0, "output", 16),
                new Port(30, 0, "output", 1),
                new Port(40, 0, "output", 1),
                new Port(50, 0, "output", 1),
                new Port(60, 0, "output", 1),
                new Port(70, 0, "input", 1),
                new Port(80, 0, "input", 5),
                new Port(90, 0, "input", 1),
                new Port(100, 0, "input", 5),
                new Port(110, 0, "input", 1),
                new Port(120, 0, "input", 1),
                new Port(120, 0, "output", 1)};

        ps[0].setToolTip(getter("dataIn"));
        ps[1].setToolTip(getter("dataOut"));
        ps[2].setToolTip(getter("address"));
        ps[3].setToolTip(getter("mem"));
        ps[4].setToolTip(getter("data"));
        ps[5].setToolTip(getter("read"));
        ps[6].setToolTip(getter("word"));
        ps[7].setToolTip(getter("irq"));
        ps[8].setToolTip(getter("intNumber"));
        ps[9].setToolTip(getter("exc"));
        ps[10].setToolTip(getter("clk"));
        ps[11].setToolTip(getter("excNumber"));
        ps[12].setToolTip(getter("hold/wait"));
        ps[13].setToolTip(getter("halted"));
        this.setPorts(ps);
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

    @Override
    public void paintInstance(InstancePainter instancePainter) {

    }

    @Override
    public void propagate(InstanceState state) {
        ProcessorClockState data = (ProcessorClockState) state.getData();
        if (data == null) {
            data = new ProcessorClockState();
            state.setData(data);
        }

        Object irqTriggerType = state.getAttributeValue(StdAttr.TRIGGER);
        boolean irqTriggered = data.updateClock(state.getPort(7), irqTriggerType, ClockType.IRQ);

        Object excTriggerType = state.getAttributeValue(StdAttr.TRIGGER);
        boolean excTriggered = data.updateClock(state.getPort(9), excTriggerType, ClockType.EXC);

        Object clkTriggerType = state.getAttributeValue(StdAttr.TRIGGER);
        boolean clkTriggered = data.updateClock(state.getPort(10), clkTriggerType, ClockType.CLK);


        if (irqTriggered){
            externalInterrupt(state.getPort(8).toIntValue());
        }
        if (excTriggered){
            externalException(state.getPort(11).toIntValue());
        }
        if (clkTriggered){
            clockRising();
        }
        else {
            clockFalling();
        }

        update();
    }

    public enum ClockType{
        IRQ, EXC, CLK
    }
}
