package org.cdm.logisim.emulator.cdm16e;

import com.cburch.logisim.data.BitWidth;
import com.cburch.logisim.data.Value;
import com.cburch.logisim.instance.InstanceState;
import org.cdm.cocoemu.components.processors.cdm16e.Cdm16e;
import org.cdm.logisim.emulator.cdm16.Cdm16LogisimAdapter;

public class Cdm16eLogisimAdapter extends Cdm16LogisimAdapter {
    public static void transferExtendedStateFromProcessor(Cdm16e cdm16e, InstanceState state) {
        Cdm16LogisimAdapter.transferStateFromProcessor(cdm16e, state);

        state.setPort(Ports.VEC, booleanToValue(cdm16e.outputs.vec), DELAY);
        state.setPort(Ports.IO_HEADER, booleanToValue(cdm16e.outputs.io_header), DELAY);

        state.setPort(
                Ports.CTX_NUMBER,
                Value.createKnown(BitWidth.create(8), cdm16e.outputs.ctx_number),
                DELAY
        );
    }
}
