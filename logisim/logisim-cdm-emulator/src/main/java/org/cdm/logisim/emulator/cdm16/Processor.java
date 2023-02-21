package org.cdm.logisim.emulator.cdm16;

import com.cburch.logisim.data.BitWidth;
import com.cburch.logisim.data.Value;
import com.cburch.logisim.instance.InstanceState;
import org.cdm.logisim.emulator.ExceptionHandler;
import org.cdm.logisim.emulator.InterruptHandler;
import org.cdm.logisim.emulator.GenericProcessor;

import java.util.HashMap;
import java.util.Map;

public class Processor implements GenericProcessor, ExceptionHandler, InterruptHandler {

    public static int MAX_INT = 0xFFFF;
    public static int DELAY = 1;

    private int[] mainMicrocode;
    private int[] exceptionMicrocode;

    private int microcommand;

    private boolean initialized = false;

    private Map<String, Integer> signals = new HashMap<>();

    private ProcessorState state = new ProcessorState();

    private Register[] gpRegisters = state.registers;
    private Register fp = state.fp;
    private RegisterCounter pc = state.pc;
    private RegisterCounter sp = state.sp;
    private StatusRegister ps = state.ps;

    private Register ir = new Register("ir");

    private boolean fetch;

    private int phase;

    private Bus bus0 = new Bus("bus0");
    private Bus bus1 = new Bus("bus1");
    private Bus busA = new Bus("busA");
    private Bus busD = new Bus("busD", false);

    private Bus[] buses = new Bus[] {
            bus0,
            bus1,
            busD,
            busA
    };

    //private boolean br_rel_nop;

    //private int alu_func;
    //private int shift_count_d;
    //private int alu_op_type;

    //private boolean arith_carry;

    //private int imm;
    //private int imm_type;

    //private int rd;
    //private int rs0;
    //private int rs1;

    //private int alu_flags;

    public Processor() {
        // Insert path to microcode
        mainMicrocode = MicrocodeLoader.loadFromFile("");
    }

    public void externalInterrupt(InstanceState state, int interruptNumber) {
        //System.out.println("externalInterrupt" + interruptNumber);
    }

    public void externalException(InstanceState state, int exceptionNumber) {
        //System.out.println("externalException " + exceptionNumber);
    }

    public void clockRising(InstanceState state) {
        //System.out.println("clockRising");
    }

    public void clockFalling(InstanceState state) {
        //System.out.println("clockFalling");

        updateRegisters();

        for (Bus bus : buses) {
            bus.clear();
        }

        if (MicrocodeSignals.check(microcommand, MicrocodeSignals.CUT)) {
            phase = 0;
            fetch = !fetch;
        } else {
            phase++;
        }

        int microcommandAddress = phase << 7;

        if (fetch) {
            microcommandAddress += Instructions.FETCH;
            signals.put("alu_op_type", ALU_InstructionGroups.ALU_3);
            signals.put("alu_func", ALU_3op.ADC);
        } else {
            microcommandAddress += decodeInstruction(ir.getValue());
        }

        microcommand = mainMicrocode[microcommandAddress];

        updateDatapath();
    }

    public void update(InstanceState state) {
        //System.out.println("update");

        if (!initialized) {
            initialize();
        }

        updateExternal(state);
    }

    private void initialize() {
        initialized = true;

        fetch = true;

        microcommand = mainMicrocode[Instructions.FETCH];
        signals.put("alu_op_type", ALU_InstructionGroups.ALU_3);
        signals.put("alu_func", ALU_3op.ADC);

        updateDatapath();
    }

