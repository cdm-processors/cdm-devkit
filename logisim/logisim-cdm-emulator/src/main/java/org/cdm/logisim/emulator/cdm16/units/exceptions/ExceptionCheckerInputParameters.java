package org.cdm.logisim.emulator.cdm16.units.exceptions;

public record ExceptionCheckerInputParameters(
    int microcommand,
    int dataBusValue,
    int instructionRegisterValue,
    boolean exc_latch
) {}
