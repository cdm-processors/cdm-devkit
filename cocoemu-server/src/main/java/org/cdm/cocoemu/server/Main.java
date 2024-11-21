package org.cdm.cocoemu.server;

public class Main {
    public static void main(String[] args) {
        if (args.length != 1) {
            throw new IllegalArgumentException("Expected exactly one argument");
        }
        int port = Integer.parseInt(args[0]);

    }
}