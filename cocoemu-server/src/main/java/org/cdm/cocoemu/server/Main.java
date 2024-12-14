package org.cdm.cocoemu.server;

import com.beust.jcommander.JCommander;
import org.cdm.cocoemu.server.debug.ServerMessageHandler;
import org.cdm.debug.server.Server;

public class Main {
    public static void main(String[] args) {
        if (args.length != 1) {
            throw new IllegalArgumentException("Expected exactly one argument");
        }
        Args args1 = new Args();
        JCommander.newBuilder().addObject(args1).build().parse(args);
        int port = args1.getPort();

        Server server = new Server(port, ServerMessageHandler::new);
    }
}