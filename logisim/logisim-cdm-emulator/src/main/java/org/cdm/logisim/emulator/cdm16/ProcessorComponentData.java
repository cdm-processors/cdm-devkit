package org.cdm.logisim.emulator.cdm16;

import com.cburch.logisim.instance.InstanceData;
import org.cdm.cocoemu.components.processors.cdm16.Cdm16;

public class ProcessorComponentData implements InstanceData {

    private final Cdm16 processor;
    private final ProcessorClockState processorClockState;

    public ProcessorComponentData(Cdm16 processor) {
        this.processor = processor;
        this.processorClockState = new ProcessorClockState();
    }

    public Cdm16 getProcessor() {
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