    private void updateExternal(InstanceState state) {
        for (int i = 0; i < gpRegisters.length; ++i) {
            state.setPort(Ports.R0 + i, Value.createKnown(BitWidth.create(16), gpRegisters[i].getValue()), DELAY);
        }

        state.setPort(Ports.PC, Value.createKnown(BitWidth.create(16), pc.getValue()), DELAY);
        state.setPort(Ports.SP, Value.createKnown(BitWidth.create(16), sp.getValue()), DELAY);
        state.setPort(Ports.PS, Value.createKnown(BitWidth.create(16), ps.getValue()), DELAY);

        if (fetch) {
            state.setPort(Ports.FETCH, Value.TRUE, DELAY);
        } else {
            state.setPort(Ports.FETCH, Value.FALSE, DELAY);
        }

        if (MicrocodeSignals.check(microcommand, MicrocodeSignals.WORD)) {
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

        state.setPort(Ports.ADDRESS, Value.createKnown(BitWidth.create(16), busA.getValue()), DELAY);

        if (!MicrocodeSignals.check(microcommand, MicrocodeSignals.MEM)) {
            return;
        }

        if (MicrocodeSignals.check(microcommand, MicrocodeSignals.READ)) {
            int externalBusD = state.getPort(Ports.DATA_IN).toIntValue();

            if (MicrocodeSignals.check(microcommand, MicrocodeSignals.SIGN_EXTEND)) {
                externalBusD = signExtend(externalBusD);
            }

            busD.setValue(externalBusD);
        } else {
            state.setPort(Ports.DATA_OUT, Value.createKnown(BitWidth.create(16), busD.getValue()), DELAY);
        }
    }

    private void updateRegisters() {
        if (MicrocodeSignals.check(microcommand, MicrocodeSignals.PC_LATCH)) {
            pc.setValue(busD.getValue());
        }
        if (MicrocodeSignals.check(microcommand, MicrocodeSignals.SP_LATCH)) {
            sp.setValue(busD.getValue());
        }
        if (MicrocodeSignals.check(microcommand, MicrocodeSignals.PS_LATCH_FLAGS)) {
            ps.setFlags(busD.getValue());
        }
        if (MicrocodeSignals.check(microcommand, MicrocodeSignals.PS_LATCH_WORD)) {
            ps.setWord(busD.getValue());
        }
        if (MicrocodeSignals.check(microcommand, MicrocodeSignals.R_LATCH)) {
            gpRegisters[signals.get("rd")].setValue(busD.getValue());
        }

        if (fetch) {
            ir.setValue(busD.getValue());
        }

        if (MicrocodeSignals.check(microcommand, MicrocodeSignals.PC_INC)) {
            Integer br_rel_nop = signals.get("br_rel_nop");
            if (br_rel_nop == null || br_rel_nop == 0) {
                pc.inc(2);
            }
        }
        if (MicrocodeSignals.check(microcommand, MicrocodeSignals.SP_INC)) {
            sp.inc(2);
        }
        if (MicrocodeSignals.check(microcommand, MicrocodeSignals.SP_DEC)) {
            sp.dec(2);
        }
    }

    private void updateDatapath() {
        if (MicrocodeSignals.check(microcommand, MicrocodeSignals.IMM_EXTEND_NEGATIVE)) {
            int imm = signals.get("imm");

            if (signals.get("imm_type") == IMM_Type.IMM_6) {
                imm |= 0b1111111111000000;
            } else {
                imm |= 0b1111111000000000;
            }

            signals.put("imm", imm);
        }

        if (MicrocodeSignals.check(microcommand, MicrocodeSignals.IMM_SHIFT)) {
            int imm = signals.get("imm");

            imm <<= 1;

            signals.put("imm", imm);
        }

        if (MicrocodeSignals.check(microcommand, MicrocodeSignals.R_ASRT0)) {
            bus0.setValue(gpRegisters[signals.get("rs0")].getValue());
        }
        if (MicrocodeSignals.check(microcommand, MicrocodeSignals.R_ASRT1)) {
            bus1.setValue(gpRegisters[signals.get("rs1")].getValue());
        }
        if (MicrocodeSignals.check(microcommand, MicrocodeSignals.R_ASRTD)) {
            busD.setValue(gpRegisters[signals.get("rd")].getValue());
        }
        if (MicrocodeSignals.check(microcommand, MicrocodeSignals.FP_ASRT0)) {
            bus0.setValue(fp.getValue());
        }
        if (MicrocodeSignals.check(microcommand, MicrocodeSignals.IMM_ASRT1)) {
            bus1.setValue(signals.get("imm"));
        }
        if (MicrocodeSignals.check(microcommand, MicrocodeSignals.IMM_ASRTD)) {
            busD.setValue(signals.get("imm"));
        }
        if (MicrocodeSignals.check(microcommand, MicrocodeSignals.SP_ASRT0)) {
            bus0.setValue(sp.getValue());
        }
        if (MicrocodeSignals.check(microcommand, MicrocodeSignals.SP_ASRTD)) {
            busD.setValue(sp.getValue());
        }
        if (MicrocodeSignals.check(microcommand, MicrocodeSignals.PC_ASRT0)) {
            bus0.setValue(pc.getValue());
        }
        if (MicrocodeSignals.check(microcommand, MicrocodeSignals.PC_ASRTD)) {
            busD.setValue(pc.getValue());
        }
        if (MicrocodeSignals.check(microcommand, MicrocodeSignals.PS_ASRTD)) {
            busD.setValue(ps.getValue());
        }

        alu();

        if (MicrocodeSignals.check(microcommand, MicrocodeSignals.ALU_ASRTD)) {
            busD.setValue(busA.getValue());
        }
    }

    private int decodeInstruction(int instruction) {
        int inst_group = (instruction >> 13) & 0b111; // higher 3 bits

        boolean X =  ((instruction >> 12) & 1) > 0; // 12th bit
        boolean Y = ((instruction >> 11) & 1) > 0; // 11th bit

        int op_type_d0 = instruction & 0b1111;
        int op_type_d1 = (instruction >> 3) & 0b1111;
        int op_type_d2 = (instruction >> 6) & 0b1111;
        int op_type_d3 = (instruction >> 9) & 0b1111;

        int br_abs_flags_d = op_type_d0;
        int br_rel_flags_d = op_type_d3;

        int rd_d = instruction & 0b111;
        int rs0_d = (instruction >> 3) & 0b111;
        int rs1_d = (instruction >> 6) & 0b111;

        int alu_op_d0 = rs1_d;
        int alu_op_d1 = (instruction >> 9) & 0b111;

        int microcode_address = 0;

        int switch_alu_func0 = 0;
        int switch_alu_func1 = 0;

        int imm6_d = (instruction >> 3) & 0b111111;
        int imm9_d = instruction & 0b111111111;

        signals.put("shift_count_d", rs1_d);

        switch (inst_group) {
            case 0b000:
                if (X) {
                    microcode_address = Instructions.SHIFTS;
                    signals.put("alu_op_type", ALU_InstructionGroups.SHIFTS);
                    switch_alu_func0 = 1;
                } else {
                    if (Y) {
                        if (checkFlags(br_abs_flags_d)) {
                            microcode_address = Instructions.BR_ABS;
                        } else {
                            microcode_address = Instructions.BR_ABS_NOP;
                        }
                    } else {
                        microcode_address = InstructionGroups.ZERO_OP + op_type_d0;
                    }
                }
                break;

            case 0b001:
                microcode_address = InstructionGroups.ONE_OP + op_type_d1;

            case 0b010:
                if (X) {
                    if (Y) {
                        microcode_address = Instructions.ALU_2;
                        signals.put("alu_op_type", ALU_InstructionGroups.ALU_2);
                        switch_alu_func1 = 1;
                    } else {
                        microcode_address = InstructionGroups.MEM_2 + op_type_d2;
                    }
                } else {
                    if (Y) {
                        microcode_address = Instructions.ALU_3_IND;
                        signals.put("alu_op_type", ALU_InstructionGroups.ALU_3);
                        signals.put("rs1", rd_d);
                        switch_alu_func1 = 1;
                    } else {
                        microcode_address = InstructionGroups.TWO_OP + op_type_d2;
                    }
                }
                break;

            case 0b011:
                microcode_address = InstructionGroups.IMM_6 + op_type_d3;
                signals.put("rs0", rd_d);
                signals.put("imm_type", IMM_Type.IMM_6);
                break;

            case 0b100:
                microcode_address = InstructionGroups.IMM_9 + op_type_d3;
                break;

            case 0b101:
                if (X) {
                    microcode_address = Instructions.ALU_3;
                    signals.put("alu_op_type", ALU_InstructionGroups.ALU_3);
                    switch_alu_func0 = 1;
                } else {
                    microcode_address = InstructionGroups.MEM_3 + op_type_d3;
                }
                break;

            case 0b110:
                if (checkFlags(br_rel_flags_d)) {
                    microcode_address = Instructions.BR_REL_N;
                } else {
                    microcode_address = Instructions.BR_REL_NOP;
                    signals.put("br_rel_nop", 1);
                }
                break;

            case 0b111:
                if (checkFlags(br_rel_flags_d)) {
                    microcode_address = Instructions.BR_REL_P;
                } else {
                    microcode_address = Instructions.BR_REL_NOP;
                    signals.put("br_rel_nop", 1);
                }
                break;
        }

        if (signals.get("alu_op_type") == null) {
            signals.put("alu_op_type", ALU_InstructionGroups.ALU_3);
        }

        signals.put("rd", rd_d);

        if (signals.get("rs1") == null) {
            signals.put("rs1", rs1_d);
        }

        if (signals.get("rs0") == null) {
            signals.put("rs0", rs0_d);
        }

        signals.put("arith_carry", switch_alu_func0);

        if ((switch_alu_func0 > 0) || (switch_alu_func1 > 0)) {
            if ((switch_alu_func1 > 0)) {
                signals.put("alu_func", alu_op_d0);
            } else {
                signals.put("alu_func", alu_op_d1);
            }
        } else {
            if ((microcode_address & 0b1110000) == InstructionGroups.IMM_6 || op_type_d3 >= 0b1110) {
                signals.put("alu_func", ALU_3op.SUB);
            } else {
                signals.put("alu_func", ALU_3op.ADC);
            }
        }

        if (signals.get("imm_type") == null) {
            signals.put("imm_type", IMM_Type.IMM_9);
        }

        if (signals.get("imm_type") ==  IMM_Type.IMM_6) {
            signals.put("imm", imm6_d);
        } else if (signals.get("imm_type") ==  IMM_Type.IMM_9) {
            signals.put("imm", imm9_d);
        }

        return microcode_address;
    }

    private boolean checkFlags(int flags) {
        int cccc = flags & 0x000F;
        int reverse = cccc & 1;
        int ccc = cccc >> 1;

        int psFlags = ps.getFlags();

        int C = (psFlags >> 3) & 1;
        int V = (psFlags >> 2) & 1;
        int Z = (psFlags >> 1) & 1;
        int N = (psFlags >> 0) & 1;

        int dcsn = 0;

        switch (ccc) {
            case 0:
                dcsn = Z;
                break;
            case 1:
                dcsn = C;
                break;
            case 2:
                dcsn = N;
                break;
            case 3:
                dcsn = V;
                break;
            case 4:
                dcsn = C & (~Z) & 1;
                break;
            case 5:
                dcsn = ~(N ^ V) & 1;
                break;
            case 6:
                dcsn = (~Z) & ~(N ^ V) & 1;
                break;
            case 7:
                dcsn = 1;
                break;
        }

        dcsn = reverse ^ dcsn;

        return dcsn != 0;
    }

    private int signExtend(int value) {
        if ((value & 0xFF) >= 0x80) {
            return value | 0xFF00;
        } else {
            return value & 0xFF;
        }
    }

    private void alu() {
        if (!bus0.isSet()) {
            bus0.setValue(0);
        }

        if (!bus1.isSet()) {
            bus1.setValue(0);
        }

        Integer op_type = signals.get("alu_op_type");
        Integer func = signals.get("alu_func");

        if (op_type == null || func == null) {
            System.err.println("ALU signals are not calculated yet!");
            busA.setValue(0);
            return;
        }

        Integer rs0 = bus0.getValue();
        Integer rs1 = bus1.getValue();

        Integer rd = 0;

        Integer arith_carry = signals.get("arith_carry");
        Integer cIn = 0;
        Integer cOut = 0;

        if (arith_carry != null && arith_carry > 0) {
            cIn = (ps.getFlags() >> 3) & 1;
        }

        switch (op_type) {
            case ALU_InstructionGroups.ALU_3:
                switch (func) {
                    case ALU_3op.AND:
                        rd = rs0 & rs1;
                        break;
                    case ALU_3op.OR:
                        rd = rs0 | rs1;
                        break;
                    case ALU_3op.XOR:
                        rd = rs0 ^ rs1;
                        break;
                    case ALU_3op.BIC:
                        rd = rs0 & (~rs1);
                        break;
                    case ALU_3op.ADD:
                        rd = rs0 + rs1;
                        break;
                    case ALU_3op.ADC:
                        rd = rs0 + rs1 + cIn;
                        break;
                    case ALU_3op.SUB:
                        rd = rs0 - rs1;
                        break;
                    case ALU_3op.SBC:
                        rd = rs0 - rs1 + cIn - 1;
                        break;
                }
                break;
            case ALU_InstructionGroups.ALU_2:
                switch (func) {
                    case ALU_2op.NEG:
                        rd = -rs0;
                        break;
                    case ALU_2op.NOT:
                        rd = ~rs0;
                        break;
                    case ALU_2op.SXT:
                        rd = signExtend(rs0);
                        break;
                    case ALU_2op.SCL:
                        rd = rs0 & 0x00FF;
                        break;
                }
                break;
            case ALU_InstructionGroups.SHIFTS:
                Integer shiftCount = signals.get("shift_count_d");

                if (shiftCount != null) {
                    shiftCount++;
                } else {
                    System.err.println("shift_count_d is not calculated");
                    return;
                }

                switch (func) {
                    case ALU_Shifts.SHL:
                        rd = rs0 << shiftCount;
                        break;
                    case ALU_Shifts.SHR:
                        rd = rs0 >>> shiftCount;
                        break;
                    case ALU_Shifts.SHRA:
                        rd = rs0 >> shiftCount;
                        break;
                    case ALU_Shifts.ROL:
                        rd = (rs0 << shiftCount) | (rs0 >> (16 - shiftCount));
                        break;
                    case ALU_Shifts.ROR:
                        rd = (rs0 >> shiftCount) | (rs0 << (16 - shiftCount));
                        break;
                    case ALU_Shifts.RCL:
                        rd = (rs0 << shiftCount) | (cIn << shiftCount - 1) | (rs0 >> (16 - shiftCount + 1));
                        break;
                    case ALU_Shifts.RCR:
                        rd = (rs0 >> shiftCount) | (cIn << (16 - shiftCount)) | (rs0 << (16 - shiftCount + 1));
                        break;
                }
                break;
        }

        busA.setValue(rd);
    }

    private int encodeFlags(int C, int V, int Z, int N) {

        C &= 1;
        V &= 1;
        Z &= 1;
        N &= 1;

        return (C << 3) | (V << 2) | (Z << 1) | N;
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
        public static final int ROR = 3;
        public static final int ROL = 4;
        public static final int RCR = 5;
        public static final int RCL = 6;
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
        public static final int BR_REL_N = 0x74;
        public static final int BR_REL_P = 0x75;
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
