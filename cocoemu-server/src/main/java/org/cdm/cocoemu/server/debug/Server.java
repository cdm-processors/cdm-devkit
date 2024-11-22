package org.cdm.cocoemu.server.debug;

import com.google.gson.Gson;
import com.google.gson.JsonObject;
import org.cdm.debug.dto.DebuggerMessage;
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
    public void onOpen(WebSocket webSocket, ClientHandshake clientHandshake) {
        if (this.getConnections().size() > 1) {
            webSocket.close();
            System.err.println("Already connected");
            return;
        }

        currentConnection = webSocket;
        System.out.println("Debug client connected");
    }

    @Override
    public void onClose(WebSocket webSocket, int i, String s, boolean b) {
        currentConnection = null;
        System.out.println("Debug client disconnected");
    }

    @Override
    public void onMessage(WebSocket webSocket, String message) {
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
    public void onError(WebSocket webSocket, Exception e) {
        if (e instanceof BindException) {
            DebuggerComponent.setServerStatus("Bind error");
        } else {
            DebuggerComponent.setServerStatus(e.getMessage());
        }

        System.err.println("Debug server error: " + e);
    }

    @Override
    public void onStart() {
        System.out.println("Started debug server on " + this.getAddress());

    }

    public void sendMessage(String message) {
        if (currentConnection != null && currentConnection.isOpen()) {
            currentConnection.send(message);
        }
    }
}
