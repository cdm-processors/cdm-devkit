import * as vscode from "vscode";
import { ContinuedEvent, DebugSession, ExitedEvent, InitializedEvent, StoppedEvent } from "@vscode/debugadapter";
import { DebugProtocol } from "@vscode/debugprotocol";

import { CdmRegistersProvider } from "../views/registers";
import { CdmRuntime } from "./runtime";

interface CdmLaunchArguments extends DebugProtocol.LaunchRequestArguments {
    sources: string[],
    artifacts: {
        image: string,
        debug: string,
    }
}

export class CdmDebugSession extends DebugSession {
    private static THREAD_ID = 1;
    private runtime: CdmRuntime;
    private config: vscode.WorkspaceConfiguration;

    constructor(
        private registersProvider: CdmRegistersProvider
    ) {
        super();

        this.config = vscode.workspace.getConfiguration("cdm.debug");
        this.runtime = new CdmRuntime(this.config.get("address")!);

        this.runtime.on("stopped", (reason) => {
            switch (reason) {
                case "breakpoint":
                case "exception": {
                    this.sendEvent(new StoppedEvent(reason, CdmDebugSession.THREAD_ID));
                    break;
                }
                case "line": {
                    this.sendEvent(new StoppedEvent("step", CdmDebugSession.THREAD_ID));
                }
                case "halt": {
                    this.sendEvent(new ExitedEvent(0));
                }
            }

            this.sendEvent(new StoppedEvent(reason, CdmDebugSession.THREAD_ID));
        });
    }

    protected initializeRequest(response: DebugProtocol.InitializeResponse, args: DebugProtocol.InitializeRequestArguments): void {
        console.log("Initializing the debug adapter;");

        this.runtime.once("initialized", (supportsExceptions, registers, ramSize) => {
            response.body = {
                supportsRestartRequest: false,
            };

            this.sendResponse(response);
            this.sendEvent(new InitializedEvent());
        });

        this.runtime.initialize(this.config.get("target")!, this.config.get("architecture")!);
    }

    protected threadsRequest(response: DebugProtocol.ThreadsResponse, request?: DebugProtocol.Request | undefined): void {
        console.log("Sending information about threads to VS Code");
        response.body = {"threads": [{ "id": CdmDebugSession.THREAD_ID, "name": "main" }]};
        this.sendResponse(response);
    }

    protected launchRequest(response: DebugProtocol.LaunchResponse, args: CdmLaunchArguments, request?: DebugProtocol.Request | undefined): void {
        let { image, debug } = args.artifacts;
        vscode.tasks.executeTask(new vscode.Task(
            { "type": "cdm" }, 2, "compile", "CdM",
            new vscode.ShellExecution(`cocas ${args.sources.join(" ")} -o ${image} --debug ${debug} -t ${this.config.get("target")!}`)
        ));

        this.runtime.once("loaded", () => console.log(`Debug server loaded sources from ${image};`));
        this.runtime.reset();
        this.runtime.loadFromPath(image);
        this.runtime.run("breakpoint", "exception", "line", "halt");
        this.sendResponse(response);
    }

    protected restartRequest(response: DebugProtocol.RestartResponse, args: DebugProtocol.RestartArguments, request?: DebugProtocol.Request | undefined): void {
        this.runtime.reset();
        this.sendResponse(response);
    }

    protected pauseRequest(response: DebugProtocol.PauseResponse, args: DebugProtocol.PauseArguments, request?: DebugProtocol.Request | undefined): void {
        console.log("Sending request to pause the execution");
        this.runtime.pause();
        this.sendResponse(response);
    }

    protected continueRequest(response: DebugProtocol.ContinueResponse, args: DebugProtocol.ContinueArguments, request?: DebugProtocol.Request | undefined): void {
        console.log("Sending request to continue the execution");
        this.runtime.run("breakpoint", "exception", "line", "halt");
        this.sendResponse(response);
    }

    protected disconnectRequest(response: DebugProtocol.DisconnectResponse, args: DebugProtocol.DisconnectArguments, request?: DebugProtocol.Request | undefined): void {
        this.runtime.pause();
        this.runtime.shutdown();
        this.sendResponse(response);
    }
}
