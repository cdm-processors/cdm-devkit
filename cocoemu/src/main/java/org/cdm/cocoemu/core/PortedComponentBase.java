package org.cdm.cocoemu.core;

import org.cdm.cocoemu.core.ports.PortsInitializer;

public abstract class PortedComponentBase implements Component {
    protected PortedComponentBase() {
        PortsInitializer.initializePorts(this);
    }
}
