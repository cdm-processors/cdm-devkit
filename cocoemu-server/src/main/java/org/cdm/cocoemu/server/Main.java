package org.cdm.cocoemu.server;

import org.cdm.cocoemu.server.app.Emulator;
import org.cdm.cocoemu.server.debug.ServerMessageHandler;
import org.cdm.debug.MessageHandler;
import org.cdm.debug.server.Server;

import java.util.function.Supplier;

public class Main {
    public static void main(String[] args) {
        if (args.length != 1) {
            throw new IllegalArgumentException("Expected exactly one argument");
        }
        int port = Integer.parseInt(args[0]);
        Emulator e = new Emulator();
        Supplier<MessageHandler> s = () -> new ServerMessageHandler(e);
        Server server = new Server(port, s);
    }
}