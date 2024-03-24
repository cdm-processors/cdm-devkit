package org.cdm.logisim.emulator.cdm16e;

import com.cburch.logisim.data.BitWidth;
import com.cburch.logisim.data.Value;
import com.cburch.logisim.instance.InstanceState;
import org.cdm.logisim.emulator.cdm16.*;
import org.cdm.logisim.emulator.cdm16.units.bus.BusControllerInputParameters;
import org.cdm.logisim.emulator.cdm16e.exceptions.ExtendedExceptionChecker;
import org.cdm.logisim.emulator.cdm16e.exceptions.ExtendedExceptionCheckerInputParameters;
import org.cdm.logisim.emulator.cdm16e.exceptions.ExtendedExceptionCheckerOutputParameters;
import org.cdm.logisim.emulator.cdm16e.exceptions.ExtendedExceptionControlUnit;
import org.cdm.logisim.emulator.cdm16e.exceptions.ExtendedExceptionControlUnitInputParameters;

import static org.cdm.logisim.emulator.cdm16.Arithmetic.toBoolean;

public class Cdm16eProcessor extends Cdm16Processor {
    private static final String MAIN_MICROCODE = "/cdm16e/cdm16e_decoder.img";
    private static final String EXC_MICROCODE = "/cdm16e/cdm16e_decoder_exc.img";
    private static final String EXTENSION_MICROCODE = "/cdm16e/cdm16e_extension.img";
    private static final String EXTENSION_EXC_MICROCODE = "/cdm16e/cdm16e_extension_exc.img";

    private int[] extensionMicrocode;
    private int[] extensionExceptionMicrocode;

    private int extensionMicrocommand;

    private final Register rx0 = new Register("rx0");
    private final Register rx1 = new Register("rx1");

    private RegisterCounter ssp = new RegisterCounter("ssp");

    private final RegisterCounter[] stackPointers = new RegisterCounter[] {
            new RegisterCounter("sp0"),
            new RegisterCounter("sp1")
    };

    @Override
    protected void loadMicrocode() {
        mainMicrocode = MicrocodeLoader.loadFromResources(MAIN_MICROCODE);
        exceptionMicrocode = MicrocodeLoader.loadFromResources(EXC_MICROCODE);

        extensionMicrocode = MicrocodeLoader.loadFromResources(EXTENSION_MICROCODE);
        extensionExceptionMicrocode = MicrocodeLoader.loadFromResources(EXTENSION_EXC_MICROCODE);
    }

    @Override
    protected void updateProcessorState(InstanceState state) {
        if (!toBoolean(state.getPort(Ports.CLK))) {
            holdLatch.setValue(toBoolean(state.getPort(Ports.HOLD)));
        }

        ExtendedStatusRegisterFields extendedStatusRegisterFields =
                decodeExtendedStatusRegister(ps.getValue());

        selectStackPointer(extendedStatusRegisterFields.mode());

        microcommand = mainMicrocode[microcommandAddress];
        extensionMicrocommand = extensionMicrocode[microcommandAddress];

        updateDatapath();

        busControllerSignals = busController.update(new BusControllerInputParameters(
                busD.getValue(),
                readDataBus(state),
                MicrocodeSignals.check(microcommand, MicrocodeSignals.SIGN_EXTEND),
                toBoolean(busA.getValue() & 1),
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


        boolean exc_trig_ext = toBoolean(state.getPort(Ports.EXC));
        boolean irq = toBoolean(state.getPort(Ports.IRQ));

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
    protected void updateExternal(InstanceState state) {
        super.updateExternal(state);

        if (ExtensionMicrocodeSignals.check(extensionMicrocommand, ExtensionMicrocodeSignals.VEC)) {
            state.setPort(Ports.VEC, Value.TRUE, DELAY);
        } else {
            state.setPort(Ports.VEC, Value.FALSE, DELAY);
        }

        ExtendedStatusRegisterFields extendedStatusRegisterFields =
                decodeExtendedStatusRegister(ps.getValue());

        if (extendedStatusRegisterFields.io_header()) {
            state.setPort(Ports.IO_HEADER, Value.TRUE, DELAY);
        } else {
            state.setPort(Ports.IO_HEADER, Value.FALSE, DELAY);
        }

        state.setPort(
                Ports.CTX_NUMBER,
                Value.createKnown(BitWidth.create(8), extendedStatusRegisterFields.context_number()),
                DELAY
        );
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
        return new ExtendedStatusRegisterFields(
                toBoolean(value & (1 << 15)),
                toBoolean(value & (1 << 14)),
                toBoolean(value & (1 << 13)),
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
}
