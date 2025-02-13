package org.cdm.debug.server;

import com.google.gson.Gson;
import com.google.gson.JsonObject;
import org.cdm.debug.MessageHandler;
import org.cdm.debug.dto.RawMessage;
import org.java_websocket.WebSocket;
import org.java_websocket.handshake.ClientHandshake;
import org.java_websocket.server.WebSocketServer;

import java.net.BindException;
import java.net.InetSocketAddress;
import java.util.concurrent.ArrayBlockingQueue;
import java.util.concurrent.BlockingQueue;
import java.util.function.Supplier;

public class Server extends WebSocketServer {

    private static final int DEFAULT_PORT = 7001;
    private static final int QUEUE_INITIAL_CAPACITY = 100;

    private final BlockingQueue<RawMessage> messageQueue = new ArrayBlockingQueue<>(QUEUE_INITIAL_CAPACITY);
    private final Supplier<MessageHandler> messageHandlerFactory;

    private MessageHandler messageHandler;

    private WebSocket currentConnection;

    public Server(Supplier<MessageHandler> messageHandlerFactory) {
        this(DEFAULT_PORT, messageHandlerFactory);
    }

    public Server(int port, Supplier<MessageHandler> messageHandlerFactory) {
        super(new InetSocketAddress(port));

        this.messageHandlerFactory = messageHandlerFactory;

        // Fix BindError
        setReuseAddr(true);
    }

    public BlockingQueue<RawMessage> getMessageQueue() {
        return messageQueue;
    }

    @Override
    public void stop() throws InterruptedException {
        if (messageHandler != null) {
            messageHandler.requestStop();
        }

        super.stop();
    }

    @Override
    public void onOpen(WebSocket conn, ClientHandshake handshake) {
        if (this.getConnections().size() > 1) {
            conn.close();
            System.err.println("Already connected");
            return;
        }

        currentConnection = conn;
        //DebuggerComponent.setServerStatus(ServerStatus.CONNECTED);
        System.out.println("Debug client connected");
    }

    @Override
    public void onClose(WebSocket conn, int code, String reason, boolean remote) {
        currentConnection = null;
        //DebuggerComponent.setServerStatus(ServerStatus.WAITING);
        System.out.println("Debug client disconnected");
    }

    @Override
    public void onMessage(WebSocket conn, String message) {
        System.out.println("Got message " + message);

        Gson gson = new Gson();

        JsonObject parsedMessage = gson.fromJson(message, JsonObject.class);

        RawMessage rawMessage = new RawMessage();

        rawMessage.action = gson.fromJson(
                parsedMessage.get(RawMessage.ACTION_FIELD),
                String.class
        );
        rawMessage.data = parsedMessage;

        messageQueue.add(rawMessage);
    }

    @Override
    public void onError(WebSocket conn, Exception ex) {
        if (ex instanceof BindException) {
            //DebuggerComponent.setServerStatus("Bind error");
        } else {
            //DebuggerComponent.setServerStatus(ex.getMessage());
        }

        System.err.println("Debug server error: " + ex);
    }

    @Override
    public void onStart() {
        System.out.println("Started debug server on " + this.getAddress());

        messageHandler = messageHandlerFactory.get();
        messageHandler.setMessageQueue(messageQueue);
        messageHandler.setSendMessageCallback(this::sendMessage);
        messageHandler.start();
    }

    public void sendMessage(String message) {
        if (currentConnection != null && currentConnection.isOpen()) {
            currentConnection.send(message);
        }
    }
}
