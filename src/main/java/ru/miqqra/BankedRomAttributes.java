package ru.miqqra;

/* Copyright (c) 2010, Carl Burch. License information is located in the
 * com.cburch.logisim.Main source code and at www.cburch.com/logisim/. */

import java.util.Arrays;
import java.util.List;
import java.util.WeakHashMap;

import com.cburch.logisim.data.AbstractAttributeSet;
import com.cburch.logisim.data.Attribute;
import com.cburch.logisim.data.BitWidth;
import com.cburch.logisim.gui.hex.HexFrame;
import com.cburch.logisim.proj.Project;

class BankedRomAttributes extends AbstractAttributeSet {
    private static List<Attribute<?>> ATTRIBUTES = Arrays.asList(new Attribute<?>[]{
            BankedMem.ADDR_ATTR, BankedMem.DATA_ATTR, BankedROM.CONTENTS_ATTR
    });

    private static WeakHashMap<BankedMemContents, BankedRomContentsListener> listenerRegistry
            = new WeakHashMap<BankedMemContents, BankedRomContentsListener>();
    private static WeakHashMap<BankedMemContents, HexFrame> windowRegistry
            = new WeakHashMap<BankedMemContents, HexFrame>();

    static void register(BankedMemContents value, Project proj) {
        if (proj == null || listenerRegistry.containsKey(value)) return;
        BankedRomContentsListener l = new BankedRomContentsListener(proj);
        value.addHexModelListener(l);
        listenerRegistry.put(value, l);
    }

    static HexFrame getHexFrame(BankedMemContents value, Project proj) {
        synchronized (windowRegistry) {
            HexFrame ret = windowRegistry.get(value);
            if (ret == null) {
                ret = new HexFrame(proj, value);
                windowRegistry.put(value, ret);
            }
            return ret;
        }
    }

    private BitWidth addrBits = BitWidth.create(8);
    private BitWidth dataBits = BitWidth.create(8);
    private BankedMemContents contents;

    BankedRomAttributes() {
        contents = BankedMemContents.create(addrBits.getWidth(), dataBits.getWidth());
    }

    void setProject(Project proj) {
        register(contents, proj);
    }

    @Override
    protected void copyInto(AbstractAttributeSet dest) {
        BankedRomAttributes d = (BankedRomAttributes) dest;
        d.addrBits = addrBits;
        d.dataBits = dataBits;
        d.contents = contents.clone();
    }

    @Override
    public List<Attribute<?>> getAttributes() {
        return ATTRIBUTES;
    }

    @Override
    @SuppressWarnings("unchecked")
    public <V> V getValue(Attribute<V> attr) {
        if (attr == BankedMem.ADDR_ATTR) return (V) addrBits;
        if (attr == BankedMem.DATA_ATTR) return (V) dataBits;
        if (attr == BankedROM.CONTENTS_ATTR) return (V) contents;
        return null;
    }

    @Override
    public <V> void setValue(Attribute<V> attr, V value) {
        if (attr == BankedMem.ADDR_ATTR) {
            addrBits = (BitWidth) value;
            contents.setDimensions(addrBits.getWidth(), dataBits.getWidth());
        } else if (attr == BankedMem.DATA_ATTR) {
            dataBits = (BitWidth) value;
            contents.setDimensions(addrBits.getWidth(), dataBits.getWidth());
        } else if (attr == BankedROM.CONTENTS_ATTR) {
            contents = (BankedMemContents) value;
        }
        fireAttributeValueChanged(attr, value);
    }
}

