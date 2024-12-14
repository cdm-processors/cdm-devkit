package org.cdm.cocoemu.server.adapter;

public enum ProcessorType {
    CDM8,
    CDM8E,
    CDM16HARVARD,
    CDM16VONNEUMANN,
    CDM16E;

    @Override
    public String toString() {
        return Factory.getDebugEnvironment(this).getProcessorAdapter().getDisplayName();
    }
}
