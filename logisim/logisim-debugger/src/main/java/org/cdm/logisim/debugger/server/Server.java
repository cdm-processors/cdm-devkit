package org.cdm.logisim.debugger.server;

import com.google.gson.Gson;
import com.google.gson.JsonObject;
import org.cdm.logisim.debugger.DebuggerComponent;
import org.cdm.logisim.debugger.dto.DebuggerMessage;
import org.cdm.logisim.debugger.simulation.TickControlThread;
import org.java_websocket.WebSocket;
import org.java_websocket.handshake.ClientHandshake;
import org.java_websocket.server.WebSocketServer;

import java.net.BindException;
import java.net.InetSocketAddress;
import java.util.concurrent.ArrayBlockingQueue;
import java.util.concurrent.BlockingQueue;

public class Server extends WebSocketServer {

    private static final int QUEUE_INITIAL_CAPACITY = 100;
    private final BlockingQueue<DebuggerMessage> messageQueue = new ArrayBlockingQueue<>(QUEUE_INITIAL_CAPACITY);
    private WebSocket currentConnection;

    public Server(int port) {
        super(new InetSocketAddress(port));
    }

    @Override
    public void onOpen(WebSocket conn, ClientHandshake handshake) {
        if (this.getConnections().size() > 1) {
            conn.close();
            System.err.println("Already connected");
            return;
        }

        currentConnection = conn;
        DebuggerComponent.setServerStatus(ServerStatus.CONNECTED);
        System.out.println("Debug client connected");
    }

    @Override
    public void onClose(WebSocket conn, int code, String reason, boolean remote) {
        currentConnection = null;
        DebuggerComponent.setServerStatus(ServerStatus.WAITING);
        System.out.println("Debug client disconnected");
    }

    @Override
    public void onMessage(WebSocket conn, String message) {
        System.out.println("Got message " + message);

        Gson gson = new Gson();

        JsonObject parsedMessage = gson.fromJson(message, JsonObject.class);

        DebuggerMessage packedMessage = new DebuggerMessage();

        packedMessage.action = gson.fromJson(
                parsedMessage.get(DebuggerMessage.ACTION_FIELD),
                String.class
        );
        packedMessage.data = parsedMessage;


        messageQueue.add(packedMessage);
    }

    @Override
    public void onError(WebSocket conn, Exception ex) {
        if (ex instanceof BindException) {
            DebuggerComponent.setServerStatus("Bind error");
        } else {
            DebuggerComponent.setServerStatus(ex.getMessage());
        }

        System.err.println("Debug server error: " + ex);
    }

    @Override
    public void onStart() {
        System.out.println("Started debug server on " + this.getAddress());

        TickControlThread tickControlThread = new TickControlThread(messageQueue, this::sendMessage);
        tickControlThread.start();
    }

    public void sendMessage(String message) {
        if (currentConnection != null && currentConnection.isOpen()) {
            currentConnection.send(message);
        }
    }
}
