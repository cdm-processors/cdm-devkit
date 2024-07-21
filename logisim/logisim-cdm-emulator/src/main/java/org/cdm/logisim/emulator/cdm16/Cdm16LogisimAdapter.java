package org.cdm.logisim.emulator.cdm16;

import com.cburch.logisim.data.BitWidth;
import com.cburch.logisim.data.Value;
import com.cburch.logisim.instance.InstanceState;
import org.cdm.cocoemu.components.processors.cdm16.Cdm16;
import org.cdm.logisim.emulator.CocoemuLogisimBridge;

public class Cdm16LogisimAdapter extends CocoemuLogisimBridge {
    public static void transferStateToProcessor(InstanceState state, Cdm16 cdm16) {
        if (state.getPort(Ports.DATA_IN).isFullyDefined()) {
            cdm16.inputs.data_in = state.getPort(Ports.DATA_IN).toIntValue();
        } else {
            cdm16.inputs.data_in = 0;
        }

        cdm16.inputs.irq = valueToBoolean(state.getPort(Ports.IRQ));
        cdm16.inputs.int_number = state.getPort(Ports.INT_NUMBER).toIntValue();

        cdm16.inputs.exc = valueToBoolean(state.getPort(Ports.EXC));
        cdm16.inputs.exc_number = state.getPort(Ports.EXC_NUMBER).toIntValue();

        cdm16.inputs.hold = valueToBoolean(state.getPort(Ports.HOLD));
    }

    public static void transferStateFromProcessor(Cdm16 cdm16, InstanceState state) {
        for (int i = 0; i < cdm16.outputs.gpRegisters.length; ++i) {
            state.setPort(
                    Ports.R0 + i,
                    Value.createKnown(BitWidth.create(16), cdm16.outputs.gpRegisters[i]),
                    DELAY
            );
        }

        state.setPort(Ports.PC, Value.createKnown(BitWidth.create(16), cdm16.outputs.pc), DELAY);
        state.setPort(Ports.SP, Value.createKnown(BitWidth.create(16), cdm16.outputs.sp), DELAY);
        state.setPort(Ports.PS, Value.createKnown(BitWidth.create(16), cdm16.outputs.ps), DELAY);

        state.setPort(Ports.STATUS, Value.createKnown(BitWidth.create(2), cdm16.outputs.status), DELAY);

        state.setPort(Ports.FETCH, booleanToValue(cdm16.outputs.fetch), DELAY);

        state.setPort(Ports.WORD, booleanToValue(cdm16.outputs.word), DELAY);
        state.setPort(Ports.DATA, booleanToValue(cdm16.outputs.data), DELAY);
        state.setPort(Ports.READ, booleanToValue(cdm16.outputs.read), DELAY);
        state.setPort(Ports.MEM, booleanToValue(cdm16.outputs.mem), DELAY);

        state.setPort(Ports.IAck, booleanToValue(cdm16.outputs.iack), DELAY);

        state.setPort(Ports.ADDRESS, Value.createKnown(BitWidth.create(16), cdm16.outputs.address), DELAY);

        /*if (!MicrocodeSignals.check(microcommand, MicrocodeSignals.MEM)) {
            return;
        }*/

        state.setPort(
                Ports.DATA_OUT,
                Value.createKnown(BitWidth.create(16), cdm16.outputs.data_out),
                DELAY
        );
    }
}
