package org.cdm.logisim.emulator.cdm16.units.bus;

import org.cdm.logisim.emulator.cdm16.Latch;
import org.cdm.logisim.emulator.cdm16.Register;

import static org.cdm.logisim.emulator.cdm16.Arithmetic.signExtend;

public class BusController {
    private final Latch incAddressLatch = new Latch();
    private final Register dataTempRegister = new Register("dtr", 8);

    public boolean inc_address() {
        return incAddressLatch.getValue();
    }

    public void clockFalling(int data_in, boolean clk_inhibit) {
        incAddressLatch.setValue(clk_inhibit);

        if (clk_inhibit) {
            dataTempRegister.setValue(data_in);
        }
    }

    public BusControllerOutputParameters update(BusControllerInputParameters parameters) {
        boolean clk_inhibit = parameters.odd_address() && parameters.word();
        boolean phase = incAddressLatch.getValue();
        boolean inc_address = incAddressLatch.getValue();

        int data_out;

        if (parameters.word()) {
            if (phase) {
                data_out = parameters.from_bus() >> 8;
            } else {
                data_out = parameters.from_bus();
            }
        } else {
            data_out = parameters.from_bus();
        }

        int to_bus;

        if (parameters.word()) {
            if (phase) {
                to_bus = (parameters.data_in() << 8) + dataTempRegister.getValue();
            } else {
                to_bus = parameters.data_in();
            }
        } else {
            if (parameters.sign_extend()) {
                to_bus = signExtend(parameters.data_in());
            } else {
                to_bus = parameters.data_in() & 0xFF;
            }
        }

        return new BusControllerOutputParameters(
                data_out,
                to_bus,
                inc_address,
                phase,
                clk_inhibit
        );
    }
}
