package org.cdm.logisim.emulator.cdm16;

import com.cburch.logisim.data.BitWidth;
import com.cburch.logisim.data.Value;
import com.cburch.logisim.instance.InstanceState;
import org.cdm.logisim.emulator.ExceptionHandler;
import org.cdm.logisim.emulator.InterruptHandler;
import org.cdm.logisim.emulator.GenericProcessor;

public class Processor implements GenericProcessor, ExceptionHandler, InterruptHandler {

    public static int MAX_INT = 0xFFFF;

    public Processor() {

    }

    public void externalInterrupt(InstanceState state, int interruptNumber) {
        System.out.println("externalInterrupt" + interruptNumber);
    }

    public void externalException(InstanceState state, int exceptionNumber) {
        System.out.println("externalException " + exceptionNumber);
    }

    public void clockRising(InstanceState state) {
        System.out.println("clockRising");
    }

    public void clockFalling(InstanceState state) {
        System.out.println("clockFalling");
    }

    public void update(InstanceState state) {
        System.out.println("update");
    }

}
