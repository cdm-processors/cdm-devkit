package org.cdm.cocoemu;

public abstract class Component<I, O> {
    public I inputs;
    public O outputs;

    public abstract void clockRising();
    public abstract void clockFalling();
    public abstract void update();
}
