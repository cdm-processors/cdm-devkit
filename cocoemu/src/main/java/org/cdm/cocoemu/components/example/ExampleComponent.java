package org.cdm.cocoemu.components.example;

import lombok.AccessLevel;
import lombok.ToString;
import lombok.experimental.FieldDefaults;
import org.cdm.cocoemu.core.PortedComponentBase;
import org.cdm.cocoemu.core.ports.InputsClass;
import org.cdm.cocoemu.core.ports.InputsField;
import org.cdm.cocoemu.core.ports.OutputsClass;
import org.cdm.cocoemu.core.ports.OutputsField;

public class ExampleComponent extends PortedComponentBase {
    @InputsField
    public ExampleComponent.Inputs inputs;
    @OutputsField
    public ExampleComponent.Outputs outputs;

    @Override
    public void update() {
        if (inputs.rw) {
            outputs.data_out = inputs.data_in;
        } else {
            outputs.data_out = 0;
        }
    }

    @ToString
    @FieldDefaults(level = AccessLevel.PUBLIC)
    @InputsClass
    public static class Inputs {
        int data_in;
        boolean rw;
    }

    @ToString
    @FieldDefaults(level = AccessLevel.PUBLIC)
    @OutputsClass
    public static class Outputs {
        int data_out;
    }
}
