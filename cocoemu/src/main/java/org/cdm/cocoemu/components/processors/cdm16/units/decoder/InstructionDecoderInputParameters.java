package org.cdm.cocoemu.components.processors.cdm16.units.decoder;

import lombok.Value;
import lombok.experimental.Accessors;

@Value
@Accessors(fluent = true)
public class InstructionDecoderInputParameters {
    int instruction;
    int psFlags;
}
