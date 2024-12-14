package org.cdm.cocoemu.server.adapter;

import org.cdm.cocoemu.components.memory.Memory;
import org.cdm.cocoemu.systems.HarvardSystem;
import org.cdm.debug.runtime.ProcessorState;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class Cdm16HarvardSystemAdapter extends ProcessorAdapter<HarvardSystem> {
    public Cdm16HarvardSystemAdapter(HarvardSystem system) {
        super(system);
    }

    @Override
    public ProcessorState getProcessorState() {
        return new ProcessorState() {
            @Override
            public boolean isFetching() {
                return system.cdm16.outputs.fetch;
            }

            @Override
            public boolean isHalted() {
                return system.cdm16.outputs.status == 2;
            }

            @Override
            public int getProgramCounter() {
                return system.cdm16.outputs.pc;
            }

            @Override
            public List<Integer> getRegisters() {
                List<Integer> registers = new ArrayList<>();
                for (int registerValue : system.cdm16.outputs.gpRegisters) {
                    registers.add(registerValue);
                }
                registers.add(system.cdm16.outputs.pc);
                registers.add(system.cdm16.outputs.sp);
                registers.add(system.cdm16.outputs.ps);

                return registers;
            }

            @Override
            public boolean exceptionHappened() {
                return system.cdm16.exceptionHappened();
            }

            @Override
            public int getExceptionNumber() {
                return system.cdm16.exceptionNumber();
            }
        };
    }

    @Override
    public Memory getBankedRam() {
        return system.ram;
    }

    @Override
    public Memory getBankedRom() {
        return system.rom;
    }

    @Override
    public String getDisplayName() {
        return "CdM-16 Harvard System";
    }

    @Override
    public int getMemorySize() {
        return 65536;
    }

    @Override
    public List<String> getRegisterNames() {
        return Arrays.asList("r0", "r1", "r2", "r3", "r4", "r5", "r6", "fp", "pc", "sp", "ps");
    }

    @Override
    public List<Integer> getRegisterSizes() {
        return Arrays.asList(16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16);
    }

    @Override
    public boolean supportsExceptions() {
        return true;
    }
}
