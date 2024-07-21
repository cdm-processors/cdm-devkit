package org.cdm.logisim.emulator.cdm16;

import com.cburch.logisim.data.Bounds;
import com.cburch.logisim.data.Direction;
import com.cburch.logisim.instance.*;
import com.cburch.logisim.util.GraphicsUtil;
import com.cburch.logisim.util.LocaleManager;
import com.cburch.logisim.util.StringGetter;
import com.cburch.logisim.util.StringUtil;
import org.cdm.cocoemu.components.processors.cdm16.Cdm16;

import java.awt.*;

public class Cdm16ProcessorComponent extends InstanceFactory {
    private static final LocaleManager source = new LocaleManager("resources/logisim", "std");

    public Cdm16ProcessorComponent() {
        super("CdM-16");

        setOffsetBounds(Bounds.create(0, 0, 120, 120));

        Port[] ps = new Port[]{
                new Port(120, 110, "input", 16), //in
                new Port(120, 100, "output", 16), //out
                new Port(120, 80, "output", 16), //addr
                new Port(120, 40, "output", 1), //mem
                new Port(120, 30, "output", 1), //data
                new Port(120, 50, "output", 1), //read
                new Port(120, 60, "output", 1), //word
                new Port(0, 30, "input", 1), //irq
                new Port(0, 40, "input", 6), //intnumber
                new Port(0, 70, "input", 1), //exc
                new Port(20, 120, "input", 1), //clk
                new Port(0, 80, "input", 6), //excnumber
                new Port(0, 100, "input", 1), //hold
                new Port(50, 120, "output", 2), //status

                new Port(10, 0, "output", 16), //r0
                new Port(20, 0, "output", 16), //r1
                new Port(30, 0, "output", 16), //r2
                new Port(40, 0, "output", 16), //r3
                new Port(50, 0, "output", 16), //r4
                new Port(60, 0, "output", 16), //r5
                new Port(70, 0, "output", 16), //r6
                new Port(80, 0, "output", 16), //fp
                new Port(90, 0, "output", 16), //pc
                new Port(100, 0, "output", 16), //sp
                new Port(110, 0, "output", 16), //ps
                new Port(80, 120, "output", 1), //fetch
                new Port(0, 50, "output", 1)}; //IAck

        ps[Ports.DATA_IN].setToolTip(getter("in"));
        ps[Ports.DATA_OUT].setToolTip(getter("out"));
        ps[Ports.ADDRESS].setToolTip(getter("addr"));
        ps[Ports.MEM].setToolTip(getter("memory"));
        ps[Ports.DATA].setToolTip(getter("data/ins'"));
        ps[Ports.READ].setToolTip(getter("read/write'"));
        ps[Ports.WORD].setToolTip(getter("word"));
        ps[Ports.IRQ].setToolTip(getter("IRQ"));
        ps[Ports.INT_NUMBER].setToolTip(getter("int_vector"));
        ps[Ports.EXC].setToolTip(getter("EXC"));
        ps[Ports.CLK].setToolTip(getter("clk"));
        ps[Ports.EXC_NUMBER].setToolTip(getter("exc_vector"));
        ps[Ports.HOLD].setToolTip(getter("hold"));
        ps[Ports.STATUS].setToolTip(getter("status"));
        ps[Ports.R0].setToolTip(getter("r0"));
        ps[Ports.R1].setToolTip(getter("r1"));
        ps[Ports.R2].setToolTip(getter("r2"));
        ps[Ports.R3].setToolTip(getter("r3"));
        ps[Ports.R4].setToolTip(getter("r4"));
        ps[Ports.R5].setToolTip(getter("r5"));
        ps[Ports.R6].setToolTip(getter("r6"));
        ps[Ports.FP].setToolTip(getter("fp"));
        ps[Ports.PC].setToolTip(getter("pc"));
        ps[Ports.SP].setToolTip(getter("sp"));
        ps[Ports.PS].setToolTip(getter("ps"));
        ps[Ports.FETCH].setToolTip(getter("fetch"));
        ps[Ports.IAck].setToolTip(getter("IAck"));

        this.setPorts(ps);
    }

