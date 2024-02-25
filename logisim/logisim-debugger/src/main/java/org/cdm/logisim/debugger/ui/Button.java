package org.cdm.logisim.debugger.ui;

import com.cburch.logisim.data.Bounds;
import com.cburch.logisim.instance.InstancePainter;

import java.awt.*;
import java.awt.event.MouseEvent;

public class Button {
    private final Bounds buttonBounds;
    private final String buttonLabel;
    private boolean buttonPressed = false;

    public Button(Bounds buttonBounds, String buttonLabel) {
        this.buttonBounds = buttonBounds;
        this.buttonLabel = buttonLabel;
    }

    public boolean checkPressed(Bounds componentBounds, MouseEvent e) {
        buttonPressed = buttonBounds
                .translate(componentBounds.getX(), componentBounds.getY())
                .contains(e.getX(), e.getY());

        return buttonPressed;
    }

    public void draw(Bounds componentBounds, InstancePainter painter) {
        painter.drawRectangle(buttonBounds.translate(componentBounds.getX(), componentBounds.getY()), buttonLabel);
    }

    public void drawOnPress(Bounds componentBounds, Graphics g) {
        if (buttonPressed) {
            buttonPressed = false;
            Bounds localBounds = buttonBounds.translate(componentBounds.getX(), componentBounds.getY());
            g.fillRect(
                    localBounds.getX(),
                    localBounds.getY(),
                    localBounds.getWidth(),
                    localBounds.getHeight()
            );
        }
    }
}
