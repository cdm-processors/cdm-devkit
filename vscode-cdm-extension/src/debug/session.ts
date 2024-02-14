import * as fs from "fs/promises";
import * as pathlib from "path";
import * as os from "os";

import * as vscode from "vscode";
import { ContinuedEvent, DebugSession, ExitedEvent, InitializedEvent, Scope, StackFrame, StoppedEvent, TerminatedEvent } from "@vscode/debugadapter";
import { DebugProtocol } from "@vscode/debugprotocol";

import { CdmDebugRuntime } from "./runtime";
import { ArchitectureID } from "../protocol/architectures";
import { TargetID } from "../protocol/targets";
import { BREAKPOINT, EXCEPTION, PAUSE, STEP, STOP } from "../protocol/general";
import { BreakpointHandler } from "./breakpoints";

type BuildArtifacts = {
    image: string;
    debug: string;
};

interface CdmLaunchArguments extends DebugProtocol.LaunchRequestArguments {
    address: string;
    architecture: ArchitectureID;
    target: TargetID;
    sources?: string[];
    artifacts: BuildArtifacts;
}

export class CdmDebugSession extends DebugSession {
    private static THREAD_ID = 1;
    private static FRAME_ID = 1;
    private registers_scope_id = 1;

    private runtime!: CdmDebugRuntime;
    private handler!: BreakpointHandler;

    protected initializeRequest(
        response: DebugProtocol.InitializeResponse,
        args: DebugProtocol.InitializeRequestArguments,
    ): void {
        response.body = {
            supportsConfigurationDoneRequest: true,
            supportsConditionalBreakpoints: undefined,
            supportsHitConditionalBreakpoints: undefined,
            exceptionBreakpointFilters: undefined,
            supportsRestartRequest: true,
        };

        this.sendResponse(response);
    }

    private compileSources(target: TargetID, sources: string[], image: string, debug: string): vscode.Task {
        const command = `cocas ${sources.join(" ")} --output ${image} --debug ${debug} -t ${target}`;
        const shell = new vscode.ShellExecution(command);
        return new vscode.Task({ "type": "cdm" }, 2, "compile", "CdM", shell);
    }

    protected async launchRequest(
        response: DebugProtocol.LaunchResponse,
        args: CdmLaunchArguments,
        request?: DebugProtocol.Request,
    ): Promise<void> {
        this.runtime = new CdmDebugRuntime(args.address, this.registers_scope_id);
        this.runtime.once("initialized", (exceptions, newRef, ram) => {
            this.registers_scope_id = newRef;
        }).on("stopped", (reason) => {
            switch (reason) {
                case PAUSE:
                case BREAKPOINT:
                case EXCEPTION: {
                    this.sendEvent(new StoppedEvent(reason, CdmDebugSession.THREAD_ID));
                    break;
                }
                case STEP: {
                    this.sendEvent(new StoppedEvent("step", CdmDebugSession.THREAD_ID));
                    break;
                }
                case STOP: {
                    this.sendEvent(new TerminatedEvent());
                    this.sendEvent(new ExitedEvent(0));
                    break;
                }
            }
        }).on("error", (body) => {
            this.sendEvent(new TerminatedEvent());
            this.sendEvent(new ExitedEvent(0));
            vscode.window.showErrorMessage(`Something went terribly wrong with the debug server; contact the developers and show them this!\n${JSON.stringify(body)}`);
        }).initialize(args.target, args.architecture);

        if (!args.sources && !vscode.window.activeTextEditor) {
            vscode.window.showErrorMessage("Open a .asm-file to launch debugging.");
            return this.sendEvent(new TerminatedEvent());
        } else if (!args.sources && !vscode.window.activeTextEditor!!.document.fileName.endsWith(".asm")) {
            vscode.window.showErrorMessage("The opened file should have a .asm extension.");
            return this.sendEvent(new TerminatedEvent());
        } else if (!args.sources) {
            args.sources = [vscode.window.activeTextEditor!!.document.fileName];
        }

        let { image, debug } = args.artifacts;
        const path = await fs.mkdtemp(pathlib.join(os.tmpdir(), "cdm-"));

        image ? await fs.mkdir(pathlib.dirname(image), { recursive: true }) : null;
        debug ? await fs.mkdir(pathlib.dirname(debug), { recursive: true }) : null;

        image ??= pathlib.join(path, "out.img");
        debug ??= pathlib.join(path, "out.dbg");

        const _ = await vscode.tasks.executeTask(this.compileSources(args.target, args.sources, image, debug));
        while (!this.handler) {
            const raw = await fs.readFile(debug, { encoding: "utf-8" }).then(JSON.parse).catch(() => {});

            if (!raw) {
                let _ = await new Promise(f => setTimeout(f, 100));
                continue;
            }

            const codeLocations = new Map();
            Object.entries(raw.codeLocations).forEach(([key, value]) => {
                codeLocations.set(Number(key), value);
            });
            this.handler = new BreakpointHandler(raw.files, codeLocations);
        }

        this.runtime.once("loaded", async () => {
            await fs.rm(path, { recursive: true, force: true });
            this.runtime.setLines(Array.from(this.handler.codes()));
            this.sendEvent(new InitializedEvent());
            this.runtime.reset().run([BREAKPOINT, EXCEPTION]);
            this.sendResponse(response);
            console.log("Sent a LaunchResponse response to the client");
        }).loadFromPath(image);
    }

