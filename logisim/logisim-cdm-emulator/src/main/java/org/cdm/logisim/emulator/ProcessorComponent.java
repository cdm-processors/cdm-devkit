package org.cdm.logisim.emulator;

import com.cburch.logisim.data.Bounds;
import com.cburch.logisim.data.Direction;
import com.cburch.logisim.instance.InstanceFactory;
import com.cburch.logisim.instance.InstancePainter;
import com.cburch.logisim.instance.InstanceState;
import com.cburch.logisim.instance.Port;
import com.cburch.logisim.instance.StdAttr;
import com.cburch.logisim.util.LocaleManager;
import com.cburch.logisim.util.StringGetter;
import com.cburch.logisim.util.StringUtil;

class ProcessorComponent extends InstanceFactory {
    Processor processor;

    static final int DATA_IN = 0;
    static final int DATA_OUT = 1;
    static final int ADDRESS = 2;
    static final int MEM = 3;
    static final int DATA = 4;
    static final int READ = 5;
    static final int WORD = 6;
    static final int IRQ = 7;
    static final int INT_NUMBER = 8;
    static final int EXC = 9;
    static final int CLK = 10;
    static final int EXC_NUMBER = 11;
    static final int HOLD_WAIT = 12;
    static final int HALTED = 13;

    private static final LocaleManager source = new LocaleManager("resources/logisim", "std");

    ProcessorComponent() {
        super("ProcessorComponent");

        setOffsetBounds(Bounds.create(0, 0, 120, 120));

        processor = null;
        Port[] ps = new Port[]{
                new Port(120, 110, "input", 16),
                new Port(120, 100, "output", 16),
                new Port(120, 80, "output", 16),
                new Port(120, 40, "output", 1),
                new Port(120, 30, "output", 1),
                new Port(120, 50, "output", 1),
                new Port(120, 60, "output", 1),
                new Port(0, 30, "input", 1),
                new Port(0, 40, "input", 5),
                new Port(0, 70, "input", 1),
                new Port(20, 120, "input", 5),
                new Port(0, 80, "input", 1),
                new Port(0, 100, "input", 1),
                new Port(50, 120, "output", 1)};

        ps[DATA_IN].setToolTip(getter("dataIn"));
        ps[DATA_OUT].setToolTip(getter("dataOut"));
        ps[ADDRESS].setToolTip(getter("address"));
        ps[MEM].setToolTip(getter("mem"));
        ps[DATA].setToolTip(getter("data"));
        ps[READ].setToolTip(getter("read"));
        ps[WORD].setToolTip(getter("word"));
        ps[IRQ].setToolTip(getter("irq"));
        ps[INT_NUMBER].setToolTip(getter("intNumber"));
        ps[EXC].setToolTip(getter("exc"));
        ps[CLK].setToolTip(getter("clk"));
        ps[EXC_NUMBER].setToolTip(getter("excNumber"));
        ps[HOLD_WAIT].setToolTip(getter("hold/wait"));
        ps[HALTED].setToolTip(getter("halted"));
        this.setPorts(ps);
    }

    @Override
    public void paintInstance(InstancePainter painter) {
        painter.drawBounds();
        painter.drawLabel();

        // DATA_IN, DATA_OUT, ADDRESS, MEM, DATA, READ, WORD, IRQ, INT_NUMBER, EXC, CLK , EXC_NUMBER , HOLD_WAIT , HALTED;
        painter.drawPort(DATA_IN, get("dataIn"), Direction.EAST);
        painter.drawPort(DATA_OUT, get("dataOut"), Direction.EAST);
        painter.drawPort(ADDRESS, get("address"), Direction.EAST);
        painter.drawPort(MEM, get("mem"), Direction.EAST);
        painter.drawPort(DATA, get("data"), Direction.EAST);
        painter.drawPort(READ, get("read"), Direction.EAST);
        painter.drawPort(WORD, get("word"), Direction.EAST);
        painter.drawPort(IRQ, get("irq"), Direction.WEST);
        painter.drawPort(INT_NUMBER, get("intNumber"), Direction.WEST);
        painter.drawPort(EXC, get("exc"), Direction.WEST);
        painter.drawPort(CLK, get("clk"), Direction.SOUTH);
        painter.drawPort(EXC_NUMBER, get("excNumber"), Direction.WEST);
        painter.drawPort(HOLD_WAIT, get("hold/wait"), Direction.WEST);
        painter.drawPort(HALTED, get("halted"), Direction.SOUTH);


        /*
        g.setColor(Color.GRAY);
        painter.drawPort(3, "0", Direction.SOUTH);
        painter.drawPort(4, Strings.get("memEnableLabel"), Direction.EAST);
        g.setColor(Color.BLACK);
        painter.drawClock(2, Direction.NORTH);
        if (b == null) {
            GraphicsUtil.drawText(g, a, bds.getX() + 15, bds.getY() + 4, 0, -1);
        } else {
            GraphicsUtil.drawText(g, a, bds.getX() + 15, bds.getY() + 3, 0, -1);
            GraphicsUtil.drawText(g, b, bds.getX() + 15, bds.getY() + 15, 0, -1);
        }

        if (this instanceof BankedROM) {
            painter.drawPort(BankedROM.BITS, BankedStrings.get("bit"), Direction.SOUTH);
        } else if (this instanceof BankedRAM) {
            painter.drawPort(BankedRAM.BITS, BankedStrings.get("bit"), Direction.SOUTH);
        }

         */

    }

    @Override
    public void propagate(InstanceState state) {
        Processor processor = new Processor(this);
        ProcessorClockState data = (ProcessorClockState) state.getData();
        if (data == null) {
            data = new ProcessorClockState();
            state.setData(data);
        }

        Object irqTriggerType = state.getAttributeValue(StdAttr.TRIGGER);
        boolean irqTriggered = data.updateClock(state.getPort(7), irqTriggerType, ProcessorClockState.ClockType.IRQ);

        Object excTriggerType = state.getAttributeValue(StdAttr.TRIGGER);
        boolean excTriggered = data.updateClock(state.getPort(9), excTriggerType, ProcessorClockState.ClockType.EXC);

        Object clkTriggerType = state.getAttributeValue(StdAttr.TRIGGER);
        boolean clkTriggered = data.updateClock(state.getPort(10), clkTriggerType, ProcessorClockState.ClockType.CLK);


        if (irqTriggered) {
            Processor.externalInterrupt(state.getPort(8).toIntValue());
        }
        if (excTriggered) {
            Processor.externalException(state.getPort(11).toIntValue());
        }
        if (clkTriggered) {
            Processor.clockRising();
        } else {
            Processor.clockFalling();
        }

        Processor.update();
    }

    public static StringGetter getter(String key) {
        return source.getter(key);
    }

    public static String get(String key) {
        return source.get(key);
    }

    public static String get(String key, String arg0) {
        return StringUtil.format(source.get(key), arg0);
    }

    public static String get(String key, String arg0, String arg1) {
        return StringUtil.format(source.get(key), arg0, arg1);
    }
}
