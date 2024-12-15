package org.cdm.cocoemu.server;

import com.beust.jcommander.JCommander;
import com.beust.jcommander.Parameter;
import org.cdm.cocoemu.server.debug.ServerMessageHandler;
import org.cdm.debug.server.Server;

public class Main {
    @Parameter(names = {"--port", "-p"})
    private int port = 7001;

    public static void main(String ... args) {
        Main main = new Main();
//        JCommander.newBuilder().addObject(main).build().parse(args);

        Server server = new Server(main.port, ServerMessageHandler::new);

    }
}