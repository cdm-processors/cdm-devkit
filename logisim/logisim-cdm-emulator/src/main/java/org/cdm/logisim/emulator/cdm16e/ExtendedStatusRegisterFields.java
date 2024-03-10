package org.cdm.logisim.emulator.cdm16e;

import lombok.Value;
import lombok.experimental.Accessors;

@Value
@Accessors(fluent = true)
public class ExtendedStatusRegisterFields {
    boolean interrupt_enable;
    boolean mode;
    boolean io_header;
    int context_number;
    int arith_flags;
}
