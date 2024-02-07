import * as fs from "fs/promises";
import * as pathlib from "path";
import * as os from "os";

import * as vscode from "vscode";
import { DebugSession, TerminatedEvent } from "@vscode/debugadapter";
import { DebugProtocol } from "@vscode/debugprotocol";

import { CdmDebugRuntime } from "./runtime";
import { ArchitectureID } from "../protocol/architectures";
import { TargetID } from "../protocol/targets";
import { createPingPong } from "../utils";

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

export class CdmDebugSession extends DebugSession {
    private static THREAD_ID = 1;

    private config = vscode.workspace.getConfiguration("cdm.build");
    private runtime!: CdmDebugRuntime;
    private debugInformation!: DebugInformation;

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
        let command = `cocas ${sources.join(" ")} --output ${image} --debug ${debug} -t ${target}`;
        let shell = new vscode.ShellExecution(command);
        return new vscode.Task({ "type": "cdm" }, 2, "compile", "CdM", shell);
    }

    protected async launchRequest(
        response: DebugProtocol.LaunchResponse,
        args: CdmLaunchArguments,
        request?: DebugProtocol.Request,
    ): Promise<void> {
        this.runtime = new CdmDebugRuntime(args.address);
        this.runtime.initialize(args.target, args.architecture);

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
        let path = await fs.mkdtemp(pathlib.join(os.tmpdir(), "cdm-"));

        image ? await fs.mkdir(pathlib.dirname(image), { recursive: true }) : null;
        debug ? await fs.mkdir(pathlib.dirname(debug), { recursive: true }) : null;

        image ??= pathlib.join(path, "out.img");
        debug ??= pathlib.join(path, "out.dbg");

        let _ = await vscode.tasks.executeTask(this.compileSources(args.target, args.sources, image, debug));
        while (!this.debugInformation) {
            this.debugInformation = await fs.readFile(debug, { encoding: "utf-8" }).then(JSON.parse).catch(() => {});
            let _ = await new Promise(f => setTimeout(f, 100));
        }

        let imageLoaded = createPingPong<void>();
        this.runtime.once("loaded", () => imageLoaded.ping()).loadFromPath(image);

        await imageLoaded.pong();
        await fs.rm(path, { recursive: true, force: true });
    }
}
