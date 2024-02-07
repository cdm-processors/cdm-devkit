package org.cdm.logisim.debugger;

import com.cburch.logisim.circuit.Circuit;
import com.cburch.logisim.circuit.SimulatorEvent;
import com.cburch.logisim.circuit.SimulatorListener;
import com.cburch.logisim.data.Attribute;
import com.cburch.logisim.data.Attributes;
import com.cburch.logisim.data.Bounds;
import com.cburch.logisim.instance.*;
import com.cburch.logisim.util.GraphicsUtil;
import com.cburch.logisim.util.LocaleManager;
import com.cburch.logisim.util.StringGetter;
import com.cburch.logisim.util.StringUtil;
import lombok.Getter;
import lombok.Setter;
import org.cdm.logisim.debugger.adapters.DefaultAdapter;
import org.cdm.logisim.debugger.adapters.ProcessorAdapter;
import org.cdm.logisim.debugger.server.Server;
import org.cdm.logisim.debugger.server.ServerStatus;
import org.cdm.logisim.debugger.ui.Button;
import org.cdm.logisim.debugger.simulation.SimulationTicker;

import java.awt.*;
import java.awt.event.MouseEvent;

public class DebuggerComponent extends InstanceFactory {
    private static final LocaleManager source = new LocaleManager("resources/logisim", "std");

    private static final Attribute<Integer> PORT_ATTR =
            Attributes.forIntegerRange("Port", 0, 65535);
    private static final int DEFAULT_PORT = 7001;

    private static final Attribute<Integer> RESET_TIMEOUT_ATTR =
            Attributes.forIntegerRange("Reset timeout (ms)", 0, 5000);
    private static final int DEFAULT_RESET_TIMEOUT = 250;
    /*private static final Attribute<ProcessorType> PROC_ATTR = Attributes.forOption("Processor", getter("Processor"), new ProcessorType[]{
            ProcessorType.CDM8, ProcessorType.CDM8E, ProcessorType.CDM16_CIRCUIT, ProcessorType.CDM16_EMU
    });*/

    private static final Button startButton = new Button(Bounds.create(10, 50, 40, 20), "Start");
    private static final Button stopButton = new Button(Bounds.create(70, 50, 40, 20), "Stop");
    private static Bounds componentBounds;

    @Getter
    private static final SimulationTicker simulationTicker = new SimulationTicker();
    @Getter
    @Setter
    private static ProcessorAdapter processorAdapter = new DefaultAdapter();
    private static Server server = null;

    @Getter
    private static Circuit debuggerCircuit = null;

    @Setter
    private static String serverStatus = ServerStatus.DOWN;

    private boolean simulatorListenerRegistered = false;

    @Getter
    private static int resetTimeout = DEFAULT_RESET_TIMEOUT;

    public DebuggerComponent() {
        super("Debugger");

        setOffsetBounds(Bounds.create(0, 0, 120, 80));

        Port[] ps = new Port[]{
                new Port(120, 110, "input", 16), //in
        };

        //ps[Ports.DATA_IN].setToolTip(getter("in"));

        this.setPorts(ps);
        this.setInstancePoker(Poker.class);
        this.setAttributes(
                new Attribute[]{
                        PORT_ATTR, RESET_TIMEOUT_ATTR/*, PROC_ATTR*/
                },
                new Object[]{
                        DEFAULT_PORT, DEFAULT_RESET_TIMEOUT/*, ProcessorType.CDM16_CIRCUIT*/
                }
        );
    }

    @Override
    protected void configureNewInstance(Instance instance) {
        instance.addAttributeListener();
    }

    @Override
    protected void instanceAttributeChanged(Instance instance, Attribute<?> attr) {
        if (attr == RESET_TIMEOUT_ATTR) {
            resetTimeout = (int) instance.getAttributeValue(attr);
        }
    }

    @Override
    public void paintInstance(InstancePainter painter) {
        Graphics g = painter.getGraphics();
        Bounds bds = painter.getBounds();
        painter.drawBounds();
        painter.drawLabel();

        // DATA_IN, DATA_OUT, ADDRESS, MEM, DATA, READ, WORD, IRQ, INT_NUMBER, EXC, CLK , EXC_NUMBER , HOLD_WAIT , STATUS;
        //painter.drawPort(Ports.DATA_IN, get("in"), Direction.WEST);

        componentBounds = bds;

        startButton.draw(bds, painter);
        stopButton.draw(bds, painter);

        // String statusString = String.format("Status: %.10s", serverStatus);
        String statusString = String.format("%.18s", serverStatus);

        GraphicsUtil.drawText(g, "CdM Debugger", bds.getX() + 60, bds.getY() + 5, 0, -1);
        GraphicsUtil.drawText(g, statusString, bds.getX() + 60, bds.getY() + 25, 0, -1);

        // System.err.println("Draw from paint");
    }

    @Override
    public void propagate(InstanceState state) {

        if (!simulatorListenerRegistered) {
            state.getProject().getSimulator().addSimulatorListener(new SimulatorListener() {
                @Override
                public void propagationCompleted(SimulatorEvent simulatorEvent) {
                }
                @Override
                public void simulatorStateChanged(SimulatorEvent simulatorEvent) {

                }

                @Override
                public void tickCompleted(SimulatorEvent simulatorEvent) {
                    if (server != null) {
                        getSimulationTicker().onTickComplete(simulatorEvent);
                    }
                }
            });

            simulatorListenerRegistered = true;
        }
        // if (server != null) return;

        // initialize(state);
    }

//    private void initialize(InstanceState state) {
//        // server = new Server();
//    }
//
//    public static StringGetter getter(String key) {
//        return source.getter(key);
//    }
//
//    public static String get(String key) {
//        return source.get(key);
//    }
//
//    public static String get(String key, String arg0) {
//        return StringUtil.format(source.get(key), arg0);
//    }
//
//    public static String get(String key, String arg0, String arg1) {
//        return StringUtil.format(source.get(key), arg0, arg1);
//    }

    public static class Poker extends InstancePoker {
        @Override
        public void paint(InstancePainter painter) {
            Graphics g = painter.getGraphics();
            // Bounds bds = painter.getBounds();
            painter.drawBounds();
            painter.drawLabel();

            startButton.drawOnPress(componentBounds, g);
            stopButton.drawOnPress(componentBounds, g);
        }

        @Override
        public void mousePressed(InstanceState state, MouseEvent e) {

            if (startButton.checkPressed(componentBounds, e)) {
                if (server == null) {
                    try {
                        debuggerCircuit = state.getProject().getCurrentCircuit();
                        simulationTicker.setProject(state.getProject());
                        resetTimeout = state.getAttributeValue(RESET_TIMEOUT_ATTR);

                        int port = state.getAttributeValue(PORT_ATTR);
                        server = new Server(port);
                        new Thread(server).start();

                        serverStatus = ServerStatus.WAITING;
                    } catch (Exception ex) {
                        serverStatus = ex.getMessage();
                    }
                }
            }

            if (stopButton.checkPressed(componentBounds, e)) {
                if (server != null) {
                    try {
                        server.stop(10, "Now stop");
                        server = null;

                        simulationTicker.setProject(null);
                        debuggerCircuit = null;

                        serverStatus = ServerStatus.DOWN;
                    } catch (InterruptedException ex) {
                        serverStatus = ex.getMessage();
                        throw new RuntimeException(ex);
                    }
                }
            }
        }

        @Override
        public void mouseReleased(InstanceState state, MouseEvent e) {
            // System.err.printf("Released %d %d\n", e.getX(), e.getY());
        }
    }
}