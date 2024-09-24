package org.cdm.cocoemu.components.example;

import lombok.AccessLevel;
import lombok.ToString;
import lombok.experimental.FieldDefaults;
import org.cdm.cocoemu.core.ports.InputsClass;
import org.cdm.cocoemu.core.ports.InputsField;
import org.cdm.cocoemu.core.ports.OutputsClass;
import org.cdm.cocoemu.core.ports.OutputsField;

public class ExampleInheritedComponent extends ExampleComponent {
    @InputsField
    public ExampleInheritedComponent.Inputs inputs;
    @OutputsField
    public ExampleInheritedComponent.Outputs outputs;

    @Override
    public void update() {
        super.update();
        outputs.data_out_high = inputs.data_in_high;
    }

    @ToString(callSuper = true)
    @FieldDefaults(level = AccessLevel.PUBLIC)
    @InputsClass
    public static class Inputs extends ExampleComponent.Inputs {
        int data_in_high;
    }

    @ToString(callSuper = true)
    @FieldDefaults(level = AccessLevel.PUBLIC)
    @OutputsClass
    public static class Outputs extends ExampleComponent.Outputs {
        int data_out_high;
    }
}
