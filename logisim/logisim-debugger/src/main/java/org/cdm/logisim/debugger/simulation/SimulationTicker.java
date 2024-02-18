package org.cdm.logisim.debugger.simulation;

import com.cburch.logisim.circuit.SimulatorEvent;
import com.cburch.logisim.proj.Project;
import lombok.Getter;
import lombok.Setter;
import org.cdm.logisim.debugger.DebuggerComponent;
import org.cdm.logisim.debugger.adapters.ProcessorAdapter;
import org.cdm.logisim.debugger.adapters.ProcessorState;

import javax.swing.*;
import java.util.function.Predicate;

public class SimulationTicker {
    @Getter
    @Setter
    private Project project;

    private boolean tickCompleted = false;
    private int bootstrapTicks;
    private Predicate<ProcessorState> tickPredicate = (state) -> true;
    private final Object tickLock = new Object();
    private ProcessorState tickResult;

    public ProcessorState tickUntil(Predicate<ProcessorState> predicate) throws InterruptedException {
        tickCompleted = false;
        bootstrapTicks = 2;
        tickPredicate = predicate;
        SwingUtilities.invokeLater(() -> {
            // will be called in UI thread
            project.getSimulator().tick();
        });

        System.out.println("request first tick");
        synchronized (tickLock) {
            while (!tickCompleted) {
                tickLock.wait();
            }
        }
        System.out.println("Pass lock");
        return tickResult;
    }

    public void onTickComplete(SimulatorEvent event) {
        bootstrapTicks--;

        ProcessorAdapter processorAdapter = DebuggerComponent.getProcessorAdapter();
        ProcessorState processorState = processorAdapter.getState(event.getSource().getCircuitState());

        if (bootstrapTicks < 0 && processorState != null && tickPredicate.test(processorState)) {
            tickCompleted = true;
            tickResult = processorState;
            synchronized (tickLock) {
                tickLock.notifyAll();
            }
        } else {
            event.getSource().tick();
        }
    }
}
