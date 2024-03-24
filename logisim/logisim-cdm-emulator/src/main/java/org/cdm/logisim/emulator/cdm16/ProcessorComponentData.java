package org.cdm.logisim.emulator.cdm16;

import com.cburch.logisim.instance.InstanceData;

public class ProcessorComponentData implements InstanceData {

    private final Cdm16Processor processor;
    private final ProcessorClockState processorClockState;

    public ProcessorComponentData(Cdm16Processor processor) {
        this.processor = processor;
        this.processorClockState = new ProcessorClockState();
    }

    public Cdm16Processor getProcessor() {
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