    protected setBreakPointsRequest(
        response: DebugProtocol.SetBreakpointsResponse,
        args: DebugProtocol.SetBreakpointsArguments,
        request?: DebugProtocol.Request,
    ): void {
        console.log("Received a SetBreakpointsRequest from the client");

        if (args.source.path && args.breakpoints) {
            let { checkedBreakpoints, codes } = this.handler.fromSetBreakpointsRequest(args.source.path!, args.breakpoints) ?? {};
            if (codes) {
                this.runtime.setBreakpoints(codes);
            }

            response.body = { breakpoints: checkedBreakpoints ?? [] };
            this.sendResponse(response);

            console.log("Sent a SetBreakpointsResponse response to the client");
        }
    }

    protected threadsRequest(
        response: DebugProtocol.ThreadsResponse,
        request?: DebugProtocol.Request
    ): void {
        console.log("Received a ThreadsRequest from the client");

        response.body = {"threads": [{ "id": CdmDebugSession.THREAD_ID, "name": "main" }]};

        this.sendResponse(response);
        console.log("Sent a ThreadsResponse response to the client");
    }

    protected stackTraceRequest(
        response: DebugProtocol.StackTraceResponse,
        args: DebugProtocol.StackTraceArguments,
        request?: DebugProtocol.Request,
    ): void {
        console.log("Received a StackTraceRequest from the client");

        if (args.threadId !== CdmDebugSession.THREAD_ID) {
            this.sendResponse(response);
            console.warn("The client sent an invalid thread ID, sent an empty StackTraceResponse response to the client");
            return;
        }

        this.runtime.once("receivedRegisters", () => {
            let { source, line } = this.handler.fromProgramCounter(this.runtime.provider.programCounter()) ?? {};

            const frame = new StackFrame(CdmDebugSession.FRAME_ID, "main", source, line);
            response.body = { stackFrames: [frame], totalFrames: 1 };

            this.sendResponse(response);
            console.log("Sent a StackTraceResponse response to the client");
        }).requestRegisters();
    }

    protected scopesRequest(
        response: DebugProtocol.ScopesResponse,
        args: DebugProtocol.ScopesArguments,
        request?: DebugProtocol.Request,
    ): void {
        console.log("Received a ScopesRequest from the client");

        if (args.frameId !== CdmDebugSession.FRAME_ID) {
            this.sendResponse(response);
            return console.warn("The client sent an invalid frame ID, sent an empty ScopesResponse response to the client");
        }

        const scope = new Scope("REGISTERS", 1, false);
        response.body = { scopes: [scope] };

        this.sendResponse(response);
        console.log("Sent a ScopesResponse response to the client");
    }

    protected variablesRequest(
        response: DebugProtocol.VariablesResponse,
        args: DebugProtocol.VariablesArguments,
        request?: DebugProtocol.Request,
    ): void {
        console.log("Received a VariablesRequest from the client");

        response.body = {
            variables: this.runtime.provider.find(args.variablesReference)?.sliceVariables(args.start ?? 0, args.count) ?? []
        };

        this.sendResponse(response);
        console.log("Sent a VariablesResponse response to the client");
    }

    protected restartRequest(
        response: DebugProtocol.RestartResponse,
        args: DebugProtocol.RestartArguments,
        request?: DebugProtocol.Request,
    ): void {
        console.log("Received a RestartRequest from the client");

        this.runtime.pause();
        this.runtime.reset();
        this.runtime.run([EXCEPTION, BREAKPOINT]);

        this.sendEvent(new ContinuedEvent(CdmDebugSession.THREAD_ID));
        this.sendResponse(response);
        console.log("Sent a RestartResponse response to the client");
    }

    protected pauseRequest(
        response: DebugProtocol.PauseResponse,
        args: DebugProtocol.PauseArguments,
        request?: DebugProtocol.Request,
    ): void {
        console.log("Received a PauseRequest from the client");

        this.runtime.pause();

        this.sendResponse(response);
        console.log("Sent a PauseResponse response to the client");
    }

    protected continueRequest(
        response: DebugProtocol.ContinueResponse,
        args: DebugProtocol.ContinueArguments,
        request?: DebugProtocol.Request,
    ): void {
        console.log("Received a ContinueRequest from the client");

        this.runtime.run([EXCEPTION, BREAKPOINT]);

        this.sendResponse(response);
        console.log("Sent a ContinueResponse response to the client");
    }

    protected stepInRequest(
        response: DebugProtocol.StepInResponse,
        args: DebugProtocol.StepInArguments,
        request?: DebugProtocol.Request,
    ): void {
        console.log("Received a StepInRequest from the client");

        this.runtime.run([EXCEPTION, BREAKPOINT, STEP]);

        this.sendResponse(response);
        console.log("Sent a StepInResponse response to the client");
    }

    protected disconnectRequest(
        response: DebugProtocol.DisconnectResponse,
        args: DebugProtocol.DisconnectArguments,
        request?: DebugProtocol.Request,
    ): void {
        console.log("Received a DisconnectRequest from the client");

        this.runtime.pause();
        this.runtime.shutdown();

        this.sendResponse(response);
        console.log("Sent a DisconnectResponse response to the client");
    }
}
