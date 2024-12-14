package org.cdm.cocoemu.server;

import org.cdm.cocoemu.server.adapter.Factory;
import org.cdm.cocoemu.server.adapter.ProcessorType;
import org.cdm.cocoemu.server.debug.ServerMessageHandler;
import org.cdm.debug.server.Server;

public class Main {
    public static void main(String[] args) {
        if (args.length != 1) {
            throw new IllegalArgumentException("Expected exactly one argument");
        }
        int port = Integer.parseInt(args[0]);

        Server server = new Server(port, () -> new ServerMessageHandler(Factory.getDebugEnvironment(ProcessorType.CDM16HARVARD)));
    }
}