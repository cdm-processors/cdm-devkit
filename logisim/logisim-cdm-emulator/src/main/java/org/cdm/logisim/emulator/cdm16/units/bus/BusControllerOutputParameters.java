package org.cdm.logisim.emulator.cdm16.units.bus;

public record BusControllerOutputParameters(
    int data_out,
    int to_bus,
    boolean inc_address,
    boolean phase,
    boolean clk_inhibit
) {}
