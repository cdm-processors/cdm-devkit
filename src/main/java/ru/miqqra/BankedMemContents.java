package ru.miqqra;

/* Copyright (c) 2010, Carl Burch. License information is located in the
 * com.cburch.logisim.Main source code and at www.cburch.com/logisim/. */

import java.util.Arrays;

import com.cburch.hex.HexModel;
import com.cburch.hex.HexModelListener;
import com.cburch.logisim.util.EventSourceWeakSupport;

class BankedMemContents implements Cloneable, HexModel {
    private static final int PAGE_SIZE_BITS = 12;
    private static final int PAGE_SIZE = 1 << PAGE_SIZE_BITS;
    private static final int PAGE_MASK = PAGE_SIZE - 1;

    static BankedMemContents create(int addrBits, int width) {
        return new BankedMemContents(addrBits, width);
    }

    private EventSourceWeakSupport<HexModelListener> listeners = null;
    private int width;
    private int addrBits;
    private int mask;
    private BankedMemContentsSub.ContentsInterface[] pages;

    private BankedMemContents(int addrBits, int width) {
        listeners = null;
        setDimensions(addrBits, width);
    }

    //
    // HexModel methods
    //
    public void addHexModelListener(HexModelListener l) {
        if (listeners == null) listeners = new EventSourceWeakSupport<HexModelListener>();
        listeners.add(l);
    }

    public void removeHexModelListener(HexModelListener l) {
        if (listeners == null) return;
        listeners.add(l);
        if (listeners.isEmpty()) listeners = null;
    }

    private void fireMetainfoChanged() {
        if (listeners == null) return;
        boolean found = false;
        for (HexModelListener l : listeners) {
            found = true;
            l.metainfoChanged(this);
        }
        if (!found) listeners = null;
    }

    private void fireBytesChanged(long start, long numBytes,
                                  int[] oldValues) {
        if (listeners == null) return;
        boolean found = false;
        for (HexModelListener l : listeners) {
            found = true;
            l.bytesChanged(this, start, numBytes, oldValues);
        }
        if (!found) listeners = null;
    }

    //
    // other methods
    //
    @Override
    public BankedMemContents clone() {
        try {
            BankedMemContents ret = (BankedMemContents) super.clone();
            ret.listeners = null;
            ret.pages = new BankedMemContentsSub.ContentsInterface[this.pages.length];
            for (int i = 0; i < ret.pages.length; i++) {
                if (this.pages[i] != null) {
                    ret.pages[i] = this.pages[i].clone();
                }
            }
            return ret;
        } catch (CloneNotSupportedException ex) {
            return this;
        }
    }

    public int getLogLength() {
        return addrBits;
    }

    public int getWidth() {
        return width;
    }

    public int get(long addr) {
        int page = (int) (addr >>> PAGE_SIZE_BITS);
        int offs = (int) (addr & PAGE_MASK);
        if (page < 0 || page >= pages.length || pages[page] == null) return 0;
        return pages[page].get(offs) & mask;
    }

    public boolean isClear() {
        for (int i = 0; i < pages.length; i++) {
            BankedMemContentsSub.ContentsInterface page = pages[i];
            if (page != null) {
                for (int j = page.getLength() - 1; j >= 0; j--) {
                    if (page.get(j) != 0) return false;
                }
            }
        }
        return true;
    }

    public void set(long addr, int value) {
        int page = (int) (addr >>> PAGE_SIZE_BITS);
        int offs = (int) (addr & PAGE_MASK);
        int old = pages[page] == null ? 0 : pages[page].get(offs) & mask;
        int val = value & mask;
        if (old != val) {
            if (pages[page] == null) {
                pages[page] = BankedMemContentsSub.createContents(PAGE_SIZE, width);
            }
            pages[page].set(offs, val);
            fireBytesChanged(addr, 1, new int[]{old});
        }
    }

