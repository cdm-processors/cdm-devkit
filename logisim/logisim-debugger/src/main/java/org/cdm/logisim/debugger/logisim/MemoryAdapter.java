package org.cdm.logisim.debugger.logisim;

import com.cburch.hex.HexModel;
import com.cburch.logisim.circuit.Circuit;
import com.cburch.logisim.comp.Component;
import com.cburch.logisim.comp.ComponentFactory;
import com.cburch.logisim.instance.InstanceState;

import java.io.File;
import java.lang.reflect.InvocationTargetException;
import java.lang.reflect.Method;

public class MemoryAdapter {
    public static HexModel getMemoryContents(ComponentFactory memoryComponentFactory, InstanceState memoryComponentState) throws NoSuchMethodException, InvocationTargetException, IllegalAccessException {
        Method getStateMethod =
                memoryComponentFactory.getClass().getDeclaredMethod("getState", InstanceState.class);
        getStateMethod.setAccessible(true);

        Object memState = getStateMethod.invoke(memoryComponentFactory, memoryComponentState);

        Method getContentsMethod = memState.getClass().getMethod("getContents");
        getContentsMethod.setAccessible(true);

        return (HexModel) getContentsMethod.invoke(memState);
    }

    public static void loadImage(File imageFile, ComponentFactory memoryComponentFactory, InstanceState memoryComponentState) throws NoSuchMethodException, InvocationTargetException, IllegalAccessException {
        Method loadImageMethod =
                memoryComponentFactory.getClass().getDeclaredMethod("loadImage", InstanceState.class, File.class);
        loadImageMethod.setAccessible(true);

        loadImageMethod.invoke(memoryComponentFactory, memoryComponentState, imageFile);
    }

    public static Component locateRamComponent(Circuit circuit) {
        return circuit
                .getNonWires()
                .stream()
                .filter(x -> x.getFactory().getName().equals("RAM"))
                .findAny()
                .orElse(null);
    }

    public static Component locateRomComponent(Circuit circuit) {
        return circuit
                .getNonWires()
                .stream()
                .filter(x -> x.getFactory().getName().equals("ROM"))
                .findAny()
                .orElse(null);
    }
}
