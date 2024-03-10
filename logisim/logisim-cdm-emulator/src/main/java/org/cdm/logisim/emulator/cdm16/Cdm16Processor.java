package org.cdm.logisim.emulator.cdm16;

import com.cburch.logisim.data.BitWidth;
import com.cburch.logisim.data.Value;
import com.cburch.logisim.instance.InstanceState;
import org.cdm.logisim.emulator.cdm16.units.FetchUnit;
import org.cdm.logisim.emulator.cdm16.units.ImmComputationUnit;
import org.cdm.logisim.emulator.cdm16.units.alu.Alu;
import org.cdm.logisim.emulator.cdm16.units.alu.AluInputParameters;
import org.cdm.logisim.emulator.cdm16.units.alu.AluOutputParameters;
import org.cdm.logisim.emulator.cdm16.units.bus.BusController;
import org.cdm.logisim.emulator.cdm16.units.bus.BusControllerInputParameters;
import org.cdm.logisim.emulator.cdm16.units.bus.BusControllerOutputParameters;
import org.cdm.logisim.emulator.cdm16.units.decoder.InstructionDecoder;
import org.cdm.logisim.emulator.cdm16.units.decoder.InstructionDecoderInputParameters;
import org.cdm.logisim.emulator.cdm16.units.decoder.InstructionDecoderOutputParameters;
import org.cdm.logisim.emulator.cdm16.units.exceptions.ExceptionChecker;
import org.cdm.logisim.emulator.cdm16.units.exceptions.ExceptionCheckerInputParameters;
import org.cdm.logisim.emulator.cdm16.units.exceptions.ExceptionCheckerOutputParameters;
import org.cdm.logisim.emulator.cdm16.units.exceptions.ExceptionControlUnit;
import org.cdm.logisim.emulator.cdm16.units.exceptions.ExceptionControlUnitInputParameters;
import org.cdm.logisim.emulator.cdm16.units.exceptions.ExceptionControlUnitOutputParameters;

import static org.cdm.logisim.emulator.cdm16.Arithmetic.toBoolean;

import java.util.ArrayList;
import java.util.List;

public class Cdm16Processor {

    public static int MAX_PHASE = 7;
    public static int DELAY = 1;

    private static final String MAIN_MICROCODE = "/cdm16/cdm16_decoder.img";
    private static final String EXC_MICROCODE = "/cdm16/cdm16_decoder_exc.img";

    protected int[] mainMicrocode;
    protected int[] exceptionMicrocode;

    protected int microcommand;

    protected int microcommandAddress;

    protected final RegisterFile registerFile = new RegisterFile();

    protected final Register fp = registerFile.getFramePointer();
    protected final RegisterCounter pc = new RegisterCounter("pc");
    protected final StatusRegister ps = new StatusRegister("ps");

    protected RegisterCounter sp = new RegisterCounter("sp");

    protected final Register ir = new Register("ir");

    protected boolean fetch = true;

    protected int status = Status.RUNNING;

    protected int phase = 0;

    protected final Bus bus0 = new Bus("bus0");
    protected final Bus bus1 = new Bus("bus1");
    protected final Bus busA = new Bus("busA");
    protected final Bus busD = new Bus("busD");

    protected final Bus[] buses = new Bus[] {
            bus0,
            bus1,
            busD,
            busA
    };

    protected final Latch holdLatch = new Latch();
    protected final Latch waitLatch = new Latch();
    protected final Latch haltLatch = new Latch();
    protected final Latch faultLatch = new Latch();

    protected final Register externalExceptionVectorRegister = new Register("exc_vec_reg");

    protected final Register internalExceptionVectorRegister = new Register("exc_internal_vec_reg");
    protected final Latch exceptionLatch = new Latch();
    protected final Latch startupLatch = new Latch();

    protected final Latch virtualInstructionLatch = new Latch();

    protected final BusController busController = new BusController();

    protected InstructionDecoderOutputParameters decoderSignals;
    protected AluOutputParameters aluSignals;
    protected ExceptionControlUnitOutputParameters ecuSignals;
    protected BusControllerOutputParameters busControllerSignals;

    public Cdm16Processor() {
        loadMicrocode();

        initialize();
    }

    protected void loadMicrocode() {
        mainMicrocode = MicrocodeLoader.loadFromResources(MAIN_MICROCODE);
        exceptionMicrocode = MicrocodeLoader.loadFromResources(EXC_MICROCODE);
    }

    public void externalInterrupt(InstanceState state, int interruptNumber) {}

