package org.cdm.cocoemu.server.adapters.processors;

import org.cdm.cocoemu.components.processors.cdm16.Cdm16;
import org.cdm.cocoemu.components.processors.cdm16.Status;
import org.cdm.cocoemu.server.adapters.ProcessorAdapter;
import org.cdm.debug.runtime.ProcessorInfo;
import org.cdm.debug.runtime.ProcessorState;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class Cdm16ProcessorAdapter implements ProcessorAdapter {
    private static final ProcessorInfo CDM16_PROCESSOR_INFO = new ProcessorInfo() {
        @Override
        public String getDisplayName() {
            return "CdM-16";
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
    };

    public Cdm16 processor;

    public Cdm16ProcessorAdapter(Cdm16 processor) {
        this.processor = processor;
    }

    @Override
    public ProcessorInfo getProcessorInfo() {
        return CDM16_PROCESSOR_INFO;
    }

    @Override
    public ProcessorState getProcessorState() {
        return new ProcessorState() {
            @Override
            public boolean isFetching() {
                return processor.outputs.fetch;
            }

            @Override
            public boolean isHalted() {
                return processor.outputs.status == Status.HALTED;
            }

            @Override
            public int getProgramCounter() {
                return processor.outputs.pc;
            }

            @Override
            public List<Integer> getRegisters() {
                List<Integer> registers = new ArrayList<>();
                for (int registerValue : processor.outputs.gpRegisters) {
                    registers.add(registerValue);
                }
                registers.add(processor.outputs.pc);
                registers.add(processor.outputs.sp);
                registers.add(processor.outputs.ps);

                return registers;
            }

            @Override
            public boolean exceptionHappened() {
                return processor.exceptionHappened();
            }

            @Override
            public int getExceptionNumber() {
                return processor.exceptionNumber();
            }
        };
    }
}
