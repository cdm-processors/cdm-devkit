package org.cdm.logisim.emulator.cdm16.units.decoder;

public record InstructionDecoderInputParameters(
    int instruction,
    int psFlags
) {}