    public void set(long start, int[] values) {
        if (values.length == 0) return;

        int pageStart = (int) (start >>> PAGE_SIZE_BITS);
        int startOffs = (int) (start & PAGE_MASK);
        int pageEnd = (int) ((start + values.length - 1) >>> PAGE_SIZE_BITS);
        int endOffs = (int) ((start + values.length - 1) & PAGE_MASK);

        if (pageStart == pageEnd) {
            ensurePage(pageStart);
            BankedMemContentsSub.ContentsInterface page = pages[pageStart];
            if (!page.matches(values, startOffs, mask)) {
                int[] oldValues = page.get(startOffs, values.length);
                page.load(startOffs, values, mask);
                if (page.isClear()) pages[pageStart] = null;
                fireBytesChanged(start, values.length, oldValues);
            }
        } else {
            int nextOffs;
            if (startOffs == 0) {
                pageStart--;
                nextOffs = 0;
            } else {
                ensurePage(pageStart);
                int[] vals = new int[PAGE_SIZE - startOffs];
                System.arraycopy(values, 0, vals, 0, vals.length);
                BankedMemContentsSub.ContentsInterface page = pages[pageStart];
                if (!page.matches(vals, startOffs, mask)) {
                    int[] oldValues = page.get(startOffs, vals.length);
                    page.load(startOffs, vals, mask);
                    if (page.isClear()) pages[pageStart] = null;
                    fireBytesChanged(start, PAGE_SIZE - pageStart, oldValues);
                }
                nextOffs = vals.length;
            }
            int[] vals = new int[PAGE_SIZE];
            int offs = nextOffs;
            for (int i = pageStart + 1; i < pageEnd; i++, offs += PAGE_SIZE) {
                BankedMemContentsSub.ContentsInterface page = pages[i];
                if (page == null) {
                    boolean allZeroes = true;
                    for (int j = 0; j < PAGE_SIZE; j++) {
                        if ((values[offs + j] & mask) != 0) {
                            allZeroes = false;
                            break;
                        }
                    }
                    if (!allZeroes) {
                        page = BankedMemContentsSub.createContents(PAGE_SIZE, width);
                        pages[i] = page;
                    }
                }
                if (page != null) {
                    System.arraycopy(values, offs, vals, 0, PAGE_SIZE);
                    if (!page.matches(vals, startOffs, mask)) {
                        int[] oldValues = page.get(0, PAGE_SIZE);
                        page.load(0, vals, mask);
                        if (page.isClear()) pages[i] = null;
                        fireBytesChanged((long) i << PAGE_SIZE_BITS, PAGE_SIZE, oldValues);
                    }
                }
            }
            if (endOffs >= 0) {
                ensurePage(pageEnd);
                vals = new int[endOffs + 1];
                System.arraycopy(values, offs, vals, 0, endOffs + 1);
                BankedMemContentsSub.ContentsInterface page = pages[pageEnd];
                if (!page.matches(vals, startOffs, mask)) {
                    int[] oldValues = page.get(0, endOffs + 1);
                    page.load(0, vals, mask);
                    if (page.isClear()) pages[pageEnd] = null;
                    fireBytesChanged((long) pageEnd << PAGE_SIZE_BITS, endOffs + 1, oldValues);
                }
            }
        }
    }

