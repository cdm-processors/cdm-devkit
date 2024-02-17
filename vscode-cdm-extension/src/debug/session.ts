import * as fs from "fs/promises";
import * as pathlib from "path";

import * as vscode from "vscode";
import { DebugSession, ExitedEvent, InitializedEvent, StackFrame, StoppedEvent, TerminatedEvent } from "@vscode/debugadapter";
import { DebugProtocol } from "@vscode/debugprotocol";

import { CdmDebugRuntime } from "./runtime";
import { BREAKPOINT, EXCEPTION, PAUSE, STEP, STOP } from "../protocol/general";
import { BreakpointHandler } from "./breakpoints";
import { createLifter } from "../lifter";
import { CdmLaunchArguments } from "./configurations";
import { ReferenceController, RegisterProvider } from "./variables";

export class CdmDebugSession extends DebugSession {
    private static THREAD_ID = 1;
    private static FRAME_ID = 1;

    private controller = new ReferenceController();
    private views = new Map<string, { offset: number, size: number, current: number }>();
    private viewUpdateQueue: string[] = [];

    private registerProvider!: RegisterProvider;
    private runtime!: CdmDebugRuntime;
    private handler!: BreakpointHandler;

    private ram!: number;
    private image!: string;
    private tempDirectory!: string;

    private updateMemoryView(path: string) {
        this.viewUpdateQueue.push(path);
        const { offset, size, current } = this.views.get(path)!;
        const realOffset = offset + size * current;
        this.runtime.requestMemory(realOffset, realOffset + size < this.ram ? size : this.ram - realOffset);
    }

    private createMemoryView() {
        const tempFile = pathlib.join(this.tempDirectory, `memory-view-${this.views.size}.hex`);
        const view = { offset: 0, size: 256, current: 0 };
        this.views.set(tempFile, view);
        this.runtime.requestMemory(view.offset + view.size * view.current, view.size).once("receivedMemory", (bytes) => {
            fs.writeFile(tempFile, new Uint8Array(bytes)).then(() => {
                vscode.commands.executeCommand("vscode.openWith", vscode.Uri.parse(`file://${tempFile}`), "hexEditor.hexedit", { preserveFocus: true, viewColumn: vscode.ViewColumn.Beside }); 
            });
        });
    }

    private previousMemoryView(path: string) {
        const view = this.views.get(path);
        if (view && view.current > 0) {
            view.current -= 1;
            this.views.set(path, view);
            this.updateMemoryView(path);
        }
    }

    private nextMemoryView(path: string) {
        const view = this.views.get(path);
        if (view && view.offset + (view.current + 1) * view.size < this.ram) {
            view.current += 1;
            this.views.set(path, view);
            this.updateMemoryView(path);
        }
    }

    private setViewOffset(path: string, offset: number) {
        const view = this.views.get(path);
        if (view && offset < this.ram) {
            view.offset = offset;
            view.current = 0;
            view.size = view.offset + view.size < this.ram ? view.size : this.ram - view.size;
            this.updateMemoryView(path);
        }
    }

    private setViewRange(path: string, range: number) {
        const view = this.views.get(path);
        if (view && view.offset + range <= this.ram) {
            view.current = 0;
            view.size = range;
            this.updateMemoryView(path);
        }
    }

    private setViewPage(path: string, page: number) {
        const view = this.views.get(path);
        if (view && view.offset + view.size * page < this.ram) {
            view.current = page;
            this.updateMemoryView(path);
        }
    }

    protected customRequest(
        command: string,
        response: DebugProtocol.Response,
        args: any,
        request?: DebugProtocol.Request,
    ): void {
        switch (command) {
            case "createMemoryView": {
                this.createMemoryView();
                break;
            }
            case "previousMemoryView": {
                this.previousMemoryView(args.path);
                break;
            }
            case "nextMemoryView": {
                this.nextMemoryView(args.path);
                break;
            }
            case "setViewOffset": {
                this.setViewOffset(args.path, args.offset);
                break;
            }
            case "setViewRange": {
                this.setViewRange(args.path, args.range);
                break;
            }
            case "setViewPage": {
                this.setViewPage(args.path, args.page);
                break;
            }
            default:
        }
    }

    protected initializeRequest(
        response: DebugProtocol.InitializeResponse,
        args: DebugProtocol.InitializeRequestArguments,
    ): void {
        console.log("Received a InitializeRequest from the client");

        response.body = {
            supportsConfigurationDoneRequest: true,
            supportsRestartRequest: true,
            supportsConditionalBreakpoints: undefined,
            supportsHitConditionalBreakpoints: undefined,
            exceptionBreakpointFilters: undefined,
        };

        this.sendResponse(response);
        console.log("Sent a InitializeResponse response to the client");
    }

