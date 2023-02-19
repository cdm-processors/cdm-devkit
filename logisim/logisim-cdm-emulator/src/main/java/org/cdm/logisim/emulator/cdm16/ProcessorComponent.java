package org.cdm.logisim.emulator.cdm16;

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

public class ProcessorComponent extends InstanceFactory {
    private static final LocaleManager source = new LocaleManager("resources/logisim", "std");

    public ProcessorComponent() {
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
                new Port(0, 40, "input", 5), //intnumber
                new Port(0, 70, "input", 1), //exc
                new Port(20, 120, "input", 1), //clk
                new Port(0, 80, "input", 5), //excnumber
                new Port(0, 100, "input", 1), //hold
                new Port(50, 120, "output", 2), //halted (status)

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

        ps[DATA_IN].setToolTip(getter("in"));
        ps[DATA_OUT].setToolTip(getter("out"));
        ps[ADDRESS].setToolTip(getter("addr"));
        ps[MEM].setToolTip(getter("memory"));
        ps[DATA].setToolTip(getter("data/ins'"));
        ps[READ].setToolTip(getter("read/write'"));
        ps[WORD].setToolTip(getter("word"));
        ps[IRQ].setToolTip(getter("IRQ"));
        ps[INT_NUMBER].setToolTip(getter("int_vector"));
        ps[EXC].setToolTip(getter("EXC"));
        ps[CLK].setToolTip(getter("clk"));
        ps[EXC_NUMBER].setToolTip(getter("exc_vector"));
        ps[HOLD_WAIT].setToolTip(getter("hold"));
        ps[HALTED].setToolTip(getter("status"));
        ps[R0].setToolTip(getter("r0"));
        ps[R1].setToolTip(getter("r1"));
        ps[R2].setToolTip(getter("r2"));
        ps[R3].setToolTip(getter("r3"));
        ps[R4].setToolTip(getter("r4"));
        ps[R5].setToolTip(getter("r5"));
        ps[R6].setToolTip(getter("r6"));
        ps[FP].setToolTip(getter("fp"));
        ps[PC].setToolTip(getter("pc"));
        ps[SP].setToolTip(getter("sp"));
        ps[PS].setToolTip(getter("ps"));
        ps[FETCH].setToolTip(getter("fetch"));
        ps[IAck].setToolTip(getter("IAck"));

        this.setPorts(ps);
    }

    @Override
    public void paintInstance(InstancePainter painter) {
        Graphics g = painter.getGraphics();
        Bounds bds = painter.getBounds();
        painter.drawBounds();
        painter.drawLabel();

        // DATA_IN, DATA_OUT, ADDRESS, MEM, DATA, READ, WORD, IRQ, INT_NUMBER, EXC, CLK , EXC_NUMBER , HOLD_WAIT , HALTED;
        painter.drawPort(DATA_IN, get("in"), Direction.WEST);
        painter.drawPort(DATA_OUT, get("out"), Direction.WEST);
        painter.drawPort(ADDRESS, get("addr"), Direction.WEST);
        painter.drawPort(MEM, get("memory"), Direction.WEST);
        painter.drawPort(DATA, get("data/ins'"), Direction.WEST);
        painter.drawPort(READ, get("read/write'"), Direction.WEST);
        painter.drawPort(WORD, get("word"), Direction.WEST);
        painter.drawPort(IRQ, get("IRQ"), Direction.EAST);
        painter.drawPort(INT_NUMBER, get("int_vector"), Direction.EAST);
        painter.drawPort(EXC, get("EXC"), Direction.EAST);
        painter.drawPort(CLK);
        painter.drawPort(EXC_NUMBER, get("exc_vector"), Direction.EAST);
        painter.drawPort(HOLD_WAIT, get("hold"), Direction.EAST);

        painter.drawPort(FETCH, get("fetch"), Direction.SOUTH);
        painter.drawPort(IAck, get("IAck"), Direction.EAST);
        painter.drawPort(HALTED, get("status"), Direction.SOUTH);

        painter.drawClock(CLK, Direction.NORTH);


        g.setFont(
                increaseFontSize(
                        makeBoldItalicFont(g.getFont()),
                        -2
                )
        );

        painter.drawPort(R0, get("r0"), Direction.NORTH);
        painter.drawPort(R1, get("...."), Direction.NORTH);
        painter.drawPort(R2, get("...."), Direction.NORTH);
        painter.drawPort(R3, get("...."), Direction.NORTH);
        painter.drawPort(R4, get("...."), Direction.NORTH);
        painter.drawPort(R5, get("...."), Direction.NORTH);
        painter.drawPort(R6, get("r6"), Direction.NORTH);
        painter.drawPort(FP, get("fp"), Direction.NORTH);
        painter.drawPort(PC, get("pc"), Direction.NORTH);
        painter.drawPort(SP, get("sp"), Direction.NORTH);
        painter.drawPort(PS, get("ps"), Direction.NORTH);

        g.setFont(
                increaseFontSize(
                        g.getFont(),
                        6
                )
        );

        GraphicsUtil.drawText(g, "CdM-16", bds.getX() + 65, bds.getY() + 85, 0, -1);
    }

    @Override
    public void propagate(InstanceState state) {
        ProcessorComponentData componentData = (ProcessorComponentData) state.getData();

        if (componentData == null) {
            componentData = new ProcessorComponentData();
            state.setData(componentData);
        }

        ProcessorClockState clockState = componentData.getProcessorClockState();

        Object irqTriggerType = state.getAttributeValue(StdAttr.TRIGGER);
        boolean irqTriggered = clockState.updateClock(state.getPort(IRQ), irqTriggerType, ProcessorClockState.ClockType.IRQ);

        Object excTriggerType = state.getAttributeValue(StdAttr.TRIGGER);
        boolean excTriggered = clockState.updateClock(state.getPort(EXC), excTriggerType, ProcessorClockState.ClockType.EXC);

        Object clkTriggerType = state.getAttributeValue(StdAttr.TRIGGER);
        boolean clkTriggered = clockState.updateClock(state.getPort(CLK), clkTriggerType, ProcessorClockState.ClockType.CLK);

        Processor processor = componentData.getProcessor();

        if (irqTriggered) {
            processor.externalInterrupt(state.getPort(INT_NUMBER).toIntValue());
        }
        if (excTriggered) {
            processor.externalException(state.getPort(EXC_NUMBER).toIntValue());
        }

        if (clkTriggered) {
            processor.clockRising();
        } else if (clockState.checkClockFalling(state.getPort(CLK))){
            processor.clockFalling();
        }

        processor.update();
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
                Font.BOLD+Font.ITALIC,
                currentFont.getSize()
        );
    }

    private static final int DATA_IN = 0;
    private static final int DATA_OUT = 1;
    private static final int ADDRESS = 2;
    private static final int MEM = 3;
    private static final int DATA = 4;
    private static final int READ = 5;
    private static final int WORD = 6;
    private static final int IRQ = 7;
    private static final int INT_NUMBER = 8;
    private static final int EXC = 9;
    private static final int CLK = 10;
    private static final int EXC_NUMBER = 11;
    private static final int HOLD_WAIT = 12;
    private static final int HALTED = 13;
    private static final int R0 = 14;
    private static final int R1 = 15;
    private static final int R2 = 16;
    private static final int R3 = 17;
    private static final int R4 = 18;
    private static final int R5 = 19;
    private static final int R6 = 20;
    private static final int FP = 21;
    private static final int PC = 22;
    private static final int SP = 23;
    private static final int PS = 24;
    private static final int FETCH = 25;
    private static final int IAck = 26;

}
