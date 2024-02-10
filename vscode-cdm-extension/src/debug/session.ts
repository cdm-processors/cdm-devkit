import * as fs from "fs/promises";
import * as pathlib from "path";
import * as os from "os";

import * as vscode from "vscode";
import { ContinuedEvent, DebugSession, ExitedEvent, InitializedEvent, Source, StackFrame, StoppedEvent, TerminatedEvent } from "@vscode/debugadapter";
import { DebugProtocol } from "@vscode/debugprotocol";

import { CdmDebugRuntime } from "./runtime";
import { ArchitectureID } from "../protocol/architectures";
import { TargetID } from "../protocol/targets";
import { BREAKPOINT, EXCEPTION, PAUSE, STEP, STOP } from "../protocol/general";

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

type LineLocation = {
    f: number;
    l: number;
    c: number;
};

type DebugInformation = {
    files: string[];
    codeLocations: Map<number, LineLocation>;
};

type Register = {
    size: number;
    value: number;
};

export class CdmDebugSession extends DebugSession {
    private static THREAD_ID = 1;

    private runtime!: CdmDebugRuntime;
    private debugInformation!: DebugInformation;
    private registers!: Map<string, Register>;

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
        this.runtime = new CdmDebugRuntime(args.address);
        this.runtime.once("initialized", (exceptions, names, sizes, ram) => {
            this.registers = new Map();
            names.forEach((name, index) => {
                this.registers.set(name, { size: sizes[index], value: NaN });
            });
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
        while (!this.debugInformation) {
            const raw = await fs.readFile(debug, { encoding: "utf-8" }).then(JSON.parse).catch(() => {});

            if (!raw) {
                let _ = await new Promise(f => setTimeout(f, 100));
                continue;
            }

            this.debugInformation = { files: raw.files, codeLocations: new Map() };
            Object.entries(raw.codeLocations).forEach(([key, value]) => {
                this.debugInformation.codeLocations.set(Number(key), value as LineLocation);
            });
        }

        this.runtime.once("loaded", async () => {
            await fs.rm(path, { recursive: true, force: true });
            this.runtime.setLines(Array.from(this.debugInformation.codeLocations.keys()));
            this.sendEvent(new InitializedEvent());
            this.runtime.reset().run([BREAKPOINT, EXCEPTION]);
            this.sendResponse(response);
            console.log("Sent a LaunchResponse response to the client");
        }).loadFromPath(image);
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
        request?: DebugProtocol.Request | undefined,
    ): void {
        console.log("Received a StackTraceRequest from the client");

        this.runtime.once("receivedRegisters", (values) => {
            const registers = this.registers.values();
            values.forEach((value) => {
                registers.next().value.value = value;
            });
            console.log(this.registers);

            const programCounter = this.registers.get("pc")!.value;
            const lineLocation = this.debugInformation.codeLocations.get(programCounter);
            if (lineLocation === undefined) {
                return console.error(`Program counter has an invalid value: ${lineLocation}`);
            }

            const file = this.debugInformation.files[lineLocation.f];
            const short = file.substring(file.lastIndexOf("/"));
            const frame = new StackFrame(0, "main", new Source(short, file), lineLocation.l);

            response.body = {
                stackFrames: [frame],
                totalFrames: 1,
            };

            this.sendResponse(response);
            console.log("Sent a StackTraceResponse response to the client");
        }).requestRegisters();
    }

    protected restartRequest(
        response: DebugProtocol.RestartResponse,
        args: DebugProtocol.RestartArguments,
        request?: DebugProtocol.Request | undefined
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
        request?: DebugProtocol.Request | undefined
    ): void {
        console.log("Received a PauseRequest from the client");

        this.runtime.pause();

        this.sendResponse(response);
        console.log("Sent a PauseResponse response to the client");
    }

    protected continueRequest(
        response: DebugProtocol.ContinueResponse,
        args: DebugProtocol.ContinueArguments,
        request?: DebugProtocol.Request | undefined
    ): void {
        console.log("Received a ContinueRequest from the client");

        this.runtime.run([EXCEPTION, BREAKPOINT]);

        this.sendResponse(response);
    }

    protected stepInRequest(
        response: DebugProtocol.StepInResponse,
        args: DebugProtocol.StepInArguments,
        request?: DebugProtocol.Request | undefined
    ): void {
        console.log("Received a StepInRequest from the client");

        this.runtime.run([EXCEPTION, BREAKPOINT, STEP]);

        this.sendResponse(response);
    }

    protected disconnectRequest(response: DebugProtocol.DisconnectResponse, args: DebugProtocol.DisconnectArguments, request?: DebugProtocol.Request | undefined): void {
        console.log("Received a DisconnectRequest from the client");

        this.runtime.pause();
        this.runtime.shutdown();

        this.sendResponse(response);
    }
}
