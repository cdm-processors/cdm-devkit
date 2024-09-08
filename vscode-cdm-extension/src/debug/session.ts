import * as fsPromises from "fs/promises";

import * as vscode from "vscode";
import { DebugSession, ExitedEvent, InitializedEvent, StackFrame, StoppedEvent, TerminatedEvent, Thread } from "@vscode/debugadapter";
import { DebugProtocol } from "@vscode/debugprotocol";

import { CdmDebugRuntime } from "./runtime";
import { DebugInfoHander } from "./breakpoints";
import { ReferenceController, RegisterProvider } from "./variables";
import { ArchitectureId } from "../protocol/architectures";
import { BREAKPOINT, EXCEPTION, PAUSE, STEP, STOP } from "../protocol/general";
import { TargetGeneralId } from "../protocol/targets";
import { MemoryViewManager, SymlinkManager } from "./memoryView";

export type CdmLaunchRequestArguments = DebugProtocol.LaunchRequestArguments & {
    address: string;
    architecture: ArchitectureId;
    target: TargetGeneralId;
    artifacts: {
        image: string;
        debug: string;
    };
};

export class CdmDebugSession extends DebugSession {
    private static THREAD_ID = 1;
    private static FRAME_ID = 1;

    private controller = new ReferenceController();
    private isConfigured = false;
    private memoryView: MemoryViewManager;

    private registerProvider!: RegisterProvider;
    private runtime!: CdmDebugRuntime;
    private debugInfoHandler!: DebugInfoHander;

    private ram!: number;
    private image!: string;

    public constructor(temporaryDirectory: string) {
        super();

        this.memoryView = new SymlinkManager(temporaryDirectory);
    }

    protected customRequest(
        command: string,
        _response: DebugProtocol.Response,
        _args: any,
        _request?: DebugProtocol.Request,
    ): void {
        if (command === "openMemoryView") {
            this.memoryView.createTab();
        }
    }

    protected initializeRequest(
        response: DebugProtocol.InitializeResponse,
        _args: DebugProtocol.InitializeRequestArguments,
    ): void {
        console.log("Received a InitializeRequest from the client");

        response.body = {
            supportsConfigurationDoneRequest: true,
            // TODO (kapkekes): add debug information handler support
            supportsRestartRequest: false,
            supportsConditionalBreakpoints: undefined,
            supportsHitConditionalBreakpoints: undefined,
            exceptionBreakpointFilters: undefined,
        };

        this.sendResponse(response);
        console.log("Sent a InitializeResponse response to the client");
    }

    protected async launchRequest(
        response: DebugProtocol.LaunchResponse,
        args: CdmLaunchRequestArguments,
        _request?: DebugProtocol.Request,
    ): Promise<void> {
        console.log("Received a LaunchRequest from the client");

        const { address, architecture, target, artifacts: { image, debug } } = args;
        this.image = image;

        this.runtime = new CdmDebugRuntime(address);
        this.runtime.once("initialized", (exceptions, names, sizes, ram) => {
            this.ram = ram;
            this.controller.issueReference((ref) => {
                return new RegisterProvider(this.controller, ref, names, sizes);
            }).then((provider) => this.registerProvider = provider as RegisterProvider);

        }).on("receivedMemory", (bytes) => {
            this.memoryView.updateDump(new Uint8Array(bytes));

        }).on("receivedRegisters", (values) => {
            this.registerProvider.update(values);

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
            vscode.window.showErrorMessage(`Something went terribly wrong with the debug server; contact the developers and show them this!\n${JSON.stringify(body)}`);

        }).initialize(target, architecture).setLines([]).setBreakpoints([]).reset();

        try {
            const contents = await fsPromises.readFile(debug, { encoding: "utf-8" }).then(JSON.parse);
            this.debugInfoHandler = DebugInfoHander.parse(contents);
        } catch {
            this.sendEvent(new TerminatedEvent());
            vscode.window.showErrorMessage("Failed to initialize a debug information handler");
            return;
        }

        this.runtime.once("loaded", () => {
            this.runtime.setLines(Array.from(this.debugInfoHandler.stepLocations()));
            this.sendEvent(new InitializedEvent());
            this.sendResponse(response);
            console.log("Sent a LaunchResponse response to the client");
        }).loadFromPath(image);
    }

    protected setBreakPointsRequest(
        response: DebugProtocol.SetBreakpointsResponse,
        args: DebugProtocol.SetBreakpointsArguments,
        _request?: DebugProtocol.Request,
    ): void {
        console.info("Received a SetBreakpointsRequest from the client");

        response.body = {
            breakpoints: this.debugInfoHandler.validateBreakpoints(args.source.path!, args.breakpoints!)
        };
        if (this.isConfigured) {
            this.runtime.setBreakpoints(this.debugInfoHandler.emitBreakpointLocations());
        }

        this.sendResponse(response);
        console.info("Sent a SetBreakpointsResponse response to the client");
    }

    protected configurationDoneRequest(
        response: DebugProtocol.ConfigurationDoneResponse,
        _args: DebugProtocol.ConfigurationDoneArguments,
        _request?: DebugProtocol.Request,
    ): void {
        console.info("Received a ConfigurationDoneRequest from the client");

        this.runtime.setBreakpoints(this.debugInfoHandler.emitBreakpointLocations()).run([BREAKPOINT, EXCEPTION]);
        this.isConfigured = true;

        this.sendResponse(response);
        console.info("Sent a ConfigurationDoneResponse response to the client");
    }

