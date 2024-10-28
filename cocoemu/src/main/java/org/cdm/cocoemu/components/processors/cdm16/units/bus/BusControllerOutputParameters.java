package org.cdm.cocoemu.components.processors.cdm16.units.bus;

import lombok.Value;
import lombok.experimental.Accessors;

@Value
@Accessors(fluent = true)
public class BusControllerOutputParameters {
    int data_out;
    int to_bus;
    boolean inc_address;
    boolean phase;
    boolean clk_inhibit;
}
