import fsPromises from "fs/promises";
import pathlib from "path";

import vscode from "vscode";

import { ARCHITECTURE_ITEMS, SOURCE_ITEMS, TARGET_ITEMS } from "./picks";
import { TargetGeneralId, getTargetByGeneralId } from "../../protocol/targets";
import { getArchitectureById } from "../../protocol/architectures";

async function createTemplate(context: vscode.ExtensionContext, targetId: TargetGeneralId): Promise<string> {
    const template = context.asAbsolutePath(pathlib.join("resources", `${targetId}-template.asm`));
    const folder = vscode.workspace.workspaceFolders![0];

    const generated = pathlib.join(folder.uri.fsPath, "main.asm");
    await fsPromises.copyFile(template, generated);

    return generated;
}

export async function bootstrapEnvironment(context: vscode.ExtensionContext) {
    const target = await vscode.window.showQuickPick(TARGET_ITEMS, { title: "Pick a target processor" });
    if (target === undefined) {
        return vscode.window.showInformationMessage("Stopping the bootstrap process, because a target processor wasn't picked.");
    }

    const architecture = await vscode.window.showQuickPick(ARCHITECTURE_ITEMS, { title: "Pick a memory architecture" });
    if (architecture === undefined) {
        return vscode.window.showInformationMessage("Stopping the bootstrap process, because a memory architecture wasn't picked.");
    }

    const discoveryStrategy = await vscode.window.showQuickPick(SOURCE_ITEMS, { title: "Pick a source discovery strategy" });
    if (discoveryStrategy?.id === undefined) {
        return vscode.window.showInformationMessage("Stopping the bootstrap process, because a source discovery strategy wasn't picked.");
    }

    const workspace = vscode.workspace.workspaceFolders![0];

    const launch = vscode.workspace.getConfiguration("launch", workspace.uri);
    const launchConfigurations = (launch.get("configurations") ?? []) as any[];
    launchConfigurations.push({
        name: `Debug ${getTargetByGeneralId(target.id)!.name} with ${getArchitectureById(architecture.id)!.name} architecture`,
        type: "cdm",
        request: "launch",
        address: "ws://localhost:7001",
        target: target.id,
        architecture: architecture.id,
        artifacts: {
            image: "${workspaceFolder}${/}build${/}out.img",
            debug: "${workspaceFolder}${/}build${/}out.dbg.json",
        },
        preLaunchTask: `Compile ${getTargetByGeneralId(target.id)!.name}`
    });
    launch.update("configurations", launchConfigurations, false);

    let sourceSet: string[];
    switch (discoveryStrategy.id) {
        case "template": {
            sourceSet = [await createTemplate(context, target.id)];
            break;
        }
        case "scan": {
            sourceSet = [];
            break;
        }
        case "nothing": {
            sourceSet = [];
            break;
        }
    }

    const tasks = vscode.workspace.getConfiguration("tasks", workspace.uri);
    const tasksConfigurations = (tasks.get("tasks") ?? []) as any[];
    tasksConfigurations.push({
        label: `Compile ${getTargetByGeneralId(target.id)!.name}`,
        type: "cocas",
        target: target.id,
        sources: sourceSet,
        artifacts: {
            image: "${workspaceFolder}${/}build${/}out.img",
            debug: "${workspaceFolder}${/}build${/}out.dbg.json",
        },
    });
    tasks.update("tasks", tasksConfigurations, false);
}
