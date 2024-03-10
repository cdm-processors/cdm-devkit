package org.cdm.logisim.emulator.cdm16.units.alu;

import org.cdm.logisim.emulator.cdm16.Cdm16Processor;

import org.cdm.logisim.emulator.cdm16.Arithmetic;

import static org.cdm.logisim.emulator.cdm16.Arithmetic.normalize;
import static org.cdm.logisim.emulator.cdm16.Arithmetic.testBit;
import static org.cdm.logisim.emulator.cdm16.Arithmetic.toBoolean;
import static org.cdm.logisim.emulator.cdm16.Arithmetic.toInteger;

public class Alu {

    private static final int MAX_INT = Arithmetic.MAX_INT;

    public static AluOutputParameters compute(AluInputParameters parameters) {
        int rs0 = parameters.A();
        int rs1 = parameters.B();

        int rd = 0;

        int cIn = toInteger(parameters.cIn());

        int cOut = 0;
        int vOut = 0;

        int ZN;

        switch (parameters.alu_op_type()) {
            case Cdm16Processor.ALU_InstructionGroups.ALU_3:
                switch (parameters.alu_func()) {
                    case Cdm16Processor.ALU_3op.AND:
                        rd = rs0 & rs1;
                        break;
                    case Cdm16Processor.ALU_3op.OR:
                        rd = rs0 | rs1;
                        break;
                    case Cdm16Processor.ALU_3op.XOR:
                        rd = rs0 ^ rs1;
                        break;
                    case Cdm16Processor.ALU_3op.BIC:
                        rd = rs0 & (~rs1);
                        break;
                    case Cdm16Processor.ALU_3op.ADD:
                        rd = rs0 + rs1;
                        cOut = checkC(rd);
                        vOut = checkV(normalize(rd), rs0, rs1);
                        break;
                    case Cdm16Processor.ALU_3op.ADC:
                        rd = rs0 + rs1 + cIn;
                        cOut = checkC(rd);
                        vOut = checkV(normalize(rd), rs0, rs1 + cIn);
                        break;
                    case Cdm16Processor.ALU_3op.SUB:
                        rd = rs0 + (rs1 ^ 0xFFFF) + 1;
                        cOut = checkC(rd);
                        vOut = checkV(normalize(rd), rs0, (rs1 ^ 0xFFFF) + 1);
                        break;
                    case Cdm16Processor.ALU_3op.SBC:
                        rd = rs0 + (rs1 ^ 0xFFFF) + cIn;
                        cOut = checkC(rd);
                        vOut = checkV(normalize(rd), rs0, (rs1 ^ 0xFFFF) + cIn);
                        break;
                }
                break;
            case Cdm16Processor.ALU_InstructionGroups.ALU_2:
                switch (parameters.alu_func()) {
                    case Cdm16Processor.ALU_2op.NEG:
                        rd = (rs0 ^ 0xFFFF) + 1;
                        cOut = checkC(rd);
                        vOut = toInteger(rs0 == 0x8000);
                        break;
                    case Cdm16Processor.ALU_2op.NOT:
                        rd = ~rs0;
                        break;
                    case Cdm16Processor.ALU_2op.SXT:
                        rd = Arithmetic.signExtend(rs0);
                        break;
                    case Cdm16Processor.ALU_2op.SCL:
                        rd = rs0 & 0x00FF;
                        break;
                }
                break;
            case Cdm16Processor.ALU_InstructionGroups.SHIFTS:
                int shiftCount = parameters.shift_count_d();

                shiftCount++;

                switch (parameters.alu_func()) {
                    case Cdm16Processor.ALU_Shifts.SHL:
                        rd = rs0 << shiftCount;
                        cOut = toInteger(testBit(rs0, 16 - shiftCount));
                        break;
                    case Cdm16Processor.ALU_Shifts.SHR:
                        rd = rs0 >>> shiftCount;
                        cOut = toInteger(testBit(rs0, shiftCount - 1));
                        break;
                    case Cdm16Processor.ALU_Shifts.SHRA:
                        int sign = checkN(rs0);
                        int mask = toBoolean(sign) ? -1 : 0;
                        rd = (rs0 >> shiftCount) | (mask << 16 - shiftCount);
                        cOut = toInteger(testBit(rs0, shiftCount - 1));
                        break;
                    case Cdm16Processor.ALU_Shifts.ROL:
                        rd = (rs0 << shiftCount) | (rs0 >> (16 - shiftCount));
                        cOut = toInteger(testBit(rs0, 16 - shiftCount));
                        break;
                    case Cdm16Processor.ALU_Shifts.ROR:
                        rd = (rs0 >> shiftCount) | (rs0 << (16 - shiftCount));
                        cOut = toInteger(testBit(rs0, shiftCount - 1));
                        break;
                    case Cdm16Processor.ALU_Shifts.RCL:
                        rd = (rs0 << shiftCount) | (cIn << shiftCount - 1) | (rs0 >> (16 - shiftCount + 1));
                        cOut = toInteger(testBit(rs0, 16 - shiftCount));
                        break;
                    case Cdm16Processor.ALU_Shifts.RCR:
                        rd = (rs0 >> shiftCount) | (cIn << (16 - shiftCount)) | (rs0 << (16 - shiftCount + 1));
                        cOut = toInteger(testBit(rs0, shiftCount - 1));
                        break;
                }
                break;
        }

        rd = normalize(rd);

        ZN = checkZN(rd);

        return new AluOutputParameters(
                rd,
                encodeFlags(cOut, vOut, ZN)
        );
    }

    private static int encodeFlags(int C, int V, int Z, int N) {

        C &= 1;
        V &= 1;
        Z &= 1;
        N &= 1;

        return (C << 3) | (V << 2) | (Z << 1) | N;
    }

    private static int encodeFlags(int C, int V, int ZN) {

        C &= 1;
        V &= 1;
        ZN &= 0b11;

        return  (C << 3) | (V << 2) | ZN;
    }

    private static int checkZ(int value) {
        return value == 0 ? 1 : 0;
    }

    private static int checkN(int value) {
        return toInteger(testBit(value, 15));
    }

    private static int checkC(int value) {
        return toInteger(testBit(value, 16));
    }

    private static int checkV(int rd, int rs0, int rs1) {
        return ((rd > (MAX_INT >> 1)) && (rs0 <= (MAX_INT >> 1)) && (rs1 <= (MAX_INT >> 1))) ||
                ((rd <= (MAX_INT >> 1)) && (rs0 > (MAX_INT >> 1)) && (rs1 > (MAX_INT >> 1))) ? 1 : 0;
    }

    private static int checkZN(int value) {
        return (checkZ(value) << 1) | checkN(value);
    }

}
