package ru.miqqra;

import java.awt.event.MouseEvent;
import java.awt.event.MouseListener;
import java.io.IOException;
import java.io.StringReader;
import java.io.StringWriter;
import java.util.NoSuchElementException;
import java.util.StringTokenizer;
import java.util.WeakHashMap;
import java.awt.Window;
import javax.swing.JLabel;

import com.cburch.logisim.circuit.CircuitState;
import com.cburch.logisim.data.Attribute;
import com.cburch.logisim.data.AttributeSet;
import com.cburch.logisim.data.BitWidth;
import com.cburch.logisim.data.Value;
import com.cburch.logisim.gui.hex.HexFile;
import com.cburch.logisim.gui.hex.HexFrame;
import com.cburch.logisim.gui.main.Frame;
import com.cburch.logisim.instance.Instance;
import com.cburch.logisim.instance.InstanceState;
import com.cburch.logisim.instance.Port;
import com.cburch.logisim.proj.Project;

public class BankedROM extends BankedMem {
    public static Attribute<BankedMemContents> CONTENTS_ATTR = new ContentsAttribute();

    // The following is so that instance's MemListeners aren't freed by the
    // garbage collector until the instance itself is ready to be freed.
    private WeakHashMap<Instance, MemListener> memListeners;

    public BankedROM() {
        super("ROM", BankedStrings.getter("romComponent"), 0);
        setIconName("rom.gif");
        memListeners = new WeakHashMap<Instance, MemListener>();
    }

    public static final int ADDR = 1;
    public static final int DATA = 0;
    public static final int SEL = 2;
    public static final int BITS = 3;
    public static final int PORTS = 4;
    public static final int DATABITS = 16;
    public static final int ADDRBITS = 8;


    @Override
    void configurePorts(Instance instance) {
        Port[] ps = new Port[PORTS];
        ps[DATA] = new Port(0, 0, "inout", 16);
        ps[ADDR] = new Port(-140, 0, "input", 8);
        ps[SEL] = new Port(-90, 40, "input", 1);
        ps[BITS] = new Port(-50, 40, "input", 1);
        ps[DATA].setToolTip(BankedStrings.getter("memDataTip"));
        ps[ADDR].setToolTip(BankedStrings.getter("memAddrTip"));
        ps[SEL].setToolTip(BankedStrings.getter("memCSTip"));
        ps[BITS].setToolTip(BankedStrings.getter("bits"));
        instance.setPorts(ps);
    }

    @Override
    public AttributeSet createAttributeSet() {
        return new BankedRomAttributes();
    }

    @Override
    BankedMemState getState(Instance instance, CircuitState state) {
        BankedMemState ret = (BankedMemState) instance.getData(state);
        if (ret == null) {
            BankedMemContents contents = getMemContents(instance);
            ret = new BankedMemState(contents);
            instance.setData(state, ret);
        }
        return ret;
    }

    @Override
    BankedMemState getState(InstanceState state) {
        BankedMemState ret = (BankedMemState) state.getData();
        if (ret == null) {
            BankedMemContents contents = getMemContents(state.getInstance());
            ret = new BankedMemState(contents);
            state.setData(ret);
        }
        return ret;
    }

    @Override
    HexFrame getHexFrame(Project proj, Instance instance, CircuitState state) {
        return BankedRomAttributes.getHexFrame(getMemContents(instance), proj);
    }

    // TODO - maybe delete this method?
    BankedMemContents getMemContents(Instance instance) {
        return instance.getAttributeValue(CONTENTS_ATTR);
    }

    @Override
    public void propagate(InstanceState state) {
        BankedMemState myState = this.getState(state);
        Value addrValue = state.getPort(1);
        Value bits = state.getPort(3);
        boolean chipSelect = state.getPort(2) != Value.FALSE;

        //state.setPort(BITS, Value.createKnown(BitWidth.create(BankedMem.DEFAULT_BITS_SIZE), BankedMem.DEFAULT_BITS_VALUE), DELAY);

        if (!chipSelect) {
            myState.setCurrent(-1L);
            state.setPort(0, Value.createUnknown(BitWidth.create(16)), 10);
        } else {
            int addr = addrValue.toIntValue();
            if (addrValue.isFullyDefined() && addr >= 0) {
                if ((long) addr != myState.getCurrent()) {
                    myState.setCurrent((long) addr);
                    myState.scrollToShow((long) addr);
                }
                int val = 0;
                if (bits.toIntValue() == 1) {
                    if (addr % 2 == 0) {
                        int val1, val2;
                        val1 = myState.getContents().get(addr);
                        val2 = myState.getContents().get(addr + 1);
                        val2 = (val2 << 8);
                        val = val1 | val2;
                    }
                } else { //(bits.toIntValue() == 0) || (bits.toIntValue() == -1) // for future versions
                    val = myState.getContents().get((long) addr);
                }
                state.setPort(DATA, Value.createKnown(BitWidth.create(16), val), 10);
            }
        }
    }

    @Override
    protected void configureNewInstance(Instance instance) {
        super.configureNewInstance(instance);
        BankedMemContents contents = getMemContents(instance);
        MemListener listener = new MemListener(instance);
        memListeners.put(instance, listener);
        contents.addHexModelListener(listener);
    }

    private static class ContentsAttribute extends Attribute<BankedMemContents> {
        public ContentsAttribute() {
            super("contents", BankedStrings.getter("romContentsAttr"));
        }

        @Override
        public java.awt.Component getCellEditor(Window source, BankedMemContents value) {
            if (source instanceof Frame) {
                Project proj = ((Frame) source).getProject();
                BankedRomAttributes.register(value, proj);
            }
            ContentsCell ret = new ContentsCell(source, value);
            ret.mouseClicked(null);
            return ret;
        }

        @Override
        public String toDisplayString(BankedMemContents value) {
            return BankedStrings.get("romContentsValue");
        }

        @Override
        public String toStandardString(BankedMemContents state) {
            int addr = state.getLogLength();
            int data = state.getWidth();
            StringWriter ret = new StringWriter();
            ret.write("addr/data: " + addr + " " + data + "\n");
            try {
                HexFile.save(ret, state);
            } catch (IOException e) {
            }
            return ret.toString();
        }

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
    }

    private static class ContentsCell extends JLabel
            implements MouseListener {
        Window source;
        BankedMemContents contents;

        ContentsCell(Window source, BankedMemContents contents) {
            super(BankedStrings.get("romContentsValue"));
            this.source = source;
            this.contents = contents;
            addMouseListener(this);
        }

        public void mouseClicked(MouseEvent e) {
            if (contents == null) return;
            Project proj = source instanceof Frame ? ((Frame) source).getProject() : null;
            HexFrame frame = BankedRomAttributes.getHexFrame(contents, proj);
            frame.setVisible(true);
            frame.toFront();
        }

        public void mousePressed(MouseEvent e) {
        }

        public void mouseReleased(MouseEvent e) {
        }

        public void mouseEntered(MouseEvent e) {
        }

        public void mouseExited(MouseEvent e) {
        }
    }
}
