import * as fs from "fs/promises";
import * as os from "os";
import * as pathlib from "path";

import * as vscode from "vscode";
import { DebugProtocol } from "@vscode/debugprotocol";
import { ArchitectureID } from "../protocol/architectures";
import { IDS, TargetID } from "../protocol/targets";

export interface BuildArtifacts {
    image: string;
    debug: string;
}

export interface CdmLaunchArguments extends DebugProtocol.LaunchRequestArguments {
    address: string;
    architecture: ArchitectureID;
    target: TargetID;
    sources: string[];
    artifacts: BuildArtifacts;
    tempDirectory: string;
}

async function mkdirparent(file: string) {
    const directory = pathlib.dirname(file);
    try {
        const _ = await fs.mkdir(directory, { recursive: true });
        await fs.access(directory);
    } catch (error) {
        vscode.window.showErrorMessage(`Failed to start the debugging: can't create a directory at \`${directory}\`.`);
        return false;
    }

    return true;
}

export class CdmConfigurationProvider implements vscode.DebugConfigurationProvider {
    public async resolveDebugConfigurationWithSubstitutedVariables(
        folder: vscode.WorkspaceFolder | undefined,
        debugConfig: vscode.DebugConfiguration,
        token?: vscode.CancellationToken,
    ): Promise<vscode.DebugConfiguration | null | undefined> {
        const tempDirectory = await fs.mkdtemp(pathlib.join(os.tmpdir(), "cdm-"));

        if (debugConfig.type !== "cdm" || debugConfig.request !== "launch") {
            return debugConfig;
        }

        if (!debugConfig?.sources) {
            const openFile = vscode.window.activeTextEditor?.document.fileName;
            if (!openFile) {
                vscode.window.showErrorMessage("Failed to start the debugging: there is no `sources` attribute in the picked debug configuration and no active text editor.");
                return undefined;
            }

            let target = vscode.window.activeTextEditor?.document.languageId;
            if (target?.endsWith("-assembly")) {
                target = target.slice(0, target.length - 9);
            }

            if (!IDS.includes(target as TargetID)) {
                vscode.window.showErrorMessage("Failed to start the debugging: there is no `sources` attribute in the picked debug configuration, while the language of the opened file isn't a CdM family assembler.");
                return undefined;
            }

            debugConfig.target = target;
            debugConfig.sources = [openFile];
        }

        if (!debugConfig?.artifacts) {
            debugConfig.artifacts = {};
        }

        if (!debugConfig.artifacts?.image) {
            debugConfig.artifacts.image = pathlib.join(tempDirectory, "out.img");
        } else {
            if (!await mkdirparent(debugConfig.artifacts.image)) {
                return undefined;
            }
        }

        if (!debugConfig.artifacts?.debug) {
            debugConfig.artifacts.debug = pathlib.join(tempDirectory, "out.dbg");
        } else {
            if (!await mkdirparent(debugConfig.artifacts.debug)) {
                return undefined;
            }
        }

        debugConfig.address ??= "ws://localhost:7001";
        debugConfig.architecture ??= "harvard";
        debugConfig.tempDirectory = tempDirectory;

        return debugConfig;
    }
}
