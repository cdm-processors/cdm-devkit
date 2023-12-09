package org.cdm.logisim.emulator.cdm16;

import com.cburch.logisim.instance.InstanceData;

public class ProcessorComponentData implements InstanceData {

    private final Processor processor;
    private final ProcessorClockState processorClockState;

    public ProcessorComponentData() {
        this.processor = new Processor();
        this.processorClockState = new ProcessorClockState();
    }

    public Processor getProcessor() {
        return processor;
    }

    public ProcessorClockState getProcessorClockState() {
        return processorClockState;
    }

    @Override
    public Object clone() {
        try {
            return (ProcessorComponentData) super.clone();
        } catch (CloneNotSupportedException var2) {
            return null;
        }
    }
}