    protected threadsRequest(
        response: DebugProtocol.ThreadsResponse,
        _request?: DebugProtocol.Request
    ): void {
        console.info("Received a ThreadsRequest from the client");

        response.body = {
            threads: [new Thread(CdmDebugSession.THREAD_ID, "main")],
        };

        this.sendResponse(response);
        console.info("Sent a ThreadsResponse response to the client");
    }

    protected stackTraceRequest(
        response: DebugProtocol.StackTraceResponse,
        args: DebugProtocol.StackTraceArguments,
        _request?: DebugProtocol.Request,
    ): void {
        console.info("Received a StackTraceRequest from the client");

        if (args.threadId !== CdmDebugSession.THREAD_ID) {
            this.sendResponse(response);
            return console.warn("The client sent an invalid thread ID, sent an empty StackTraceResponse response to the client");
        }

        this.runtime.once("receivedRegisters", () => {
            let { source, line } = this.debugInfoHandler.restoreSourceLocation(this.registerProvider.programCounter()) ?? {};

            const frame = new StackFrame(CdmDebugSession.FRAME_ID, "main", source, line);
            response.body = { stackFrames: [frame], totalFrames: 1 };

            this.sendResponse(response);
            console.info("Sent a StackTraceResponse response to the client");
        }).requestRegisters().requestMemory(0, this.ram);
    }

    protected scopesRequest(
        response: DebugProtocol.ScopesResponse,
        args: DebugProtocol.ScopesArguments,
        _request?: DebugProtocol.Request,
    ): void {
        console.info("Received a ScopesRequest from the client");

        if (args.frameId !== CdmDebugSession.FRAME_ID) {
            this.sendResponse(response);
            return console.warn("The client sent an invalid frame ID, sent an empty ScopesResponse response to the client");
        }

        response.body = {
            scopes: [
                this.registerProvider.scope,
            ],
        };

        this.sendResponse(response);
        console.info("Sent a ScopesResponse response to the client");
    }

    protected variablesRequest(
        response: DebugProtocol.VariablesResponse,
        args: DebugProtocol.VariablesArguments,
        _request?: DebugProtocol.Request,
    ): void {
        console.info("Received a VariablesRequest from the client");

        response.body = {
            variables: this.controller.retrieve(args.variablesReference)?.slice(args.start, args.count) ?? [],
        };

        this.sendResponse(response);
        console.info("Sent a VariablesResponse response to the client");
    }

    protected restartRequest(
        response: DebugProtocol.RestartResponse,
        args: DebugProtocol.RestartArguments,
        _request?: DebugProtocol.Request,
    ): void {
        console.info("Received a RestartRequest from the client");

        this.runtime.pause().reset().loadFromPath(this.image).run([EXCEPTION, BREAKPOINT]);

        this.sendResponse(response);
        console.info("Sent a RestartResponse response to the client");
    }

    protected pauseRequest(
        response: DebugProtocol.PauseResponse,
        _args: DebugProtocol.PauseArguments,
        _request?: DebugProtocol.Request,
    ): void {
        console.info("Received a PauseRequest from the client");

        this.runtime.pause();

        this.sendResponse(response);
        console.info("Sent a PauseResponse response to the client");
    }

    protected continueRequest(
        response: DebugProtocol.ContinueResponse,
        _args: DebugProtocol.ContinueArguments,
        _request?: DebugProtocol.Request,
    ): void {
        console.info("Received a ContinueRequest from the client");

        this.runtime.run([EXCEPTION, BREAKPOINT]);

        this.sendResponse(response);
        console.info("Sent a ContinueResponse response to the client");
    }

    protected stepInRequest(
        response: DebugProtocol.StepInResponse,
        _args: DebugProtocol.StepInArguments,
        _request?: DebugProtocol.Request,
    ): void {
        console.info("Received a StepInRequest from the client");

        this.runtime.run([EXCEPTION, BREAKPOINT, STEP]);

        this.sendResponse(response);
        console.info("Sent a StepInResponse response to the client");
    }

    protected nextRequest(
        response: DebugProtocol.StepOutResponse,
        _args: DebugProtocol.StepOutArguments,
        _request?: DebugProtocol.Request,
    ): void {
        console.info("Received a NextRequest from the client");

        this.runtime.run([EXCEPTION, BREAKPOINT, STEP]);

        this.sendResponse(response);
        console.info("Sent a NextResponse response to the client");
    }

    protected stepOutRequest(
        response: DebugProtocol.StepOutResponse,
        _args: DebugProtocol.StepOutArguments,
        _request?: DebugProtocol.Request,
    ): void {
        console.info("Received a StepOutRequest from the client");

        vscode.window.showInformationMessage("'Step Out' action isn't supported yet.");
        this.sendEvent(new StoppedEvent("step", CdmDebugSession.THREAD_ID));

        this.sendResponse(response);
        console.info("Sent a StepOutResponse response to the client");
    }

    protected disconnectRequest(
        response: DebugProtocol.DisconnectResponse,
        _args: DebugProtocol.DisconnectArguments,
        _request?: DebugProtocol.Request,
    ): void {
        console.info("Received a DisconnectRequest from the client");

        this.runtime.pause().shutdown();
        this.memoryView.closeAllTabs();

        this.sendResponse(response);
        console.info("Sent a DisconnectResponse response to the client");
    }
}
