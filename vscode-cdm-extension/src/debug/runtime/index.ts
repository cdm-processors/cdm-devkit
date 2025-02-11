import * as vscode from 'vscode';

import { EventEmitter } from "events";

import { WebSocket } from "ws";

import { ArchitectureId } from "../../protocol/architectures";
import { BreakCondition, ExecutionStop, InitializationResponse, Reason, RequestMemoryResponse, RequestRegistersResponse } from "../../protocol/general";
import { TargetGeneralId } from "../../protocol/targets";

export abstract class CdmDebugRuntime extends EventEmitter {
    protected address: string;

    protected ws!: WebSocket;
    protected buffered: string[] = [];

    public constructor(address: string) {
        super();

        this.address = address;
    }

    public async start() {
        this.ws = new WebSocket(this.address);

        const connectionConfiguration = vscode.workspace.getConfiguration("cdm.connection");
        const connectionTimeout = connectionConfiguration.get("timeout") as number;
        
        setTimeout(() => {
            if (this.ws.readyState !== this.ws.OPEN) {
                const errorMessage = "Websocket connection timeout";
                console.error(errorMessage);
                this.emit("error", errorMessage);
                return;
            }
        }, connectionTimeout);

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
                    this.emit("error", unmarshalled);
                    return;
                }
                default: {
                    console.error(`Received a malformed message from the debug server: ${decoded}`);
                    return;
                }
            }

            switch (unmarshalled?.action) {
                case "init": {
                    const { supportsExceptions, registerNames, registerSizes, ramSize } = unmarshalled as InitializationResponse;
                    this.emit("initialized", supportsExceptions, registerNames, registerSizes, ramSize);
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
                    const { registers } = unmarshalled as RequestRegistersResponse;
                    this.emit("receivedRegisters", registers);
                    break;
                }
                case "getMemory": {
                    const { bytes } = unmarshalled as RequestMemoryResponse;
                    this.emit("receivedMemory", bytes);
                    break;
                }
                case "debugEvent": {
                    const { reason } = unmarshalled as ExecutionStop;
                    this.emit("stopped", reason);
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

    public on(eventName: "initialized", listener: (supportsExceptions: boolean, registerNames: string[], registerSizes: number[], ramSize: number) => void): this;
    public on(eventName: "loaded", listener: () => void): this;
    public on(eventName: "setBreakpoints", listener: () => void): this;
    public on(eventName: "setLines", listener: () => void): this;
    public on(eventName: "run", listener: () => void): this;
    public on(eventName: "receivedRegisters", listener: (values: number[]) => void): this;
    public on(eventName: "receivedMemory", listener: (bytes: number[]) => void): this;
    public on(eventName: "stopped", listener: (reason: Reason) => void): this;
    public on(eventName: "error", listener: (body: any) => void): this;
    public on(eventName: string | symbol, listener: (...args: any[]) => void): this {
        return super.on(eventName, listener);
    }

    public once(eventName: "initialized", listener: (supportsExceptions: boolean, registerNames: string[], registerSizes: number[], ramSize: number) => void): this;
    public once(eventName: "loaded", listener: () => void): this;
    public once(eventName: "setBreakpoints", listener: () => void): this;
    public once(eventName: "setLines", listener: () => void): this;
    public once(eventName: "run", listener: () => void): this;
    public once(eventName: "receivedRegisters", listener: (values: number[]) => void): this;
    public once(eventName: "receivedMemory", listener: (bytes: number[]) => void): this;
    public once(eventName: "stopped", listener: (reason: Reason) => void): this;
    public once(eventName: "error", listener: (body: any) => void): this;
    public once(eventName: string | symbol, listener: (...args: any[]) => void): this {
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

    public initialize(target: TargetGeneralId, arch: ArchitectureId): this {
        this.send({
            action: "init",
            target: target,
            memoryConfiguration: arch,
        });
        return this;
    }

    public loadFromPath(path: string): this {
        this.send({
            action: "load",
            source: "path",
            path: path,
        });
        return this;
    }

    public loadFromBytes(bytes: number[]): this {
        this.send({
            action: "load",
            source: "bytes",
            bytes: bytes,
        });
        return this;
    }

    public reset(): this {
        this.send({
            action: "reset",
        });
        return this;
    }

    public setBreakpoints(locations: number[]): this {
        this.send({
            action: "setBreakpoints",
            breakpoints: locations,
        });
        return this;
    }

    public setLines(locations: number[]): this {
        this.send({
            action: "setLineLocations",
            lineLocations: locations,
        });
        return this;
    }

    public run(conditions: BreakCondition[]): this {
        this.send({
            action: "run",
            stopConditions: conditions,
        });
        return this;
    }

    public pause(): this {
        this.send({
            action: "pause",
        });
        return this;
    }

    public requestRegisters(): this {
        this.send({
            action: "getRegisters",
        });
        return this;
    }

    public requestMemory(offset: number, size: number): this {
        this.send({
            action: "getMemory",
            offset: offset,
            size: size,
        });
        return this;
    }

    public shutdown(): this {
        if (this.ws) {
            this.ws.close();
            console.log(`WebSocket connection closed.`);
        } else {
            console.warn(`No WebSocket connection found to shut down.`);
        }
        return this;
    }
}





