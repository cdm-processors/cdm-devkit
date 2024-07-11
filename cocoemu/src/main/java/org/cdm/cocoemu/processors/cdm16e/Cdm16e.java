package org.cdm.cocoemu.processors.cdm16e;

import lombok.ToString;
import org.cdm.cocoemu.primitives.Register;
import org.cdm.cocoemu.primitives.RegisterCounter;
import org.cdm.cocoemu.processors.MicrocodeLoader;
import org.cdm.cocoemu.processors.cdm16.Arithmetic;
import org.cdm.cocoemu.processors.cdm16.Cdm16;
import org.cdm.cocoemu.processors.cdm16.Status;
import org.cdm.cocoemu.processors.cdm16.units.bus.BusControllerInputParameters;
import org.cdm.cocoemu.processors.cdm16e.exceptions.*;

public class Cdm16e extends Cdm16 {

    {
        inputs = new Cdm16e.Inputs();
        outputs = new Cdm16e.Outputs();
    }

    @Override
    public Cdm16e.Inputs getInputs() {
        return (Cdm16e.Inputs) inputs;
    }

    @Override
    public Cdm16e.Outputs getOutputs() {
        return (Cdm16e.Outputs) outputs;
    }

    private static final String MAIN_MICROCODE = "/cdm16e/cdm16e_decoder.img";
    private static final String EXC_MICROCODE = "/cdm16e/cdm16e_decoder_exc.img";
    private static final String EXTENSION_MICROCODE = "/cdm16e/cdm16e_extension.img";
    private static final String EXTENSION_EXC_MICROCODE = "/cdm16e/cdm16e_extension_exc.img";

    private int[] extensionMicrocode;
    private int[] extensionExceptionMicrocode;

    private int extensionMicrocommand;

    private final Register rx0 = new Register("rx0", BIT_WIDTH);
    private final Register rx1 = new Register("rx1", BIT_WIDTH);

    private RegisterCounter ssp = new RegisterCounter("ssp", BIT_WIDTH);

    private final RegisterCounter[] stackPointers = new RegisterCounter[]{
            new RegisterCounter("sp0", BIT_WIDTH),
            new RegisterCounter("sp1", BIT_WIDTH)
    };

    @Override
    protected void loadMicrocode() {
        mainMicrocode = MicrocodeLoader.loadFromResources(MAIN_MICROCODE);
        exceptionMicrocode = MicrocodeLoader.loadFromResources(EXC_MICROCODE);

        extensionMicrocode = MicrocodeLoader.loadFromResources(EXTENSION_MICROCODE);
        extensionExceptionMicrocode = MicrocodeLoader.loadFromResources(EXTENSION_EXC_MICROCODE);
    }

    @Override
    protected void updateProcessorState() {
        if (!clockState) {
            holdLatch.setValue(inputs.hold);
        }

        ExtendedStatusRegisterFields extendedStatusRegisterFields =
                decodeExtendedStatusRegister(ps.getValue());

        selectStackPointer(extendedStatusRegisterFields.mode());

        microcommand = mainMicrocode[microcommandAddress];
        extensionMicrocommand = extensionMicrocode[microcommandAddress];

        updateDatapath();

        busControllerSignals = busController.update(new BusControllerInputParameters(
                busD.getValue(),
                readDataBus(),
                MicrocodeSignals.check(microcommand, MicrocodeSignals.SIGN_EXTEND),
                Arithmetic.toBoolean(busA.getValue() & 1),
                MicrocodeSignals.check(microcommand, MicrocodeSignals.WORD)
        ));

        if (MicrocodeSignals.check(microcommand, MicrocodeSignals.READ)) {
            busD.setValue(busControllerSignals.to_bus());
        }

        ExtendedExceptionCheckerOutputParameters excInfo =
                ExtendedExceptionChecker.compute(new ExtendedExceptionCheckerInputParameters(
                        microcommand,
                        extensionMicrocommand,
                        virtualInstructionLatch.getValue(),
                        busD.getValue(),
                        ir.getValue(),
                        exceptionLatch.getValue(),
                        extendedStatusRegisterFields.mode()
                ));


        boolean exc_trig_ext = inputs.exc;
        boolean irq = inputs.irq;

        ecuSignals = ExtendedExceptionControlUnit.compute(new ExtendedExceptionControlUnitInputParameters(
                excInfo.exc_trig_sp(),
                excInfo.exc_trig_pc(),
                excInfo.exc_trig_invalid_inst(),
                excInfo.exc_privilege_violation(),
                exc_trig_ext,
                excInfo.double_fault(),
                exceptionLatch.getValue(),
                decoderSignals.intInstruction(),
                decoderSignals.rtiInstruction(),
                irq,
                ps.getInterruptStatus(),
                fetch
        ));

        if (ecuSignals.exc_triggered()) {
            microcommand = exceptionMicrocode[microcommandAddress];
            extensionMicrocommand = extensionExceptionMicrocode[microcommandAddress];
        }

        boolean suspendMicrocode = (status == Status.HALTED) || (status == Status.FAULT) ||
                startupLatch.getValue() || (fetch && ecuSignals.latch_int());

        if (suspendMicrocode) {
            microcommand = 0x8000000;
            extensionMicrocommand = 0;
        }

        updateDatapath();
    }

