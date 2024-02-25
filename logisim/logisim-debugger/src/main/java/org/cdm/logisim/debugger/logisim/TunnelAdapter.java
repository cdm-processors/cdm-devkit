package org.cdm.logisim.debugger.logisim;

import com.cburch.logisim.circuit.Circuit;
import com.cburch.logisim.circuit.CircuitState;
import com.cburch.logisim.comp.Component;
import com.cburch.logisim.instance.StdAttr;
import com.cburch.logisim.std.wiring.Tunnel;

public class TunnelAdapter {
    public static Integer getTunnelValue(String name, Circuit circuit, CircuitState circuitState) {
        Component tunnel = circuit
                .getNonWires()
                .stream()
                .filter(x -> x.getFactory() instanceof Tunnel)
                .filter(x -> x.getAttributeSet().getValue(StdAttr.LABEL).equals(name))
                .findAny()
                .orElse(null);

        if (tunnel == null) {
            return null;
        }

        return circuitState.getValue(tunnel.getEnd(0).getLocation()).toIntValue();
    }
}
