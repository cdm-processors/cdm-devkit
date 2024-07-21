package org.cdm.logisim.emulator;

import com.cburch.logisim.instance.InstanceData;
import org.cdm.cocoemu.core.Component;

public class ProcessorComponentData<T extends Component> implements InstanceData {

    private final T processorComponent;
    private final ProcessorClockState processorClockState;

    public ProcessorComponentData(T processorComponent) {
        this.processorComponent = processorComponent;
        this.processorClockState = new ProcessorClockState();
    }

    public T getProcessorComponent() {
        return processorComponent;
    }

    public ProcessorClockState getProcessorClockState() {
        return processorClockState;
    }

    @Override
    public Object clone() {
        try {
            return super.clone();
        } catch (CloneNotSupportedException var2) {
            return null;
        }
    }
}
