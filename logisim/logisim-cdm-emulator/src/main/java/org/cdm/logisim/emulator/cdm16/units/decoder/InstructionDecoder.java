package org.cdm.logisim.emulator.cdm16.units.decoder;

import org.cdm.logisim.emulator.cdm16.Cdm16Processor;

import static org.cdm.logisim.emulator.cdm16.units.BranchUnit.checkFlags;

public class InstructionDecoder {
    public static InstructionDecoderOutputParameters compute(InstructionDecoderInputParameters parameters) {
        int instruction = parameters.instruction();

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

        boolean switch_alu_func0 = false;
        boolean switch_alu_func1 = false;

        int imm6_d = (instruction >> 3) & 0b111111;
        int imm9_d = instruction & 0b111111111;

        int shift_count_d = rs1_d;

        int rs0 = rs0_d;
        int rs1 = rs1_d;
        int rd = rd_d;

        int alu_op_type = Cdm16Processor.ALU_InstructionGroups.ALU_3;

        int imm_type = Cdm16Processor.IMM_Type.IMM_9;

        boolean br_rel_nop = false;

        boolean arith_carry;

        int alu_func;

        int imm_d;

        boolean intInstruction = false;
        boolean jsrInstruction = false;
        boolean rtiInstruction = false;
        boolean haltInstruction = false;
        boolean waitInstruction = false;
        boolean eiInstruction = false;
        boolean diInstruction = false;


        switch (inst_group) {
            case 0b000:
                if (X) {
                    microcode_address = Cdm16Processor.Instructions.SHIFTS;
                    alu_op_type = Cdm16Processor.ALU_InstructionGroups.SHIFTS;
                    switch_alu_func0 = true;
                } else {
                    if (Y) {
                        if (checkFlags(br_abs_flags_d, parameters.psFlags())) {
                            microcode_address = Cdm16Processor.Instructions.BR_ABS;
                        } else {
                            microcode_address = Cdm16Processor.Instructions.BR_ABS_NOP;
                        }
                    } else {
                        microcode_address = Cdm16Processor.InstructionGroups.ZERO_OP + op_type_d0;
                    }
                }
                break;

            case 0b001:
                microcode_address = Cdm16Processor.InstructionGroups.ONE_OP + op_type_d1;
                rs1 = rd_d;

                break;

            case 0b010:
                if (X) {
                    if (Y) {
                        microcode_address = Cdm16Processor.Instructions.ALU_2;
                        alu_op_type = Cdm16Processor.ALU_InstructionGroups.ALU_2;
                        switch_alu_func1 = true;
                    } else {
                        microcode_address = Cdm16Processor.InstructionGroups.MEM_2 + op_type_d2;
                    }
                } else {
                    if (Y) {
                        microcode_address = Cdm16Processor.Instructions.ALU_3_IND;
                        alu_op_type = Cdm16Processor.ALU_InstructionGroups.ALU_3;
                        rs1 = rd_d;
                        switch_alu_func1 = true;
                    } else {
                        microcode_address = Cdm16Processor.InstructionGroups.TWO_OP + op_type_d2;
                    }
                }
                break;

            case 0b011:
                microcode_address = Cdm16Processor.InstructionGroups.IMM_6 + op_type_d3;
                rs0 = rd_d;
                imm_type = Cdm16Processor.IMM_Type.IMM_6;

                break;

            case 0b100:
                microcode_address = Cdm16Processor.InstructionGroups.IMM_9 + op_type_d3;
                break;

            case 0b101:
                if (X) {
                    microcode_address = Cdm16Processor.Instructions.ALU_3;
                    alu_op_type = Cdm16Processor.ALU_InstructionGroups.ALU_3;
                    switch_alu_func0 = true;
                } else {
                    microcode_address = Cdm16Processor.InstructionGroups.MEM_3 + op_type_d3;
                }
                break;

            case 0b110:
                if (checkFlags(br_rel_flags_d, parameters.psFlags())) {
                    microcode_address = Cdm16Processor.Instructions.BR_REL_N;
                } else {
                    microcode_address = Cdm16Processor.Instructions.BR_REL_NOP;
                    br_rel_nop = true;
                }
                break;

            case 0b111:
                if (checkFlags(br_rel_flags_d, parameters.psFlags())) {
                    microcode_address = Cdm16Processor.Instructions.BR_REL_P;
                } else {
                    microcode_address = Cdm16Processor.Instructions.BR_REL_NOP;
                    br_rel_nop = true;
                }
                break;
        }

        arith_carry = switch_alu_func0;

        if (switch_alu_func0 || switch_alu_func1) {
            if (switch_alu_func1) {
                alu_func = alu_op_d0;
            } else {
                alu_func = alu_op_d1;
            }
        } else {
            if ((microcode_address & 0b1110000) == Cdm16Processor.InstructionGroups.IMM_6 && op_type_d3 >= 0b1110) {
                alu_func = Cdm16Processor.ALU_3op.SUB;
            } else {
                alu_func = Cdm16Processor.ALU_3op.ADC;
            }
        }

        if (imm_type == Cdm16Processor.IMM_Type.IMM_6) {
            imm_d = imm6_d;
        } else {
            imm_d = imm9_d;
        }

        if (microcode_address == Cdm16Processor.InstructionGroups.IMM_9
                || microcode_address == Cdm16Processor.InstructionGroups.IMM_9 + 1) {
            intInstruction = true;
        }

        if (microcode_address == 0b1000) {
            jsrInstruction = true;
        }

        if (microcode_address == 0b1001) {
            rtiInstruction = true;
        }

        switch (microcode_address) {
            case 0x4:
                haltInstruction = true;
                break;
            case 0x5:
                waitInstruction = true;
                break;
            case 0x6:
                eiInstruction = true;
                break;
            case 0x7:
                diInstruction = true;
                break;
        }

        return new InstructionDecoderOutputParameters(
                microcode_address,
                shift_count_d,
                rs0,
                rs1,
                rd,
                alu_op_type,
                br_rel_nop,
                arith_carry,
                alu_func,
                imm_type,
                imm_d,
                intInstruction,
                jsrInstruction,
                rtiInstruction,
                haltInstruction,
                waitInstruction,
                eiInstruction,
                diInstruction
        );
    }

    public static InstructionDecoderOutputParameters getFetchSignals() {
        return new InstructionDecoderOutputParameters(
                Cdm16Processor.Instructions.FETCH,
                0,
                0,
                0,
                0,
                Cdm16Processor.ALU_InstructionGroups.ALU_3,
                false,
                false,
                Cdm16Processor.ALU_3op.ADC,
                Cdm16Processor.IMM_Type.IMM_6,
                0,
                false,
                false,
                false,
                false,
                false,
                false,
                false
        );
    }
}
