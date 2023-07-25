package org.cdm.logisim.memory;

import java.awt.event.WindowAdapter;
import java.awt.event.WindowEvent;
import java.io.IOException;
import java.io.StringReader;
import java.util.List;
import java.util.NoSuchElementException;
import java.util.StringTokenizer;

import com.cburch.logisim.circuit.CircuitState;
import com.cburch.logisim.data.Attribute;
import com.cburch.logisim.data.AttributeEvent;
import com.cburch.logisim.data.AttributeListener;
import com.cburch.logisim.data.AttributeSet;
import com.cburch.logisim.data.AttributeSets;
import com.cburch.logisim.data.BitWidth;
import com.cburch.logisim.data.Direction;
import com.cburch.logisim.data.Location;
import com.cburch.logisim.data.Value;
import com.cburch.logisim.gui.hex.HexFile;
import com.cburch.logisim.gui.hex.HexFrame;
import com.cburch.logisim.instance.Instance;
import com.cburch.logisim.instance.InstanceData;
import com.cburch.logisim.instance.InstanceLogger;
import com.cburch.logisim.instance.InstancePainter;
import com.cburch.logisim.instance.InstanceState;
import com.cburch.logisim.instance.Port;
import com.cburch.logisim.instance.StdAttr;
import com.cburch.logisim.proj.Project;

public class BankedRAM extends BankedMem {

    //todo ram memcontent attribute
    public static Attribute<BankedMemContents> CONTENTS_ATTR = new Attribute<BankedMemContents>
            ("contents", BankedStrings.getter("ramContentsAttr")) {
        @Override
        public BankedMemContents parse(String value) {
            int lineBreak = value.indexOf('\n');
            String first = lineBreak < 0 ? value : value.substring(0, lineBreak);
            String rest = lineBreak < 0 ? "" : value.substring(lineBreak + 1);
            StringTokenizer toks = new StringTokenizer(first);
            try {
                String header = toks.nextToken();
                if (!header.equals("addr/data:")) return null;
                int addr = Integer.parseInt(toks.nextToken());
                int data = Integer.parseInt(toks.nextToken());
                BankedMemContents ret = BankedMemContents.create(addr, data);
                HexFile.open(ret, new StringReader(rest));
                return ret;
            } catch (IOException e) {
                return null;
            } catch (NumberFormatException e) {
                return null;
            } catch (NoSuchElementException e) {
                return null;
            }
        }
    };

    /*
    static final AttributeOption HAS_IMAGE_FILE
            = new AttributeOption("with image file", BankedStrings.getter("ramImageFile"));
    static final AttributeOption NO_IMAGE_FILE
            = new AttributeOption("no image file", BankedStrings.getter("ramNoImageFile"));

    static final Attribute<AttributeOption> ATTR_IMG_FILE = Attributes.forOption("bus",
            BankedStrings.getter("ramBusAttr"),
            new AttributeOption[]{NO_IMAGE_FILE, HAS_IMAGE_FILE});
     */

    private static Attribute<?>[] ATTRIBUTES = {
            BankedMem.ADDR_ATTR, PATH_ATTRIBUTE, LOAD_FROM_IMAGE_FILE
    };
    private static Object[] DEFAULTS = {
            BitWidth.create(8), "", NO_IMAGE_FILE
    };



    private static final int OE = MEM_INPUTS + 0;
    private static final int CLR = MEM_INPUTS + 1;
    private static final int CLK = MEM_INPUTS + 2;
    private static final int WE = MEM_INPUTS + 3;
    private static final int DIN = MEM_INPUTS + 4;
    public static final int DATA = 0;
    public static final int ADDR = 1;
    public static final int SEL = 2;
    public static final int LD = 3;
    public static final int CLEAR = 4;
    public static final int CLOCK = 5;
    public static final int BITS = 6;

    private static Object[][] logOptions = new Object[9][];

    public BankedRAM() {
        super("RAM", BankedStrings.getter("ramComponent"), 3);
        setIconName("ram.gif");
        setInstanceLogger(Logger.class);
    }

    public BankedMemContents getMemContents(Instance instance) {
        return instance.getAttributeValue(CONTENTS_ATTR);
    }

    public List<List<Integer>> getPrettyContent(InstanceState state){
        return this.getState(state).getContents().getPrettyContent();
    }

    @Override
    protected void configureNewInstance(Instance instance) {
        super.configureNewInstance(instance);
        instance.addAttributeListener();
    }

    @Override
    protected void instanceAttributeChanged(Instance instance, Attribute<?> attr) {
        configurePorts(instance);
    }

