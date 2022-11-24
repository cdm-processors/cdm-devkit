package ru.miqqra;

/* Copyright (c) 2010, Carl Burch. License information is located in the
 * com.cburch.logisim.Main source code and at www.cburch.com/logisim/. */

import java.awt.Color;
import java.awt.Graphics;
import java.awt.event.KeyEvent;
import java.awt.event.MouseEvent;

import com.cburch.logisim.data.Bounds;
import com.cburch.logisim.instance.InstancePainter;
import com.cburch.logisim.instance.InstancePoker;
import com.cburch.logisim.instance.InstanceState;
import com.cburch.logisim.proj.Project;

public class BankedMemPoker extends InstancePoker {
    private BankedMemPoker sub;

    @Override
    public boolean init(InstanceState state, MouseEvent event) {
        Bounds bds = state.getInstance().getBounds();
        BankedMemState data = (BankedMemState) state.getData();
        long addr = data.getAddressAt(event.getX() - bds.getX(),
                event.getY() - bds.getY());

        // See if outside box
        if (addr < 0) {
            sub = new BankedMemPoker.AddrPoker();
        } else {
            sub = new BankedMemPoker.DataPoker(state, data, addr);
        }
        return true;
    }

    @Override
    public Bounds getBounds(InstancePainter state) {
        return sub.getBounds(state);
    }

    @Override
    public void paint(InstancePainter painter) {
        sub.paint(painter);
    }

    @Override
    public void keyTyped(InstanceState state, KeyEvent e) {
        sub.keyTyped(state, e);
    }

    private static class DataPoker extends BankedMemPoker {
        int initValue;
        int curValue;

        private DataPoker(InstanceState state, BankedMemState data, long addr) {
            data.setCursor(addr);
            initValue = data.getContents().get(data.getCursor());
            curValue = initValue;

            Object attrs = state.getInstance().getAttributeSet();
            if (attrs instanceof BankedRomAttributes) {
                Project proj = state.getProject();
                if (proj != null) {
                    ((BankedRomAttributes) attrs).setProject(proj);
                }
            }
        }

        @Override
        public Bounds getBounds(InstancePainter painter) {
            BankedMemState data = (BankedMemState) painter.getData();
            Bounds inBounds = painter.getInstance().getBounds();
            return data.getBounds(data.getCursor(), inBounds);
        }

        @Override
        public void paint(InstancePainter painter) {
            Bounds bds = getBounds(painter);
            Graphics g = painter.getGraphics();
            g.setColor(Color.RED);
            g.drawRect(bds.getX(), bds.getY(), bds.getWidth(), bds.getHeight());
            g.setColor(Color.BLACK);
        }

        @Override
        public void stopEditing(InstanceState state) {
            BankedMemState data = (BankedMemState) state.getData();
            data.setCursor(-1);
        }

        @Override
        public void keyTyped(InstanceState state, KeyEvent e) {
            char c = e.getKeyChar();
            int val = Character.digit(e.getKeyChar(), 16);
            BankedMemState data = (BankedMemState) state.getData();
            if (val >= 0) {
                curValue = curValue * 16 + val;
                data.getContents().set(data.getCursor(), curValue);
                state.fireInvalidated();
            } else if (c == ' ' || c == '\t') {
                moveTo(data, data.getCursor() + 1);
            } else if (c == '\r' || c == '\n') {
                moveTo(data, data.getCursor() + data.getColumns());
            } else if (c == '\u0008' || c == '\u007f') {
                moveTo(data, data.getCursor() - 1);
            }
        }

        private void moveTo(BankedMemState data, long addr) {
            if (data.isValidAddr(addr)) {
                data.setCursor(addr);
                data.scrollToShow(addr);
                initValue = data.getContents().get(addr);
                curValue = initValue;
            }
        }
    }

    private static class AddrPoker extends BankedMemPoker {
        @Override
        public Bounds getBounds(InstancePainter painter) {
            BankedMemState data = (BankedMemState) painter.getData();
            return data.getBounds(-1, painter.getBounds());
        }

        @Override
        public void paint(InstancePainter painter) {
            Bounds bds = getBounds(painter);
            Graphics g = painter.getGraphics();
            g.setColor(Color.RED);
            g.drawRect(bds.getX(), bds.getY(), bds.getWidth(), bds.getHeight());
            g.setColor(Color.BLACK);
        }

        @Override
        public void keyTyped(InstanceState state, KeyEvent e) {
            char c = e.getKeyChar();
            int val = Character.digit(e.getKeyChar(), 16);
            BankedMemState data = (BankedMemState) state.getData();
            if (val >= 0) {
                long newScroll = (data.getScroll() * 16 + val) & (data.getLastAddress());
                data.setScroll(newScroll);
            } else if (c == ' ') {
                data.setScroll(data.getScroll() + (data.getRows() - 1) * data.getColumns());
            } else if (c == '\r' || c == '\n') {
                data.setScroll(data.getScroll() + data.getColumns());
            } else if (c == '\u0008' || c == '\u007f') {
                data.setScroll(data.getScroll() - data.getColumns());
            }
        }
    }
}
