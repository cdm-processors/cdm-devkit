package org.cdm.cocoemu.server;

import com.beust.jcommander.JCommander;
import org.cdm.cocoemu.server.debug.ServerMessageHandler;
import org.cdm.debug.server.Server;

public class Main {
    public static void main(String[] argv) {
        Args args = new Args();
        JCommander p = JCommander.newBuilder().addObject(args).build();
        p.parse(argv);

        Server server = new Server(args.getPort(), ServerMessageHandler::new);
        new Thread(server).start();
    }
}
