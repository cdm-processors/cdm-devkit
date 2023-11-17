import * as pathlib from "node:path";

import { ShellExecution, Task, tasks, window, workspace } from "vscode";
import { DebugSession } from "@vscode/debugadapter";
import { DebugProtocol } from "@vscode/debugprotocol";
import WebSocket from "ws";

import { InitializationResponse, Target } from "../adapterServerProtocol";

interface CdmInitializeArguments extends DebugProtocol.InitializeRequestArguments {
    serverAddress: string,
    target: Target,
    program: string,
}

export class CdmDebugSession extends DebugSession {
    private static threadID = 1;
    private ws: WebSocket | null = null;

    protected initializeRequest(response: DebugProtocol.InitializeResponse, args: CdmInitializeArguments): void {
        let parsed_asm_path = pathlib.parse(args.program);
        let img_path = pathlib.join(parsed_asm_path.dir, parsed_asm_path.name + ".img");
        let dbg_path = pathlib.join(parsed_asm_path.dir, parsed_asm_path.name + ".dbg");

        tasks.executeTask(new Task(
            { "type": "cdm" },
            workspace.workspaceFolders!![0],
            "compile",
            "CdM",
            new ShellExecution(`cocas ${args.program} -o ${img_path} --debug ${dbg_path}`)
        ));

        console.log(`Connecting to the debug server at ${args.serverAddress}`);
        this.ws = new WebSocket(args.serverAddress);
        this.ws.on("open", () => {
            let messageBuffer: Array<string> = [];
            this.ws?.on("message", (data, isBinary) => messageBuffer.push(data.toString()));

            this.ws?.send(JSON.stringify({
                "action": "init",
                "target": args.target,
                "memoryConfiguration": "vonNeumann",
            }));

            this.ws?.send(JSON.stringify({
                "action": "reset",
            }));

            this.ws?.send(JSON.stringify({
                "action": "load",
                "source": "path",
                "path": img_path,
            }));

            this.sendResponse(response);

            this.ws?.removeAllListeners();
        });
    }

    protected launchRequest(response: DebugProtocol.LaunchResponse, args: DebugProtocol.LaunchRequestArguments, request?: DebugProtocol.Request | undefined): void {
        this.ws?.send(JSON.stringify({
            "action": "run",
            "stopConditions": ["exception"],
        }));
    }

    protected disconnectRequest(response: DebugProtocol.DisconnectResponse, args: DebugProtocol.DisconnectArguments, request?: DebugProtocol.Request | undefined): void {
        console.log(`Disconnecting from the debug server at ${this.ws!.url}`);
        this.ws!.close();
        this.sendResponse(response);
    }
}
