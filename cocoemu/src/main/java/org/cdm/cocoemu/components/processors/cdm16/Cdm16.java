package org.cdm.cocoemu.components.processors.cdm16;

import lombok.AccessLevel;
import lombok.ToString;
import lombok.experimental.FieldDefaults;
import org.cdm.cocoemu.components.processors.MicrocodeLoader;
import org.cdm.cocoemu.components.processors.Processor;
import org.cdm.cocoemu.components.processors.cdm16.units.FetchUnit;
import org.cdm.cocoemu.components.processors.cdm16.units.ImmComputationUnit;
import org.cdm.cocoemu.components.processors.cdm16.units.alu.Alu;
import org.cdm.cocoemu.components.processors.cdm16.units.alu.AluInputParameters;
import org.cdm.cocoemu.components.processors.cdm16.units.alu.AluOutputParameters;
import org.cdm.cocoemu.components.processors.cdm16.units.bus.BusController;
import org.cdm.cocoemu.components.processors.cdm16.units.bus.BusControllerInputParameters;
import org.cdm.cocoemu.components.processors.cdm16.units.bus.BusControllerOutputParameters;
import org.cdm.cocoemu.components.processors.cdm16.units.decoder.InstructionDecoder;
import org.cdm.cocoemu.components.processors.cdm16.units.decoder.InstructionDecoderInputParameters;
import org.cdm.cocoemu.components.processors.cdm16.units.decoder.InstructionDecoderOutputParameters;
import org.cdm.cocoemu.components.processors.cdm16.units.exceptions.*;
import org.cdm.cocoemu.core.PortedComponentBase;
import org.cdm.cocoemu.core.ports.InputsClass;
import org.cdm.cocoemu.core.ports.InputsField;
import org.cdm.cocoemu.core.ports.OutputsClass;
import org.cdm.cocoemu.core.ports.OutputsField;
import org.cdm.cocoemu.core.primitives.*;

import java.util.ArrayList;
import java.util.List;

import static org.cdm.cocoemu.components.processors.cdm16.Arithmetic.toBoolean;

@ToString
@Processor
public class Cdm16 extends PortedComponentBase {

    @InputsField
    public Cdm16.Inputs inputs;
    @OutputsField
    public Cdm16.Outputs outputs;

    public static final int BIT_WIDTH = 16;

    protected static final int MICROCODE_LENGTH = 1024;

    private static final int EXTERNAL_EXCEPTION_VECTOR_REGISTER_WIDTH = 6;
    private static final int INTERNAL_EXCEPTION_VECTOR_REGISTER_WIDTH = 3;

    private static final int INTERRUPT_BIT_POS = 15;

    private static final int MAX_PHASE = 7;

    private static final String MAIN_MICROCODE = "/cdm16/cdm16_decoder.img";
    private static final String EXC_MICROCODE = "/cdm16/cdm16_decoder_exc.img";

    @ToString.Exclude
    protected int[] mainMicrocode;
    @ToString.Exclude
    protected int[] exceptionMicrocode;

    protected int microcommand;

    protected int microcommandAddress;

    protected final RegisterFile registerFile = new RegisterFile();

    protected final Register fp = registerFile.getFramePointer();
    protected final RegisterCounter pc = new RegisterCounter("pc", BIT_WIDTH);
    protected final StatusRegister ps = new StatusRegister("ps", BIT_WIDTH, INTERRUPT_BIT_POS);

    protected RegisterCounter sp = new RegisterCounter("sp", BIT_WIDTH);

    protected final Register ir = new Register("ir", BIT_WIDTH);

    protected boolean clockState = false;

    protected boolean fetch = true;

    protected int status = Status.RUNNING;

    protected int phase = 0;

    protected final Bus bus0 = new Bus("bus0", BIT_WIDTH);
    protected final Bus bus1 = new Bus("bus1", BIT_WIDTH);
    protected final Bus busA = new Bus("busA", BIT_WIDTH);
    protected final Bus busD = new Bus("busD", BIT_WIDTH);

    protected final Bus[] buses = new Bus[]{
            bus0,
            bus1,
            busD,
            busA
    };

    protected final Latch holdLatch = new Latch("hold_latch");
    protected final Latch waitLatch = new Latch("wait_latch");
    protected final Latch haltLatch = new Latch("halt_latch");
    protected final Latch faultLatch = new Latch("fault_latch");

    protected final Register externalExceptionVectorRegister =
            new Register("exc_vec_reg", EXTERNAL_EXCEPTION_VECTOR_REGISTER_WIDTH);

    protected final Register internalExceptionVectorRegister =
            new Register("exc_internal_vec_reg", INTERNAL_EXCEPTION_VECTOR_REGISTER_WIDTH);

    protected final Latch exceptionLatch = new Latch("exc_latch");
    protected final Latch startupLatch = new Latch("startup_latch");

    protected final Latch virtualInstructionLatch = new Latch("virtual_instruction_latch");

    protected final BusController busController = new BusController();

    protected InstructionDecoderOutputParameters decoderSignals;
    protected AluOutputParameters aluSignals;
    protected ExceptionControlUnitOutputParameters ecuSignals;
    protected BusControllerOutputParameters busControllerSignals;

