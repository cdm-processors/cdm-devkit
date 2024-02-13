import { EventEmitter } from "events";

import { WebSocket } from "ws";

import { ArchitectureID } from "../protocol/architectures";
import { TargetID } from "../protocol/targets";
import { BreakCondition, ExecutionStop, InitializationResponse, Reason, RequestMemoryResponse, RequestRegistersResponse } from "../protocol/general";
import { Cdm16VariableProvider, RegisterController } from "./variables";


export class CdmDebugRuntime extends EventEmitter {
    private ws: WebSocket;
    private buffered: string[] = [];

    provider!: RegisterController;

    constructor(
        address: string,
        variablesReference: number,
    ) {
        super();

        this.ws = new WebSocket(address);
        this.ws.on("message", (data) => {
            let decoded = data.toString();
            let unmarshalled = JSON.parse(decoded);

            switch (unmarshalled?.status) {
                case "OK": {
                    console.log(`Received a success message from the debug server: ${decoded}`);
                    break;
                }
                case "FAIL": {
                    console.error(`Received an error message from the debug server: ${decoded}`);
                    return;
                }
                default: {
                    console.error(`Received a malformed message from the debug server: ${decoded}`);
                    return;
                }
            }

            switch (unmarshalled?.action) {
                case "init": {
                    let casted: InitializationResponse = unmarshalled;
                    let { supportsExceptions, registerNames, registerSizes, ramSize } = casted;
                    const newRef = this.provider.initialize(variablesReference, registerNames, registerSizes);
                    this.emit("initialized", supportsExceptions, newRef, ramSize);
                    break;
                }
                case "load": {
                    this.emit("loaded");
                    break;
                }
                case "setBreakpoints": {
                    this.emit("setBreakpoints");
                    break;
                }
                case "setLineLocations": {
                    this.emit("setLines");
                    break;
                }
                case "run": {
                    this.emit("run");
                    break;
                }
                case "getRegisters": {
                    let casted: RequestRegistersResponse = unmarshalled;
                    this.provider.set(casted.registers);
                    this.emit("receivedRegisters");
                    break;
                }
                case "getMemory": {
                    let casted: RequestMemoryResponse = unmarshalled;
                    this.emit("receivedMemory", casted.bytes);
                    break;
                }
                case "debugEvent": {
                    let casted: ExecutionStop = unmarshalled;
                    this.emit("stopped", casted.reason);
                    break;
                }
                default: {
                    return;
                }
            }
        });

        this.ws.once("open", () => {
            console.log(`Websocket has connected to the debug server, sending buffered messages to the debug server, message quantity - ${this.buffered.length}`);
            this.buffered.forEach((message) => {
                this.ws.send(message);
            });
        });
    }

    on(eventName: "initialized", listener: (supportsExceptions: boolean, variablesReference: number, ramSize: number) => void): this;
    on(eventName: "loaded", listener: () => void): this;
    on(eventName: "setBreakpoints", listener: () => void): this;
    on(eventName: "setLines", listener: () => void): this;
    on(eventName: "run", listener: () => void): this;
    on(eventName: "receivedRegisters", listener: () => void): this;
    on(eventName: "receivedMemory", listener: (bytes: number[]) => void): this;
    on(eventName: "stopped", listener: (reason: Reason) => void): this;
    on(eventName: string | symbol, listener: (...args: any[]) => void): this {
        return super.on(eventName, listener);
    }

    once(eventName: "initialized", listener: (supportsExceptions: boolean, variablesReference: number, ramSize: number) => void): this;
    once(eventName: "loaded", listener: () => void): this;
    once(eventName: "setBreakpoints", listener: () => void): this;
    once(eventName: "setLines", listener: () => void): this;
    once(eventName: "run", listener: () => void): this;
    once(eventName: "receivedRegisters", listener: () => void): this;
    once(eventName: "receivedMemory", listener: (bytes: number[]) => void): this;
    once(eventName: "stopped", listener: (reason: Reason) => void): this;
    once(eventName: string | symbol, listener: (...args: any[]) => void): this {
        return super.once(eventName, listener);
    }    

    private send(obj: any): void {
        let marshalled = JSON.stringify(obj);
        if (this.ws.readyState !== this.ws.OPEN) {
            console.log(`Pushing message to buffer, as websocket hasn't connected to the debug server yet; message - ${marshalled}`);
            this.buffered.push(marshalled);
        } else {
            console.log(`Sending message directly to the debug server; message - ${marshalled}`);
            this.ws.send(marshalled);
        }
    }

    initialize(target: TargetID, arch: ArchitectureID): this {
        if (target === "cdm16") {
            this.provider = new Cdm16VariableProvider();
        }

        this.send({
            action: "init",
            target: target,
            arch: arch,
        });
        return this;
    }

    loadFromPath(path: string): this {
        this.send({
            action: "load",
            source: "path",
            path: path,
        });
        return this;
    }

    loadFromBytes(bytes: number[]): this {
        this.send({
            action: "load",
            source: "bytes",
            bytes: bytes,
        });
        return this;
    }

    reset(): this {
        this.send({
            action: "reset",
        });
        return this;
    }

    setBreakpoints(locations: number[]): this {
        this.send({
            action: "setBreakpoints",
            breakpoints: locations,
        });
        return this;
    }

    setLines(locations: number[]): this {
        this.send({
            action: "setLineLocations",
            lineLocations: locations,
        });
        return this;
    }

    run(conditions: BreakCondition[]): this {
        this.send({
            action: "run",
            stopConditions: conditions,
        });
        return this;
    }

    pause(): this {
        this.send({
            action: "pause",
        });
        return this;
    }

    requestRegisters(): this {
        this.send({
            action: "getRegisters",
        });
        return this;
    }

    requestMemory(): this {
        this.send({
            action: "getMemory",
        });
        return this;
    }

    shutdown(): this {
        this.ws.close();
        return this;
    }
}
