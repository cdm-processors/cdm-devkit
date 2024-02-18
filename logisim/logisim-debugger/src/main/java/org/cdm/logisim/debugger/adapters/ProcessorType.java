package org.cdm.logisim.debugger.adapters;

public enum ProcessorType {
    CDM8,
    CDM8E,
    CDM16_CIRCUIT,
    CDM16_EMU;

    @Override
    public String toString() {
        return ProcessorAdapterFactory.getProcessorAdapter(this).getDisplayName();
    }
}
