import { EventEmitter } from "events";

import { WebSocket } from "ws";

import { Arch, StopCondition, InitializationResponse, Reason, GetRegistersResponse, GetMemoryResponse, DebugEvent, reasons } from "../protocol/general";
import { TargetID } from "../protocol/targets";

export class CdmRuntime extends EventEmitter {
    private readonly ws: WebSocket;
    private bufferUntilOpened: any[];

    constructor(
        address: string
    ) {
        super();

        this.ws = new WebSocket(address);
        this.ws.on("message", (data) => {
            let message = JSON.parse(data.toString());
            switch (message?.status) {
                case "OK": break;
                case "FAIL": {
                    console.log(`Something went terribly wrong: ${data.toString()}`);
                    return;
                }
                default: {
                    console.log(`Received an invalid message: ${message}`);
                    return;
                }
            }

            switch (message?.action) {
                case "init": {
                    let casted: InitializationResponse = message;
                    let { supportsExceptions, registers, ramSize } = casted;
                    this.emit("initialized", supportsExceptions, registers, ramSize);
                    console.log(`Debug server initialized, capabilities are: ${supportsExceptions ? "supports" : "does not support"} exceptions; ${registers.join(", ")} registers; RAM size - ${ramSize} bytes`);
                    break;
                }
                case "load": {
                    this.emit("loaded");
                    console.log("Debug server loaded provided sources");
                    break;
                }
                case "setBreakpoints": {
                    this.emit("setBreakpoints");
                    console.log("Debug server got breakpoints");
                    break;
                }
                case "setLineLocations": {
                    this.emit("setLines");
                    console.log("Debug server got line locations");
                    break;
                }
                case "run": {
                    this.emit("run");
                    console.log("Debug server executes debuggee");
                    break;
                }
                case "getRegisters": {
                    let casted: GetRegistersResponse = message;
                    this.emit("receivedRegisters", casted.registers);
                    console.log(`Debug server sent new register values: ${casted.registers.join(", ")}`);
                    break;
                }
                case "getMemory": {
                    let casted: GetMemoryResponse = message;
                    this.emit("receivedMemory", casted.bytes);
                    console.log("Debug server sent memory page");
                    break;
                }
                case "debugEvent": {
                    let casted: DebugEvent = message;
                    this.emit("stopped", casted.reason);
                    console.log(`Debug server stopped execution of debuggee because of ${casted.reason}`);
                    break;
                }
                default: {
                    return;
                }
            }
        });

        this.bufferUntilOpened = [];
        this.ws.once("open", () => {
            this.bufferUntilOpened.forEach((message) => {
                this.send(message);
            });
        });
    }

    on(eventName: "initialized", listener: (supportsExceptions: boolean, registers: string[], ramSize: number) => void): this;
    on(eventName: "loaded", listener: () => void): this;
    on(eventName: "setBreakpoints", listener: () => void): this;
    on(eventName: "setLines", listener: () => void): this;
    on(eventName: "run", listener: () => void): this;
    on(eventName: "receivedRegisters", listener: (registers: number[]) => void): this;
    on(eventName: "receivedMemory", listener: (bytes: number[]) => void): this;
    on(eventName: "stopped", listener: (reason: Reason) => void): this;
    on(eventName: string | symbol, listener: (...args: any[]) => void): this {
        return super.on(eventName, listener);
    }

    once(eventName: "initialized", listener: (supportsExceptions: boolean, registers: string[], ramSize: number) => void): this;
    once(eventName: "loaded", listener: () => void): this;
    once(eventName: "setBreakpoints", listener: () => void): this;
    once(eventName: "setLines", listener: () => void): this;
    once(eventName: "run", listener: () => void): this;
    once(eventName: "receivedRegisters", listener: (registers: number[]) => void): this;
    once(eventName: "receivedMemory", listener: (bytes: number[]) => void): this;
    once(eventName: "stopped", listener: (reason: Reason) => void): this;
    once(eventName: string | symbol, listener: (...args: any[]) => void): this {
        return super.once(eventName, listener);
    }    

    private send(obj: any) {
        if (this.ws.readyState !== this.ws.OPEN) {
            this.bufferUntilOpened.push(obj);
            return;
        }

        this.ws.send(JSON.stringify(obj));
    }

    initialize(target: TargetID, arch: Arch) {
        console.log(`Initializing debug server with ${target} target and ${arch} architecture`);
        this.send({
            action: "init",
            target: target,
            arch: arch,
        });
    }

    loadFromPath(path: string) {
        console.log(`Passing path (${path}) to image to debug server;`);
        this.send({
            action: "load",
            source: "path",
            path: path,
        });
    }

    loadFromBytes(bytes: number[]) {
        this.send({
            action: "load",
            source: "bytes",
            bytes: bytes,
        });
    }

    reset() {
        console.log("Resetting execution of debuggee");
        this.send({
            action: "reset",
        });
    }

    setBreakpoints(locations: number[]) {
        console.log(`Passing breakpoints (${locations}) to debug server`);
        this.send({
            action: "setBreakpoints",
            breakpoints: locations,
        });
    }

    setLines(locations: number[]) {
        console.log(`Passing line locations (${locations}) to debug server`);
        this.send({
            action: "setLineLocations",
            locations: locations,
        });
    }

    run(...conditions: Reason[]) {
        console.log(`Starting execution of debuggee, stop conditions: ${conditions.join(", ")}`);
        this.send({
            action: "run",
            stopConditions: conditions,
        });
    }

    pause() {
        console.log("Pausing execution of debuggee");
        this.send({
            action: "pause",
        });
    }

    requestRegisters() {
        console.log("Requesting register values");
        this.send({
            action: "getRegisters",
        });
    }

    requestMemory() {
        this.send({
            action: "getMemory",
        });
    }

    shutdown() {
        this.ws.close();
    }
}
