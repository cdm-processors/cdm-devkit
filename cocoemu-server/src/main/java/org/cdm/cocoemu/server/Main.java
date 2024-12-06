package org.cdm.cocoemu.server;

import org.cdm.cocoemu.components.processors.cdm16.Cdm16;
import org.cdm.cocoemu.server.emulator.CdM16Emulator;
import org.cdm.cocoemu.server.emulator.CdMEmulator;
import org.cdm.cocoemu.server.debug.ServerMessageHandler;
import org.cdm.debug.server.Server;

import java.util.function.Supplier;

public class Main {
    public static void main(String[] args) {
        if (args.length != 1) {
            throw new IllegalArgumentException("Expected exactly one argument");
        }
        int port = Integer.parseInt(args[0]);
        CdMEmulator<Cdm16> e = new CdM16Emulator();
        Server server = new Server(port, () -> new ServerMessageHandler(e));
    }
}