    public void fill(long start, long len, int value) {
        if (len == 0) return;

        int pageStart = (int) (start >>> PAGE_SIZE_BITS);
        int startOffs = (int) (start & PAGE_MASK);
        int pageEnd = (int) ((start + len - 1) >>> PAGE_SIZE_BITS);
        int endOffs = (int) ((start + len - 1) & PAGE_MASK);
        value &= mask;

        if (pageStart == pageEnd) {
            ensurePage(pageStart);
            int[] vals = new int[(int) len];
            Arrays.fill(vals, value);
            BankedMemContentsSub.ContentsInterface page = pages[pageStart];
            if (!page.matches(vals, startOffs, mask)) {
                int[] oldValues = page.get(startOffs, (int) len);
                page.load(startOffs, vals, mask);
                if (value == 0 && page.isClear()) pages[pageStart] = null;
                fireBytesChanged(start, len, oldValues);
            }
        } else {
            if (startOffs == 0) {
                pageStart--;
            } else {
                if (value == 0 && pages[pageStart] == null) {
                    // nothing to do
                } else {
                    ensurePage(pageStart);
                    int[] vals = new int[PAGE_SIZE - startOffs];
                    Arrays.fill(vals, value);
                    BankedMemContentsSub.ContentsInterface page = pages[pageStart];
                    if (!page.matches(vals, startOffs, mask)) {
                        int[] oldValues = page.get(startOffs, vals.length);
                        page.load(startOffs, vals, mask);
                        if (value == 0 && page.isClear()) pages[pageStart] = null;
                        fireBytesChanged(start, PAGE_SIZE - pageStart, oldValues);
                    }
                }
            }
            if (value == 0) {
                for (int i = pageStart + 1; i < pageEnd; i++) {
                    if (pages[i] != null) clearPage(i);
                }
            } else {
                int[] vals = new int[PAGE_SIZE];
                Arrays.fill(vals, value);
                for (int i = pageStart + 1; i < pageEnd; i++) {
                    ensurePage(i);
                    BankedMemContentsSub.ContentsInterface page = pages[i];
                    if (!page.matches(vals, 0, mask)) {
                        int[] oldValues = page.get(0, PAGE_SIZE);
                        page.load(0, vals, mask);
                        fireBytesChanged((long) i << PAGE_SIZE_BITS, PAGE_SIZE, oldValues);
                    }
                }
            }
            if (endOffs >= 0) {
                BankedMemContentsSub.ContentsInterface page = pages[pageEnd];
                if (value == 0 && page == null) {
                    // nothing to do
                } else {
                    ensurePage(pageEnd);
                    int[] vals = new int[endOffs + 1];
                    Arrays.fill(vals, value);
                    if (!page.matches(vals, 0, mask)) {
                        int[] oldValues = page.get(0, endOffs + 1);
                        page.load(0, vals, mask);
                        if (value == 0 && page.isClear()) pages[pageEnd] = null;
                        fireBytesChanged((long) pageEnd << PAGE_SIZE_BITS, endOffs + 1, oldValues);
                    }
                }
            }
        }
    }

    public void clear() {
        for (int i = 0; i < pages.length; i++) {
            if (pages[i] != null) {
                if (pages[i] != null) clearPage(i);
            }
        }
    }

    private void clearPage(int index) {
        BankedMemContentsSub.ContentsInterface page = pages[index];
        int[] oldValues = new int[page.getLength()];
        boolean changed = false;
        for (int j = 0; j < oldValues.length; j++) {
            int val = page.get(j) & mask;
            oldValues[j] = val;
            if (val != 0) changed = true;
        }
        if (changed) {
            pages[index] = null;
            fireBytesChanged(index << PAGE_SIZE_BITS, oldValues.length, oldValues);
        }
    }

    public void setDimensions(int addrBits, int width) {
        if (addrBits == this.addrBits && width == this.width) return;
        this.addrBits = addrBits;
        this.width = width;
        this.mask = width == 32 ? 0xffffffff : ((1 << width) - 1);

        BankedMemContentsSub.ContentsInterface[] oldPages = pages;
        int pageCount;
        int pageLength;
        if (addrBits < PAGE_SIZE_BITS) {
            pageCount = 1;
            pageLength = 1 << addrBits;
        } else {
            pageCount = 1 << (addrBits - PAGE_SIZE_BITS);
            pageLength = PAGE_SIZE;
        }
        pages = new BankedMemContentsSub.ContentsInterface[pageCount];
        if (oldPages != null) {
            int n = Math.min(oldPages.length, pages.length);
            for (int i = 0; i < n; i++) {
                if (oldPages[i] != null) {
                    pages[i] = BankedMemContentsSub.createContents(pageLength, width);
                    int m = Math.max(oldPages[i].getLength(), pageLength);
                    for (int j = 0; j < m; j++) {
                        pages[i].set(j, oldPages[i].get(j));
                    }
                }
            }
        }
        if (pageCount == 0 && pages[0] == null) {
            pages[0] = BankedMemContentsSub.createContents(pageLength, width);
        }
        fireMetainfoChanged();
    }

    public long getFirstOffset() {
        return 0;
    }

    public long getLastOffset() {
        return (1L << addrBits) - 1;
    }

    public int getValueWidth() {
        return width;
    }

    private void ensurePage(int index) {
        if (pages[index] == null) {
            pages[index] = BankedMemContentsSub.createContents(PAGE_SIZE, width);
        }
    }
}

