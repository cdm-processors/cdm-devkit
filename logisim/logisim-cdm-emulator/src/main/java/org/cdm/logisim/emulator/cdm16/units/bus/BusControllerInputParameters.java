package org.cdm.logisim.emulator.cdm16.units.bus;

public record BusControllerInputParameters(
    int from_bus,
    int data_in,
    boolean sign_extend,
    boolean odd_address,
    boolean word
) {}