    @Override
    void configurePorts(Instance instance) {
        int portCount = 7;
        Port[] ps = new Port[portCount];

        ps[DATA] = new Port(0, 0, "inout", BankedMem.DEFAULT_DATA_SIZE);
        ps[ADDR] = new Port(-140, 0, "inout", ADDR_ATTR);
        ps[SEL] = new Port(-90, 40, "input", 1);
        ps[LD] = new Port(-50, 40, "input", 1);
        ps[CLEAR] = new Port(-30, 40, "input", 1);
        ps[CLOCK] = new Port(-70, 40, "input", 1);
        ps[BITS] = new Port(-110, 40, "input", 1);

        ps[DATA].setToolTip(BankedStrings.getter("ramBusTip"));
        ps[ADDR].setToolTip(BankedStrings.getter("memAddrTip"));
        ps[SEL].setToolTip(BankedStrings.getter("memCSTip"));
        ps[LD].setToolTip(BankedStrings.getter("ramOETip"));
        ps[CLEAR].setToolTip(BankedStrings.getter("ramClrTip"));
        ps[CLOCK].setToolTip(BankedStrings.getter("ramClkTip"));
        ps[BITS].setToolTip(BankedStrings.getter("ramBits"));

        instance.setPorts(ps);
    }

    @Override
    public AttributeSet createAttributeSet() {
        return AttributeSets.fixedSet(ATTRIBUTES, DEFAULTS);
    }

    @Override
    public BankedMemState getState(InstanceState state) {
        BitWidth addrBits = state.getAttributeValue(ADDR_ATTR);
        BitWidth dataBits = BitWidth.create(8);

        BankedRamState myState = (BankedRamState) state.getData();
        if (myState == null) {
            BankedMemContents contents = BankedMemContents.create(addrBits.getWidth(), dataBits.getWidth());
            Instance instance = state.getInstance();
            myState = new BankedRamState(instance, contents, new MemListener(instance));
            state.setData(myState);
        } else {
            myState.setRam(state.getInstance());
        }
        return myState;
    }

    @Override
    public BankedMemState getState(Instance instance, CircuitState state) {
        BitWidth addrBits = instance.getAttributeValue(ADDR_ATTR);
        BitWidth dataBits = instance.getAttributeValue(DATA_ATTR);

        BankedRamState myState = (BankedRamState) instance.getData(state);
        if (myState == null) {
            BankedMemContents contents = BankedMemContents.create(addrBits.getWidth(), dataBits.getWidth());
            myState = new BankedRamState(instance, contents, new MemListener(instance));
            instance.setData(state, myState);
        } else {
            myState.setRam(instance);
        }
        return myState;
    }

    @Override
    HexFrame getHexFrame(Project proj, Instance instance, CircuitState circState) {
        BankedRamState state = (BankedRamState) getState(instance, circState);
        return state.getHexFrame(proj);
    }

    @Override
    public void propagate(InstanceState state) {
        BankedRamState myState = (BankedRamState) getState(state);
        //BitWidth dataBits = state.getAttributeValue(DATA_ATTR);
        //Object busVal = state.getAttributeValue(ATTR_BUS);
        // state.setPort(BITS, Value.createKnown(BitWidth.create(BankedMem.DEFAULT_BITS_SIZE), BankedMem.DEFAULT_BITS_VALUE), DELAY);
        Value addrValue = state.getPort(ADDR);
        Value bits = state.getPort(BITS);
        boolean chipSelect = state.getPort(CS) != Value.FALSE;
        boolean triggered = myState.setClock(state.getPort(CLK), StdAttr.TRIG_RISING);
        boolean outputEnabled = state.getPort(OE) != Value.FALSE;
        boolean shouldClear = state.getPort(CLR) == Value.TRUE;

        if (myState.isNewlyCreated()) {
            myState.markLoaded();
            autoLoadImage(state);
        }

        if (shouldClear) {
            myState.getContents().clear();
        }

        if (!chipSelect) {
            myState.setCurrent(-1);
            state.setPort(DATA, Value.createUnknown(BitWidth.create(DEFAULT_DATA_SIZE)), DELAY);
            return;
        }

        int addr = addrValue.toIntValue();
        if (!addrValue.isFullyDefined() || addr < 0)
            return;
        if (addr != myState.getCurrent()) {
            myState.setCurrent(addr);
            myState.scrollToShow(addr);
        }

        if (!shouldClear && triggered && !outputEnabled) {
            int data = state.getPort(DATA).toIntValue();
            if (bits.toIntValue() == 1) {
                int data1 = data & ((1 << 8) - 1);
                int data2 = (data & (((1 << 8) - 1) << 8)) >>> 8;
                myState.getContents().set(addr, data1);
                myState.getContents().set(addr + 1, data2);
            } else { // (bits.toIntValue() == 0) || (bits.toIntValue() == -1) //for future versions
                data = data & ((1 << 8) - 1);
                myState.getContents().set(addr, data);
            }
        }

        if (outputEnabled) {
            int val = 0;
            if (bits.toIntValue() == 1) {
                if (addr % 2 == 0) {
                    int val1, val2;
                    val1 = myState.getContents().get(addr);
                    val2 = myState.getContents().get(addr + 1);
                    val2 = (val2 << 8);
                    val = val1 | val2;
                }
            } else { // (bits.toIntValue() == 0) || (bits.toIntValue() == -1)  //for future versions
                val = myState.getContents().get((long) addr);
            }
            state.setPort(DATA, Value.createKnown(BitWidth.create(DEFAULT_DATA_SIZE), val), DELAY);
        } else {
            state.setPort(DATA, Value.createUnknown(BitWidth.create(DEFAULT_DATA_SIZE)), DELAY);
        }
    }