    public void externalException(InstanceState state, int exceptionNumber) {}

    public void clockRising(InstanceState state) {}

    public void clockFalling(InstanceState state) {
        if (clockSuspended()) {
            updateWaitLatch(toBoolean(state.getPort(Ports.IRQ)));
            updateStatus();

            return;
        }

        // Pre-latch
        updateProcessorState(state);

        // Latch
        updateExceptionLatches(state);

        updateClockControlLatches(
                decoderSignals.haltInstruction() && !ecuSignals.exc_triggered(),
                decoderSignals.waitInstruction() && !ecuSignals.exc_triggered(),
                toBoolean(state.getPort(Ports.IRQ)),
                ecuSignals.critical_fault()
        );
        updateStatus();

        busController.clockFalling(
                readDataBus(state),
                busControllerSignals.clk_inhibit()
        );

        if (busControllerSignals.clk_inhibit()) {
            return;
        }

        updateRegisters();

        if (fetch) {
            int instruction = FetchUnit.fetchInstruction(
                    busD.getValue(),
                    state.getPort(Ports.INT_NUMBER).toIntValue(),
                    internalExceptionVectorRegister.getValue(),
                    externalExceptionVectorRegister.getValue(),
                    state.getPort(Ports.EXC_NUMBER).toIntValue(),
                    ecuSignals.latch_double_fault(),
                    toBoolean(state.getPort(Ports.EXC)),
                    ecuSignals.exc_triggered(),
                    ecuSignals.latch_int(),
                    startupLatch.getValue()
            );

            ir.setValue(instruction);

            virtualInstructionLatch.setValue(ecuSignals.latch_int() || startupLatch.getValue());
        }

        if (startupLatch.getValue()) {
            startupLatch.reset();
        }

        if (MicrocodeSignals.check(microcommand, MicrocodeSignals.CUT)) {
            phase = 0;
            fetch = !fetch;
        } else {
            phase++;

            if (phase > MAX_PHASE) {
                phase = 0;
                status = Status.FAULT;
            }
        }

        // Post-latch
        for (Bus bus : buses) {
            bus.clear();
        }

        if (fetch) {
            decoderSignals = InstructionDecoder.getFetchSignals();
        } else {
            decoderSignals = InstructionDecoder.compute(new InstructionDecoderInputParameters(
                    ir.getValue(),
                    ps.getFlags()
            ));
        }

        microcommandAddress = decoderSignals.microcodeAddress() + (phase << 7);
    }

    public void update(InstanceState state) {
        updateProcessorState(state);

        updateExternal(state);
    }

    protected void initialize() {
        fetch = true;

        decoderSignals = InstructionDecoder.getFetchSignals();
        microcommandAddress = decoderSignals.microcodeAddress();

        startupLatch.set();
    }