    @Override
    public void paintInstance(InstancePainter painter) {
        Graphics g = painter.getGraphics();
        Bounds bds = painter.getBounds();
        painter.drawBounds();
        painter.drawLabel();

        // DATA_IN, DATA_OUT, ADDRESS, MEM, DATA, READ, WORD, IRQ, INT_NUMBER, EXC, CLK , EXC_NUMBER , HOLD_WAIT , STATUS;
        painter.drawPort(Ports.DATA_IN, get("in"), Direction.WEST);
        painter.drawPort(Ports.DATA_OUT, get("out"), Direction.WEST);
        painter.drawPort(Ports.ADDRESS, get("addr"), Direction.WEST);
        painter.drawPort(Ports.MEM, get("memory"), Direction.WEST);
        painter.drawPort(Ports.DATA, get("data/ins'"), Direction.WEST);
        painter.drawPort(Ports.READ, get("read/write'"), Direction.WEST);
        painter.drawPort(Ports.WORD, get("word"), Direction.WEST);
        painter.drawPort(Ports.IRQ, get("IRQ"), Direction.EAST);
        painter.drawPort(Ports.INT_NUMBER, get("int_vector"), Direction.EAST);
        painter.drawPort(Ports.EXC, get("EXC"), Direction.EAST);
        painter.drawPort(Ports.CLK);
        painter.drawPort(Ports.EXC_NUMBER, get("exc_vector"), Direction.EAST);
        painter.drawPort(Ports.HOLD, get("hold"), Direction.EAST);

        painter.drawPort(Ports.FETCH, get("fetch"), Direction.SOUTH);
        painter.drawPort(Ports.IAck, get("IAck"), Direction.EAST);
        painter.drawPort(Ports.STATUS, get("status"), Direction.SOUTH);

        painter.drawClock(Ports.CLK, Direction.NORTH);


        g.setFont(
                increaseFontSize(
                        makeBoldItalicFont(g.getFont()),
                        -2
                )
        );

        painter.drawPort(Ports.R0, get("r0"), Direction.NORTH);
        painter.drawPort(Ports.R1, get("...."), Direction.NORTH);
        painter.drawPort(Ports.R2, get("...."), Direction.NORTH);
        painter.drawPort(Ports.R3, get("...."), Direction.NORTH);
        painter.drawPort(Ports.R4, get("...."), Direction.NORTH);
        painter.drawPort(Ports.R5, get("...."), Direction.NORTH);
        painter.drawPort(Ports.R6, get("r6"), Direction.NORTH);
        painter.drawPort(Ports.FP, get("fp"), Direction.NORTH);
        painter.drawPort(Ports.PC, get("pc"), Direction.NORTH);
        painter.drawPort(Ports.SP, get("sp"), Direction.NORTH);
        painter.drawPort(Ports.PS, get("ps"), Direction.NORTH);

        g.setFont(
                increaseFontSize(
                        g.getFont(),
                        6
                )
        );

        GraphicsUtil.drawText(g, "CdM-16", bds.getX() + 65, bds.getY() + 85, 0, -1);

        g.setFont(
                increaseFontSize(
                        g.getFont(),
                        -7
                )
        );

        GraphicsUtil.drawText(g, "Emulator", bds.getX() + 65, bds.getY() + 99, 0, -1);

    }

    @Override
    public void propagate(InstanceState state) {
        ProcessorComponentData componentData = (ProcessorComponentData) state.getData();

        if (componentData == null) {
            componentData = new ProcessorComponentData(new Cdm16());
            state.setData(componentData);
        }

        ProcessorClockState clockState = componentData.getProcessorClockState();

        Object irqTriggerType = state.getAttributeValue(StdAttr.TRIGGER);
        boolean irqTriggered = clockState.updateClock(state.getPort(Ports.IRQ), irqTriggerType, ProcessorClockState.ClockType.IRQ);

        Object excTriggerType = state.getAttributeValue(StdAttr.TRIGGER);
        boolean excTriggered = clockState.updateClock(state.getPort(Ports.EXC), excTriggerType, ProcessorClockState.ClockType.EXC);

        Object clkTriggerType = state.getAttributeValue(StdAttr.TRIGGER);
        boolean clkTriggered = clockState.updateClock(state.getPort(Ports.CLK), clkTriggerType, ProcessorClockState.ClockType.CLK);

        Cdm16 processor = componentData.getProcessor();

        Cdm16LogisimAdapter.transferStateToProcessor(state, processor);

        if (clkTriggered) {
            processor.clockRising();
        } else if (clockState.checkClockFalling(state.getPort(Ports.CLK))) {
            processor.clockFalling();
        }

        processor.update();

        Cdm16LogisimAdapter.transferStateFromProcessor(processor, state);
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

    public Font increaseFontSize(Font currentFont, int delta) {
        return new Font(
                currentFont.getName(),
                currentFont.getStyle(),
                currentFont.getSize() + delta
        );
    }

    public Font makeBoldItalicFont(Font currentFont) {
        return new Font(
                currentFont.getName(),
                Font.BOLD + Font.ITALIC,
                currentFont.getSize()
        );
    }
}
