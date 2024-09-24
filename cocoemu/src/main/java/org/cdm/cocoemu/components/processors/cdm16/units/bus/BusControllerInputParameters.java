package org.cdm.cocoemu.components.processors.cdm16.units.bus;

import lombok.Value;
import lombok.experimental.Accessors;

@Value
@Accessors(fluent = true)
public class BusControllerInputParameters {
    int from_bus;
    int data_in;
    boolean sign_extend;
    boolean odd_address;
    boolean word;
}