    protected async launchRequest(
        response: DebugProtocol.LaunchResponse,
        args: CdmLaunchArguments,
        request?: DebugProtocol.Request,
    ): Promise<void> {
        console.log("Received a LaunchRequest from the client");

        const { address, architecture, target, sources, artifacts: { image, debug }, tempDirectory } = args;
        this.image = image;
        this.tempDirectory = tempDirectory;

        const { event, submit } = createLifter<number>();
        const disposable = vscode.tasks.onDidEndTaskProcess((taskEvent) => {
            if (taskEvent.execution.task.source === "CdM") {
                submit(taskEvent.exitCode!);
            }
        });

        const command = `cocas ${sources.join(" ")} --output ${image} --debug ${debug} -t ${target}`;
        const shell = new vscode.ShellExecution(command);
        const task = new vscode.Task({ "type": "cdm" }, 2, "compile", "CdM", shell);
        const _ = await vscode.tasks.executeTask(task);

        const compileCode = await event();
        disposable.dispose();
        if (compileCode !== 0) {
            this.sendEvent(new TerminatedEvent());
            this.sendEvent(new ExitedEvent(compileCode));
            this.sendErrorResponse(response, compileCode);

            return;
        }

        this.runtime = new CdmDebugRuntime(address);
        this.runtime.once("initialized", (exceptions, names, sizes, ram) => {
            this.ram = ram;
            this.controller.issueReference((ref) => {
                return new RegisterProvider(this.controller, ref, names, sizes);
            }).then((provider) => this.registerProvider = provider as RegisterProvider);
        }).on("receivedMemory", (bytes) => {
            const view = this.viewUpdateQueue.shift();
            if (view) {
                fs.writeFile(view, new Uint8Array(bytes));
                // vscode.commands.executeCommand("workbench.action.files.revert");
            }
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
            this.sendEvent(new ExitedEvent(0));
            vscode.window.showErrorMessage(`Something went terribly wrong with the debug server; contact the developers and show them this!\n${JSON.stringify(body)}`);
        }).initialize(target, architecture).setLines([]).setBreakpoints([]).reset();

        const raw = await fs.readFile(debug, { encoding: "utf-8" }).then(JSON.parse).catch(() => {});

        const codeLocations = new Map();
        Object.entries(raw.codeLocations).forEach(([key, value]) => {
            codeLocations.set(Number(key), value);
        });
        this.handler = new BreakpointHandler(raw.files, codeLocations);

        this.runtime.once("loaded", () => {
            this.runtime.setLines(Array.from(this.handler.codes()));
            this.sendEvent(new InitializedEvent());
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
            let { checkedBreakpoints, codes } = this.handler.fromSetBreakpointsRequest(args.source.path, args.breakpoints) ?? {};
            if (codes) {
                this.runtime.setBreakpoints(codes);
            }

            response.body = { breakpoints: checkedBreakpoints ?? [] };
            this.sendResponse(response);

            console.log("Sent a SetBreakpointsResponse response to the client");
        }
    }

    protected configurationDoneRequest(
        response: DebugProtocol.ConfigurationDoneResponse,
        args: DebugProtocol.ConfigurationDoneArguments,
        request?: DebugProtocol.Request,
    ): void {
        console.log("Received a ConfigurationDoneRequest from the client");

        this.runtime.run([BREAKPOINT, EXCEPTION]);

        this.sendResponse(response);
        console.log("Sent a ConfigurationDoneResponse response to the client");
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

        this.views.forEach(({ offset, size, current }, view) => {
            this.viewUpdateQueue.push(view);
            this.runtime.requestMemory(offset + size * current, size);
        });

        this.runtime.once("receivedRegisters", () => {
            let { source, line } = this.handler.fromProgramCounter(this.registerProvider.programCounter()) ?? {};

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

        response.body = {
            scopes: [
                this.registerProvider.scope,
            ],
        };

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
            variables: this.controller.retrieve(args.variablesReference)?.slice(args.start, args.count) ?? [],
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

        this.runtime.pause().reset().loadFromPath(this.image).run([EXCEPTION, BREAKPOINT]);

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

    protected nextRequest(
        response: DebugProtocol.StepOutResponse,
        args: DebugProtocol.StepOutArguments,
        request?: DebugProtocol.Request,
    ): void {
        console.log("Received a NextRequest from the client");

        this.runtime.run([EXCEPTION, BREAKPOINT, STEP]);

        this.sendResponse(response);
        console.log("Sent a NextResponse response to the client");
    }

    protected stepOutRequest(
        response: DebugProtocol.StepOutResponse,
        args: DebugProtocol.StepOutArguments,
        request?: DebugProtocol.Request,
    ): void {
        console.log("Received a StepOutRequest from the client");

        vscode.window.showInformationMessage("'Step Out' action isn't supported yet.");
        this.sendEvent(new StoppedEvent("step", CdmDebugSession.THREAD_ID));

        this.sendResponse(response);
        console.log("Sent a StepOutResponse response to the client");
    }

    protected disconnectRequest(
        response: DebugProtocol.DisconnectResponse,
        args: DebugProtocol.DisconnectArguments,
        request?: DebugProtocol.Request,
    ): void {
        console.log("Received a DisconnectRequest from the client");

        this.runtime.pause().shutdown();

        vscode.window.tabGroups.all.forEach((group) => {
            group.tabs.forEach((tab) => {
                if (tab.label.startsWith("memory-view-") && tab.label.endsWith(".hex")) {
                    vscode.window.tabGroups.close(tab);
                }
            });
        });
        fs.rm(this.tempDirectory, { recursive: true, force: true }).catch(() => {
			console.error(`Failed to recursively remove the temporary directory at ${this.tempDirectory}`);
		});

        this.sendResponse(response);
        console.log("Sent a DisconnectResponse response to the client");
    }
}
