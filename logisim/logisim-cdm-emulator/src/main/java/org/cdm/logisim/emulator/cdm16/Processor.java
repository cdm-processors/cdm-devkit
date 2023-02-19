package org.cdm.logisim.emulator.cdm16;

import org.cdm.logisim.emulator.ExceptionHandler;
import org.cdm.logisim.emulator.InterruptHandler;
import org.cdm.logisim.emulator.GenericProcessor;

public class Processor implements GenericProcessor, ExceptionHandler, InterruptHandler {

    public static int MAX_INT = 0xFFFF;
    private final ProcessorComponent processorComponent;

    public Processor(ProcessorComponent processorComponent) {
        this.processorComponent = processorComponent;
    }

    public void externalInterrupt(int interruptNumber) {
        System.out.println("externalInterrupt" + interruptNumber);
    }

    public void externalException(int exceptionNumber) {
        System.out.println("externalException " + exceptionNumber);
    }

    public void clockRising() {
        System.out.println("clockRising");
    }

    public void clockFalling() {
        System.out.println("clockFalling");
    }

    public void update() {
        System.out.println("update");
    }

}
