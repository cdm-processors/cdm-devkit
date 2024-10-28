package org.cdm.cocoemu.components.example;

import lombok.AccessLevel;
import lombok.ToString;
import lombok.experimental.FieldDefaults;
import org.cdm.cocoemu.core.ports.InputsClass;
import org.cdm.cocoemu.core.ports.InputsField;
import org.cdm.cocoemu.core.ports.OutputsClass;
import org.cdm.cocoemu.core.ports.OutputsField;

public class ExampleInheritedComponent2 extends ExampleInheritedComponent {
    @InputsField
    public ExampleInheritedComponent2.Inputs inputs;
    @OutputsField
    public ExampleInheritedComponent2.Outputs outputs;

    @Override
    public void update() {
        super.update();
        outputs.data_out_high2 = inputs.data_in_high2;
    }

    @ToString(callSuper = true)
    @FieldDefaults(level = AccessLevel.PUBLIC)
    @InputsClass
    public static class Inputs extends ExampleInheritedComponent.Inputs {
        int data_in_high2;
    }

    @ToString(callSuper = true)
    @FieldDefaults(level = AccessLevel.PUBLIC)
    @OutputsClass
    public static class Outputs extends ExampleInheritedComponent.Outputs {
        int data_out_high2;
    }
}
