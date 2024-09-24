package org.cdm.cocoemu.core.ports;

import org.cdm.cocoemu.core.Component;

import java.util.Arrays;
import java.util.concurrent.atomic.AtomicInteger;

public class PortsInitializer {
    public static void initializePorts(Component component) {
        Class<? extends Component> currentClass = component.getClass();

        Class<?> inputsClass = null;
        Class<?> outputsClass = null;

        for (Class<?> cls : currentClass.getDeclaredClasses()) {
            if (cls.isAnnotationPresent(InputsClass.class)) {
                inputsClass = cls;
            } else if (cls.isAnnotationPresent(OutputsClass.class)) {
                outputsClass = cls;
            }
        }

        if (inputsClass == null) {
            throw new RuntimeException(String.format("There is no inputs class provided for %s", component.getClass().getName()));
        }

        if (outputsClass == null) {
            throw new RuntimeException(String.format("There is no outputs class provided for %s", component.getClass().getName()));
        }

        Object inputsObject;
        Object outputsObject;
        try {
            inputsObject = inputsClass.getConstructor().newInstance();
            outputsObject = outputsClass.getConstructor().newInstance();
        } catch (Exception e) {
            throw new RuntimeException("Can't create inputs and outputs objects", e);
        }

        AtomicInteger setCount = new AtomicInteger();

        Arrays.stream(currentClass.getFields())
                .filter((x) -> x.isAnnotationPresent(InputsField.class))
                .forEach((x) -> {
                    try {
                        x.set(component, inputsObject);
                        setCount.getAndIncrement();
                    } catch (IllegalAccessException e) {
                        throw new RuntimeException("Can't initialize inputs field " + x.getName(), e);
                    }
                });

        Arrays.stream(currentClass.getFields())
                .filter((x) -> x.isAnnotationPresent(OutputsField.class))
                .forEach((x) -> {
                    try {
                        x.set(component, outputsObject);
                        setCount.getAndIncrement();
                    } catch (IllegalAccessException e) {
                        throw new RuntimeException("Can't initialize outputs field " + x.getName(), e);
                    }
                });

        if (setCount.get() == 0) {
            throw new RuntimeException(String.format("There is no inputs and outputs fields provided for %s", currentClass.getName()));
        }
    }
}