    public Cdm16() {
        loadMicrocode();

        reset();
    }

    protected void loadMicrocode() {
        mainMicrocode = MicrocodeLoader.loadFromResources(MAIN_MICROCODE, MICROCODE_LENGTH);
        exceptionMicrocode = MicrocodeLoader.loadFromResources(EXC_MICROCODE, MICROCODE_LENGTH);
    }

    public void clockRising() {
        clockState = true;
    }

    public void clockFalling() {
        if (clockSuspended()) {
            updateWaitLatch(inputs.irq);
            updateStatus();

            return;
        }

        // Pre-latch
        updateProcessorState();

        // Latch
        updateExceptionLatches();

        updateClockControlLatches(
                decoderSignals.haltInstruction() && !ecuSignals.exc_triggered(),
                decoderSignals.waitInstruction() && !ecuSignals.exc_triggered(),
                inputs.irq,
                ecuSignals.critical_fault()
        );
        updateStatus();

        busController.clockFalling(
                readDataBus(),
                busControllerSignals.clk_inhibit()
        );

        if (busControllerSignals.clk_inhibit()) {
            return;
        }

        updateRegisters();

        if (fetch) {
            int instruction = FetchUnit.fetchInstruction(
                    busD.getValue(),
                    inputs.int_number,
                    internalExceptionVectorRegister.getValue(),
                    externalExceptionVectorRegister.getValue(),
                    inputs.exc_number,
                    ecuSignals.latch_double_fault(),
                    inputs.exc,
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

        clockState = false;
    }

    public void update() {
        updateProcessorState();

        updateExternal();
    }

    public void reset() {
        status = Status.RUNNING;

        phase = 0;
        fetch = true;

        decoderSignals = InstructionDecoder.getFetchSignals();
        microcommandAddress = decoderSignals.microcodeAddress();

        startupLatch.set();

        holdLatch.reset();
        waitLatch.reset();
        haltLatch.reset();
        faultLatch.reset();

        ps.setValue(0x0000);
    }

    protected void updateProcessorState() {
        if (!clockState) {
            holdLatch.setValue(inputs.hold);
        }

        microcommand = mainMicrocode[microcommandAddress];

        updateDatapath();

        busControllerSignals = busController.update(new BusControllerInputParameters(
                busD.getValue(),
                readDataBus(),
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


        boolean exc_trig_ext = inputs.exc;
        boolean irq = inputs.irq;

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

    protected int readDataBus() {
        return inputs.data_in;
    }

    protected void updateExternal() {
        for (int i = 0; i < registerFile.getRegisterCount(); ++i) {
            outputs.gpRegisters[i] = registerFile.getRegisterValue(i);
        }

        outputs.pc = pc.getValue();
        outputs.sp = sp.getValue();
        outputs.ps = ps.getValue();

        outputs.status = status;

        outputs.fetch = fetch;

        outputs.word = MicrocodeSignals.check(microcommand, MicrocodeSignals.WORD)
                && !(busControllerSignals.phase() || busControllerSignals.clk_inhibit());

        outputs.data = MicrocodeSignals.check(microcommand, MicrocodeSignals.DATA);
        outputs.read = MicrocodeSignals.check(microcommand, MicrocodeSignals.READ);
        outputs.mem = MicrocodeSignals.check(microcommand, MicrocodeSignals.MEM);

        outputs.iack = ecuSignals.int_ack();

        outputs.address = busA.getValue();

        /*if (!MicrocodeSignals.check(microcommand, MicrocodeSignals.MEM)) {
            return;
        }*/

        outputs.data_out = busControllerSignals.data_out();
    }

    protected void updateExceptionLatches() {
        if (inputs.exc) {
            externalExceptionVectorRegister.setValue(inputs.exc_number);
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

    // Debugger support
    public boolean exceptionHappened() {
        return ecuSignals.exc_triggered();
    }

    public int exceptionNumber() {
        int instruction = FetchUnit.fetchInstruction(
                busD.getValue(),
                inputs.int_number,
                internalExceptionVectorRegister.getValue(),
                externalExceptionVectorRegister.getValue(),
                inputs.exc_number,
                ecuSignals.latch_double_fault(),
                inputs.exc,
                ecuSignals.exc_triggered(),
                ecuSignals.latch_int(),
                startupLatch.getValue()
        );

        return instruction & 0b111111;
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


    @ToString
    @FieldDefaults(level = AccessLevel.PUBLIC)
    @InputsClass
    public static class Inputs {
        int data_in;
        boolean irq;
        int int_number;
        boolean exc;
        int exc_number;
        boolean hold;
    }

    @ToString
    @FieldDefaults(level = AccessLevel.PUBLIC)
    @OutputsClass
    public static class Outputs {
        int data_out;
        int address;
        boolean mem;
        boolean data;
        boolean read;
        boolean word;
        int status;
        boolean fetch;
        boolean iack;
        int[] gpRegisters = new int[8];
        int pc;
        int sp;
        int ps;
    }
}
