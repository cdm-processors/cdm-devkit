package org.cdm.cocoemu.components.processors.cdm16.units.alu;

import lombok.Value;
import lombok.experimental.Accessors;

@Value
@Accessors(fluent = true)
public class AluOutputParameters {
    int S;
    int flags;
}