    protected void updateProcessorState(InstanceState state) {
        if (!toBoolean(state.getPort(Ports.CLK))) {
            holdLatch.setValue(toBoolean(state.getPort(Ports.HOLD)));
        }

        microcommand = mainMicrocode[microcommandAddress];

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

        ExceptionCheckerOutputParameters excInfo =
                ExceptionChecker.compute(new ExceptionCheckerInputParameters(
                        microcommand,
                        busD.getValue(),
                        ir.getValue(),
                        exceptionLatch.getValue()
                ));


        boolean exc_trig_ext = toBoolean(state.getPort(Ports.EXC));
        boolean irq = toBoolean(state.getPort(Ports.IRQ));

        ecuSignals = ExceptionControlUnit.compute(new ExceptionControlUnitInputParameters(
                excInfo.exc_trig_sp(),
                excInfo.exc_trig_pc(),
                excInfo.exc_trig_invalid_inst(),
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
        }

        boolean suspendMicrocode = (status == Status.HALTED) || (status == Status.FAULT) ||
                startupLatch.getValue() || (fetch && ecuSignals.latch_int());

        if (suspendMicrocode) {
            microcommand = 0x8000000;
        }

        updateDatapath();
    }

    protected void updateRegisters() {
        if (MicrocodeSignals.check(microcommand, MicrocodeSignals.PC_LATCH)) {
            pc.setValue(busD.getValue());
        }
        if (MicrocodeSignals.check(microcommand, MicrocodeSignals.SP_LATCH)) {
            sp.setValue(busD.getValue());
        }
        if (MicrocodeSignals.check(microcommand, MicrocodeSignals.PS_LATCH_FLAGS)) {
            ps.setFlags(aluSignals.flags());
        }
        if (MicrocodeSignals.check(microcommand, MicrocodeSignals.PS_LATCH_WORD)) {
            ps.setValue(busD.getValue());
        }
        if (decoderSignals.eiInstruction() && !ecuSignals.exc_triggered()) {
            ps.setInterrupt();
        }
        if (decoderSignals.diInstruction() && !ecuSignals.exc_triggered()) {
            ps.clearInterrupt();
        }
        if (MicrocodeSignals.check(microcommand, MicrocodeSignals.R_LATCH)) {
            registerFile.setRegisterValue(decoderSignals.rd(), busD.getValue());
        }

        if (MicrocodeSignals.check(microcommand, MicrocodeSignals.PC_INC)) {
            boolean pc_int_inhibit;

            if (ecuSignals.exc_triggered()) {
                pc_int_inhibit = virtualInstructionLatch.getValue();
            } else {
                pc_int_inhibit = decoderSignals.br_rel_nop();
            }

            if (!pc_int_inhibit) {
                if (ecuSignals.exc_triggered()) {
                    pc.dec(2);
                } else {
                    pc.inc(2);
                }
            }
        }
        if (MicrocodeSignals.check(microcommand, MicrocodeSignals.SP_INC)) {
            sp.inc(2);
        }
        if (MicrocodeSignals.check(microcommand, MicrocodeSignals.SP_DEC)) {
            sp.dec(2);
        }
    }

    protected void updateDatapath() {
        int imm = ImmComputationUnit.computeImmediate(
                decoderSignals.imm_d(),
                microcommand,
                decoderSignals.imm_type(),
                decoderSignals.intInstruction(),
                phase
        );

        if (MicrocodeSignals.check(microcommand, MicrocodeSignals.R_ASRT0)) {
            bus0.setValue(registerFile.getRegisterValue(decoderSignals.rs0()));
        }
        if (MicrocodeSignals.check(microcommand, MicrocodeSignals.R_ASRT1)) {
            bus1.setValue(registerFile.getRegisterValue(decoderSignals.rs1()));
        }
        if (MicrocodeSignals.check(microcommand, MicrocodeSignals.R_ASRTD)) {
            busD.setValue(registerFile.getRegisterValue(decoderSignals.rd()));
        }
        if (MicrocodeSignals.check(microcommand, MicrocodeSignals.FP_ASRT0)) {
            bus0.setValue(fp.getValue());
        }
        if (MicrocodeSignals.check(microcommand, MicrocodeSignals.IMM_ASRT1)) {
            bus1.setValue(imm);
        }
        if (MicrocodeSignals.check(microcommand, MicrocodeSignals.IMM_ASRTD)) {
            busD.setValue(imm);
        }
        if (MicrocodeSignals.check(microcommand, MicrocodeSignals.SP_ASRT0)) {
            if (MicrocodeSignals.check(microcommand, MicrocodeSignals.SP_DEC)) {
                RegisterCounter spClone = sp.clone();
                spClone.dec(2);
                bus0.setValue(spClone.getValue());
            } else {
                bus0.setValue(sp.getValue());
            }
        }
        if (MicrocodeSignals.check(microcommand, MicrocodeSignals.SP_ASRTD)) {
            if (MicrocodeSignals.check(microcommand, MicrocodeSignals.SP_DEC)) {
                RegisterCounter spClone = sp.clone();
                spClone.dec(2);
                busD.setValue(spClone.getValue());
            } else {
                busD.setValue(sp.getValue());
            }
        }
        if (MicrocodeSignals.check(microcommand, MicrocodeSignals.PC_ASRT0)) {
            bus0.setValue(pc.getValue());
        }
        if (MicrocodeSignals.check(microcommand, MicrocodeSignals.PC_ASRTD)) {
            if (decoderSignals.jsrInstruction()
                    && MicrocodeSignals.check(microcommand, MicrocodeSignals.PC_ASRTD)) {
                RegisterCounter pcClone = pc.clone();
                pcClone.inc(2);
                busD.setValue(pcClone.getValue());
            } else {
                busD.setValue(pc.getValue());
            }
        }
        if (MicrocodeSignals.check(microcommand, MicrocodeSignals.PS_ASRTD)) {
            busD.setValue(ps.getValue());
        }

        boolean cIn;

        if (decoderSignals.arith_carry()) {
            cIn = ps.getCarry();
        } else {
            cIn = busController.inc_address() && MicrocodeSignals.check(microcommand, MicrocodeSignals.MEM);
        }

        aluSignals = Alu.compute(new AluInputParameters(
                bus0.getValue(),
                bus1.getValue(),
                cIn,
                decoderSignals.alu_func(),
                decoderSignals.alu_op_type(),
                decoderSignals.shift_count_d()
        ));

        busA.setValue(aluSignals.S());

        if (MicrocodeSignals.check(microcommand, MicrocodeSignals.ALU_ASRTD)) {
            busD.setValue(busA.getValue());
        }
    }

    protected int readDataBus(InstanceState state) {
        if (state.getPort(Ports.DATA_IN).isFullyDefined()) {
            return state.getPort(Ports.DATA_IN).toIntValue();
        } else {
            return 0;
        }
    }

    protected void updateExternal(InstanceState state) {
        for (int i = 0; i < registerFile.getRegisterCount(); ++i) {
            state.setPort(
                    Ports.R0 + i,
                    Value.createKnown(BitWidth.create(16), registerFile.getRegisterValue(i)),
                    DELAY
            );
        }

        state.setPort(Ports.PC, Value.createKnown(BitWidth.create(16), pc.getValue()), DELAY);
        state.setPort(Ports.SP, Value.createKnown(BitWidth.create(16), sp.getValue()), DELAY);
        state.setPort(Ports.PS, Value.createKnown(BitWidth.create(16), ps.getValue()), DELAY);

        state.setPort(Ports.STATUS, Value.createKnown(BitWidth.create(2), status), DELAY);

        if (fetch) {
            state.setPort(Ports.FETCH, Value.TRUE, DELAY);
        } else {
            state.setPort(Ports.FETCH, Value.FALSE, DELAY);
        }

        if (MicrocodeSignals.check(microcommand, MicrocodeSignals.WORD)
                && !(busControllerSignals.phase() || busControllerSignals.clk_inhibit())) {
            state.setPort(Ports.WORD, Value.TRUE, DELAY);
        } else {
            state.setPort(Ports.WORD, Value.FALSE, DELAY);
        }

        if (MicrocodeSignals.check(microcommand, MicrocodeSignals.DATA)) {
            state.setPort(Ports.DATA, Value.TRUE, DELAY);
        } else {
            state.setPort(Ports.DATA, Value.FALSE, DELAY);
        }

        if (MicrocodeSignals.check(microcommand, MicrocodeSignals.READ)) {
            state.setPort(Ports.READ, Value.TRUE, DELAY);
        } else {
            state.setPort(Ports.READ, Value.FALSE, DELAY);
        }

        if (MicrocodeSignals.check(microcommand, MicrocodeSignals.MEM)) {
            state.setPort(Ports.MEM, Value.TRUE, DELAY);
        } else {
            state.setPort(Ports.MEM, Value.FALSE, DELAY);
        }

        if (ecuSignals.int_ack()) {
            state.setPort(Ports.IAck, Value.TRUE, DELAY);
        } else {
            state.setPort(Ports.IAck, Value.FALSE, DELAY);
        }

        state.setPort(Ports.ADDRESS, Value.createKnown(BitWidth.create(16), busA.getValue()), DELAY);

        /*if (!MicrocodeSignals.check(microcommand, MicrocodeSignals.MEM)) {
            return;
        }*/

        state.setPort(
                Ports.DATA_OUT,
                Value.createKnown(BitWidth.create(16), busControllerSignals.data_out()),
                DELAY
        );
    }

    protected void updateExceptionLatches(InstanceState state) {
        if (toBoolean(state.getPort(Ports.EXC))) {
            externalExceptionVectorRegister.setValue(state.getPort(Ports.EXC_NUMBER).toIntValue());
        }

        if (ecuSignals.exc_internal_vec_reg_en()) {
            internalExceptionVectorRegister.setValue(ecuSignals.exc_internal_vec_reg_output());
        }

        boolean set = ecuSignals.exc_latch_output();
        boolean reset = ecuSignals.reset_exc();

        if (set && !reset) {
            exceptionLatch.set();
        } else if (!set && reset) {
            exceptionLatch.reset();
        }
    }

    protected void updateClockControlLatches(
            boolean halt,
            boolean wait,
            boolean irq,
            boolean critical_fault
    ) {
        if (wait && !irq) {
            waitLatch.set();
        }

        if (halt) {
            haltLatch.set();
        }

        if (critical_fault) {
            faultLatch.set();
        }
    }

    protected void updateWaitLatch(boolean irq) {
        if (waitLatch.getValue() && irq) {
            waitLatch.reset();
        }
    }

    protected void updateStatus() {
        List<Integer> enabledLatches = new ArrayList<>();
        enabledLatches.add(Status.RUNNING);

        if (waitLatch.getValue()) {
            enabledLatches.add(Status.WAITING);
        }

        if (haltLatch.getValue()) {
            enabledLatches.add(Status.HALTED);
        }

        if (faultLatch.getValue()) {
            enabledLatches.add(Status.FAULT);
        }

        status = enabledLatches
                .stream()
                .max(Integer::compareTo)
                .get();
    }


    protected boolean clockSuspended() {
        return haltLatch.getValue() ||
                faultLatch.getValue() ||
                holdLatch.getValue() ||
                waitLatch.getValue();
    }

    public static class ALU_InstructionGroups {
        public static final int ALU_3 = 1;
        public static final int ALU_2 = 1 << 1;
        public static final int SHIFTS = 1 << 2;
    }

    public static class ALU_Shifts {
        public static final int SHL = 0;
        public static final int SHR = 1;
        public static final int SHRA = 2;
        public static final int ROL = 3;
        public static final int ROR = 4;
        public static final int RCL = 5;
        public static final int RCR = 6;
    }

    public static class ALU_3op {
        public static final int AND = 0;
        public static final int OR = 1;
        public static final int XOR = 2;
        public static final int BIC = 3;
        public static final int ADD = 4;
        public static final int ADC = 5;
        public static final int SUB = 6;
        public static final int SBC = 7;
    }

    public static class ALU_2op {
        public static final int NEG = 0;
        public static final int NOT = 1;
        public static final int SXT = 2;
        public static final int SCL = 3;
    }


    public static class IMM_Type {
        public static final int IMM_6 = 0;
        public static final int IMM_9 = 1;
    }

    public static class ExceptionNumbers {
        public static final int UNALIGNED_SP = 1;
        public static final int UNALIGNED_PC = 2;
        public static final int INVALID_INST = 3;
        public static final int DOUBLE_FAULT = 4;
        public static final int EXTERNAL_EXC = 7;
    }

    public static class InstructionGroups {
        public static final int ZERO_OP = 0x00;
        public static final int ONE_OP = 0x10;
        public static final int TWO_OP = 0x20;
        public static final int MEM_2 = 0x30;
        public static final int IMM_6 = 0x40;
        public static final int IMM_9 = 0x50;
        public static final int MEM_3 = 0x60;
    }


    public static class Instructions {
        public static final int BR_ABS = 0x70;
        public static final int SHIFTS = 0x71;
        public static final int ALU_2 = 0x71;
        public static final int ALU_3_IND = 0x72;
        public static final int ALU_3 = 0x73;
        public static final int BR_REL_P = 0x74;
        public static final int BR_REL_N = 0x75;
        public static final int BR_ABS_NOP = 0x76;
        public static final int BR_REL_NOP = 0x76;
        public static final int FETCH = 0x77;
    }

    public static class MicrocodeSignals {
        public static final int ALU_ASRTD = 1;
        public static final int DATA = 1 << 1;
        public static final int FP_ASRT0 = 1 << 2;
        public static final int IMM_ASRT1 = 1 << 3;
        public static final int IMM_ASRTD = 1 << 4;
        public static final int IMM_EXTEND_NEGATIVE = 1 << 5;
        public static final int IMM_SHIFT = 1 << 6;
        public static final int MEM = 1 << 7;
        public static final int PC_ASRT0 = 1 << 8;
        public static final int PC_ASRTD = 1 << 9;
        public static final int PC_INC = 1 << 10;
        public static final int PC_LATCH = 1 << 11;
        public static final int PS_ASRTD = 1 << 12;
        public static final int PS_LATCH_FLAGS = 1 << 13;
        public static final int PS_LATCH_WORD = 1 << 14;
        public static final int R_ASRT0 = 1 << 15;
        public static final int R_ASRT1 = 1 << 16;
        public static final int R_ASRTD = 1 << 17;
        public static final int R_LATCH = 1 << 18;
        public static final int READ = 1 << 19;
        public static final int SIGN_EXTEND = 1 << 20;
        public static final int SP_ASRT0 = 1 << 21;
        public static final int SP_ASRTD = 1 << 22;
        public static final int SP_DEC = 1 << 23;
        public static final int SP_INC = 1 << 24;
        public static final int SP_LATCH = 1 << 25;
        public static final int WORD = 1 << 26;
        public static final int CUT = 1 << 27;

        public static boolean check(int value, int signal) {
            return (value & signal) > 0;
        }
    }
}
