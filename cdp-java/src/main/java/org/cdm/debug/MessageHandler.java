package org.cdm.debug;

import com.google.gson.Gson;
import org.cdm.debug.dto.*;

import java.util.concurrent.BlockingQueue;
import java.util.concurrent.TimeUnit;
import java.util.function.Consumer;

public abstract class MessageHandler extends Thread {
    private BlockingQueue<RawMessage> messageQueue;
    private Consumer<String> sendMessageCallback;

    private boolean stopped = false;

    public void setMessageQueue(BlockingQueue<RawMessage> messageQueue) {
        this.messageQueue = messageQueue;
    }

    public void setSendMessageCallback(Consumer<String> sendMessageCallback) {
        this.sendMessageCallback = sendMessageCallback;
    }

    protected void sendMessage(String message) {
        if (sendMessageCallback != null) {
            sendMessageCallback.accept(message);
        }
    }

    protected void sendResponse(DebuggerResponse response) {
        sendMessage(
                new Gson().toJson(response)
        );
    }

    protected void sendDebugEvent(String eventType) {
        sendMessage(
                new Gson().toJson(
                        new DebugEvent(eventType)
                )
        );
    }

    @Override
    public void run() {
        while (!stopped) {
            handleMessage(true);
        }
    }

    public void requestStop() {
        stopped = true;
        this.interrupt();
    }

    public void handleMessage(boolean block) {
        if (!block && messageQueue.isEmpty()) {
            return;
        }

        RawMessage message;

        try {
            message = messageQueue.poll(100, TimeUnit.MILLISECONDS);
        } catch (InterruptedException e) {
            stopped = true;
            return;
        }

        if (message == null) {
            return;
        }

        System.out.printf("%s %s\n", message.action, message.data);

        DebuggerResponse response;

        switch (message.action) {
            case MessageActions.PING:
                response = new PingResponse("Pong");
                break;
            case MessageActions.SET_BREAKPOINTS:
                response = handleBreakpointsMessage(
                        new Gson().fromJson(message.data, BreakpointsMessage.class)
                );
                break;
            case MessageActions.SET_LINE_LOCATIONS:
                response = handleLineLocationsMessage(
                        new Gson().fromJson(message.data, LineLocationsMessage.class)
                );
                break;
            case MessageActions.STEP:
                response = handleStepMessage();
                break;
            case MessageActions.RUN:
                response = handleRunMessage(
                        new Gson().fromJson(message.data, RunMessage.class)
                );
                break;
            case MessageActions.PAUSE:
                response = handlePauseMessage();
                break;
            case MessageActions.RESET:
                response = handleResetMessage();
                break;
            case MessageActions.LOAD:
                String source = new Gson().fromJson(
                        message.data.get(LoadMessage.SOURCE_FIELD),
                        String.class
                );

                switch (source) {
                    case PathLoadMessage.SOURCE:
                        response = handlePathLoadMessage(
                                new Gson().fromJson(message.data, PathLoadMessage.class)
                        );
                        break;
                    case BytesLoadMessage.SOURCE:
                        response = handleBytesLoadMessage(
                                new Gson().fromJson(message.data, BytesLoadMessage.class)
                        );
                        break;
                    default:
                        response = new FailResponse("Unknown source: " + source);
                }
                break;
            case MessageActions.INIT:
                response = handleInitMessage(
                        new Gson().fromJson(message.data, InitializationMessage.class)
                );
                break;
            case MessageActions.GET_REGISTERS:
                response = handleGetRegistersMessage();
                break;
            case MessageActions.GET_MEMORY:
                response = handleGetMemoryMessage(
                        new Gson().fromJson(message.data, GetMemoryMessage.class)
                );
                break;
            case MessageActions.SET_MEMORY:
                response = handleSetMemoryMessage(
                        new Gson().fromJson(message.data, SetMemoryMessage.class)
                );
                break;
            case MessageActions.GET_TUNNEL:
                response = handleGetTunnelMessage(
                        new Gson().fromJson(message.data, GetTunnelMessage.class)
                );
                break;
            default:
                response = new FailResponse("Unknown action: " + message.action);
        }

        sendResponse(response);
    }

    protected abstract DebuggerResponse handleBreakpointsMessage(BreakpointsMessage message);

    protected abstract DebuggerResponse handleLineLocationsMessage(LineLocationsMessage message);

    protected abstract DebuggerResponse handleStepMessage();

    protected abstract DebuggerResponse handleRunMessage(RunMessage message);

    protected abstract DebuggerResponse handlePauseMessage();

    protected abstract DebuggerResponse handleResetMessage();

    protected abstract DebuggerResponse handleInitMessage(InitializationMessage message);

    protected abstract DebuggerResponse handleGetRegistersMessage();

    protected abstract DebuggerResponse handleGetMemoryMessage(GetMemoryMessage message);

    protected abstract DebuggerResponse handlePathLoadMessage(PathLoadMessage message);

    protected abstract DebuggerResponse handleBytesLoadMessage(BytesLoadMessage message);

    protected abstract DebuggerResponse handleSetMemoryMessage(SetMemoryMessage message);

    protected abstract DebuggerResponse handleGetTunnelMessage(GetTunnelMessage message);
}
