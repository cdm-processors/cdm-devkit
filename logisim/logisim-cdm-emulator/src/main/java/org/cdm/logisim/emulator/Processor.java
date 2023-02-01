package org.cdm.logisim.emulator;

public class Processor {
    private final ProcessorComponent processorComponent;

    public Processor(ProcessorComponent processorComponent) {
        this.processorComponent = processorComponent;
    }

    public void externalInterrupt(int interruptNumber) {
        System.out.println("externalInterrupt");
    }

    public void externalException(int exceptionNumber) {
        System.out.println("externalException");
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
