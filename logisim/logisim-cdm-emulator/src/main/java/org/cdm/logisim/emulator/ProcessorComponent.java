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

class ProcessorComponent extends InstanceFactory {
    private static final LocaleManager source = new LocaleManager("resources/logisim", "std");

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
    ProcessorComponent() {
        super("ProcessorComponent");

        //setOffsetBounds(Bounds.create(-30, -15, 30, 30));

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

    @Override
    public void paintInstance(InstancePainter painter) {
        Graphics g = painter.getGraphics();
        Bounds bds = painter.getBounds();
        painter.drawBounds();

        if (painter.getShowState()) {
            MemState state = getState(painter);
            state.paint(painter.getGraphics(), bds.getX(), bds.getY());
        } else {
            BitWidth addr = painter.getAttributeValue(ADDR_ATTR);
            int addrBits = addr.getWidth();
            int bytes = 1 << addrBits;
            String label;
            if (this instanceof BankedROM) {

                if (addrBits >= 30) {
                    label = StringUtil.format(get("romGigabyteLabel"), ""
                            + (bytes >>> 30));
                } else if (addrBits >= 20) {
                    label = StringUtil.format(get("romMegabyteLabel"), ""
                            + (bytes >> 20));
                } else if (addrBits >= 10) {
                    label = StringUtil.format(get("romKilobyteLabel"), ""
                            + (bytes >> 10));
                } else {
                    label = StringUtil.format(get("romByteLabel"), ""
                            + bytes);
                }
            } else {
                if (addrBits >= 30) {
                    label = StringUtil.format(get("ramGigabyteLabel"), ""
                            + (bytes >>> 30));
                } else if (addrBits >= 20) {
                    label = StringUtil.format(get("ramMegabyteLabel"), ""
                            + (bytes >> 20));
                } else if (addrBits >= 10) {
                    label = StringUtil.format(get("ramKilobyteLabel"), ""
                            + (bytes >> 10));
                } else {
                    label = StringUtil.format(get("ramByteLabel"), ""
                            + bytes);
                }
            }
            GraphicsUtil.drawCenteredText(g, label, bds.getX() + bds.getWidth()
                    / 2, bds.getY() + bds.getHeight() / 2);
        }

        // draw input and output ports
        painter.drawPort(DATA, BankedStrings.get("ramDataLabel"), Direction.WEST);
        painter.drawPort(ADDR, BankedStrings.get("ramAddrLabel"), Direction.EAST);
        g.setColor(Color.GRAY);
        painter.drawPort(CS, BankedStrings.get("ramCSLabel"), Direction.SOUTH);

        if (this instanceof BankedROM) {
            painter.drawPort(BankedROM.BITS, BankedStrings.get("bit"), Direction.SOUTH);
        } else if (this instanceof BankedRAM) {
            painter.drawPort(BankedRAM.BITS, BankedStrings.get("bit"), Direction.SOUTH);
        }

    }

    @Override
    public void propagate(InstanceState state) {
        ProcessorClockState data = (ProcessorClockState) state.getData();
        if (data == null) {
            data = new ProcessorClockState();
            state.setData(data);
        }

        Object irqTriggerType = state.getAttributeValue(StdAttr.TRIGGER);
        boolean irqTriggered = data.updateClock(state.getPort(7), irqTriggerType, Processor.ClockType.IRQ);

        Object excTriggerType = state.getAttributeValue(StdAttr.TRIGGER);
        boolean excTriggered = data.updateClock(state.getPort(9), excTriggerType, Processor.ClockType.EXC);

        Object clkTriggerType = state.getAttributeValue(StdAttr.TRIGGER);
        boolean clkTriggered = data.updateClock(state.getPort(10), clkTriggerType, Processor.ClockType.CLK);


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
}