    @Override
    protected void updateExternal() {
        super.updateExternal();

        Cdm16e.Outputs outputs = getOutputs();

        outputs.vec = ExtensionMicrocodeSignals.check(extensionMicrocommand, ExtensionMicrocodeSignals.VEC);

        ExtendedStatusRegisterFields extendedStatusRegisterFields =
                decodeExtendedStatusRegister(ps.getValue());

        outputs.io_header = extendedStatusRegisterFields.io_header();
        outputs.ctx_number = extendedStatusRegisterFields.context_number();
    }

    @Override
    protected void updateRegisters() {
        super.updateRegisters();

        if (ExtensionMicrocodeSignals.check(extensionMicrocommand, ExtensionMicrocodeSignals.SHADOW_SP_LATCH)) {
            ssp.setValue(busD.getValue());
        }

        if (ExtensionMicrocodeSignals.check(extensionMicrocommand, ExtensionMicrocodeSignals.RX0_LATCH)) {
            rx0.setValue(busD.getValue());
        }
        if (ExtensionMicrocodeSignals.check(extensionMicrocommand, ExtensionMicrocodeSignals.RX1_LATCH)) {
            rx1.setValue(busD.getValue());
        }
    }

    @Override
    protected void updateDatapath() {
        if (ExtensionMicrocodeSignals.check(extensionMicrocommand, ExtensionMicrocodeSignals.SHADOW_SP_ASRTD)) {
            busD.setValue(ssp.getValue());
        }

        if (ExtensionMicrocodeSignals.check(extensionMicrocommand, ExtensionMicrocodeSignals.RX0_ASRTD)) {
            busD.setValue(rx0.getValue());
        }
        if (ExtensionMicrocodeSignals.check(extensionMicrocommand, ExtensionMicrocodeSignals.RX1_ASRTD)) {
            busD.setValue(rx1.getValue());
        }

        super.updateDatapath();
    }

    private void selectStackPointer(boolean mode) {
        sp = mode ? stackPointers[1] : stackPointers[0];
        ssp = mode ? stackPointers[0] : stackPointers[1];
    }

    private ExtendedStatusRegisterFields decodeExtendedStatusRegister(int value) {
        // TODO: Get rid of object allocation
        return new ExtendedStatusRegisterFields(
                Arithmetic.toBoolean(value & (1 << 15)),
                Arithmetic.toBoolean(value & (1 << 14)),
                Arithmetic.toBoolean(value & (1 << 13)),
                (value >> 4) & 0xFF,
                value & 0xF
        );
    }

    public static class ExtendedExceptionNumbers {
        public static final int PRIVILEGE_VIOLATION = 5;
    }

    public static class ExtensionMicrocodeSignals {
        public static final int NOP = 1;
        public static final int PRIVILEGED = 1 << 1;
        public static final int RX0_ASRTD = 1 << 2;
        public static final int RX0_LATCH = 1 << 3;
        public static final int RX1_ASRTD = 1 << 4;
        public static final int RX1_LATCH = 1 << 5;
        public static final int SHADOW_SP_ASRTD = 1 << 6;
        public static final int SHADOW_SP_LATCH = 1 << 7;
        public static final int VEC = 1 << 8;
        public static final int CUT_NOP = 1 << 9;

        public static boolean check(int value, int signal) {
            return (value & signal) > 0;
        }
    }

    @ToString(callSuper = true)
    public static class Inputs extends Cdm16.Inputs {
    }

    @ToString(callSuper = true)
    public static class Outputs extends Cdm16.Outputs {
        public boolean io_header;
        public boolean vec;
        public int ctx_number;
    }
}