    @Override
    public void paintInstance(InstancePainter painter) {
        super.paintInstance(painter);
        painter.drawClock(CLK, Direction.NORTH);
        painter.drawPort(OE, BankedStrings.get("ramOELabel"), Direction.SOUTH);
        painter.drawPort(CLR, BankedStrings.get("ramClrLabel"), Direction.SOUTH);
    }

    private static class BankedRamState extends BankedMemState
            implements InstanceData, AttributeListener {
        private Instance parent;
        private MemListener listener;
        private HexFrame hexFrame = null;
        private BankedClockState clockState;

        BankedRamState(Instance parent, BankedMemContents contents, MemListener listener) {
            super(contents);
            this.parent = parent;
            this.listener = listener;
            this.clockState = new BankedClockState();
            if (parent != null) parent.getAttributeSet().addAttributeListener(this);
            contents.addHexModelListener(listener);
        }

        void setRam(Instance value) {
            if (parent == value) return;
            if (parent != null) parent.getAttributeSet().removeAttributeListener(this);
            parent = value;
            if (value != null) value.getAttributeSet().addAttributeListener(this);
        }

        @Override
        public BankedRamState clone() {
            BankedRamState ret = (BankedRamState) super.clone();
            ret.parent = null;
            ret.clockState = this.clockState.clone();
            ret.getContents().addHexModelListener(listener);
            return ret;
        }

        // Retrieves a HexFrame for editing within a separate window
        public HexFrame getHexFrame(Project proj) {
            if (hexFrame == null) {
                hexFrame = new HexFrame(proj, getContents());
                hexFrame.addWindowListener(new WindowAdapter() {
                    @Override
                    public void windowClosed(WindowEvent e) {
                        hexFrame = null;
                    }
                });
            }
            return hexFrame;
        }

        //
        // methods for accessing the write-enable data
        //
        public boolean setClock(Value newClock, Object trigger) {
            return clockState.updateClock(newClock, trigger);
        }

        public void attributeListChanged(AttributeEvent e) {
        }

        public void attributeValueChanged(AttributeEvent e) {
            AttributeSet attrs = e.getSource();
            BitWidth addrBits = attrs.getValue(BankedMem.ADDR_ATTR);
            //BitWidth dataBits = attrs.getValue(BankedMem.DATA_ATTR);
            //todo
            getContents().setDimensions(addrBits.getWidth(), 8);
        }
    }

    public static class Logger extends InstanceLogger {
        @Override
        public Object[] getLogOptions(InstanceState state) {
            int addrBits = state.getAttributeValue(ADDR_ATTR).getWidth();
            if (addrBits >= logOptions.length) addrBits = logOptions.length - 1;
            synchronized (logOptions) {
                Object[] ret = logOptions[addrBits];
                if (ret == null) {
                    ret = new Object[1 << addrBits];
                    logOptions[addrBits] = ret;
                    for (int i = 0; i < ret.length; i++) {
                        ret[i] = Integer.valueOf(i);
                    }
                }
                return ret;
            }
        }

        @Override
        public String getLogName(InstanceState state, Object option) {
            if (option instanceof Integer) {
                String disp = BankedStrings.get("ramComponent");
                Location loc = state.getInstance().getLocation();
                return disp + loc + "[" + option + "]";
            } else {
                return null;
            }
        }

        @Override
        public Value getLogValue(InstanceState state, Object option) {
            if (option instanceof Integer) {
                BankedMemState s = (BankedMemState) state.getData();
                int addr = ((Integer) option).intValue();
                return Value.createKnown(BitWidth.create(s.getDataBits()),
                        s.getContents().get(addr));
            } else {
                return Value.NIL;
            }
        }
    }
}

