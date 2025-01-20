package org.cdm.cocoemu.server;

import com.beust.jcommander.JCommander;
import com.beust.jcommander.ParameterException;
import org.cdm.cocoemu.server.debug.ServerMessageHandler;
import org.cdm.debug.server.Server;

public class Main {
    public static void main(String[] rawArguments) {
        Args parsedArguments = new Args();

        JCommander argumentsParser = JCommander.newBuilder()
                .addObject(parsedArguments)
                .build();

        try {
            argumentsParser.parse(rawArguments);
        } catch (ParameterException e) {
            System.out.println(e.getMessage());
            e.usage();
            return;
        }

        if (parsedArguments.help) {
            argumentsParser.usage();
            return;
        }

        Server server = new Server(parsedArguments.getPort(), ServerMessageHandler::new);
        new Thread(server).start();
    }
}
