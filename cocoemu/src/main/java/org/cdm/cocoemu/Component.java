package org.cdm.cocoemu;

public abstract class Component<I, O> {
    protected I inputs;
    protected O outputs;

    public I getInputs() {
        return inputs;
    }

    public O getOutputs() {
        return outputs;
    }

    public abstract void clockRising();

    public abstract void clockFalling();

    public abstract void update();
}
