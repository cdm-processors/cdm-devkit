package org.cdm.logisim.emulator.cdm16;

import com.cburch.logisim.instance.InstanceData;
import com.cburch.logisim.instance.InstanceState;

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

    // Debugger support
    public boolean exceptionHappened() {
        return getProcessor().exceptionHappened();
    }

    public int exceptionNumber(InstanceState state) {
        return getProcessor().exceptionNumber(state);
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
