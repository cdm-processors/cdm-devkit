package org.cdm.debug.dto;

public class InitializationMessage implements DebuggerMessage {
    public String target;
    public String memoryConfiguration = MemoryConfigurations.HARVARD;
}
