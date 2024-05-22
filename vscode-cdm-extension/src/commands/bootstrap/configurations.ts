import fsPromises from "fs/promises";
import pathlib from "path";

import vscode from "vscode";

import { ArchitectureId, getArchitectureById } from "../../protocol/architectures";
import { TargetGeneralId, getTargetByGeneralId } from "../../protocol/targets";

export function updateLaunchConfigurations(targetId: TargetGeneralId, architectureId: ArchitectureId) {
    const workspace = vscode.workspace.workspaceFolders![0];

    const target = getTargetByGeneralId(targetId)!;
    const architecture = getArchitectureById(architectureId)!;

    const launch = vscode.workspace.getConfiguration("launch", workspace.uri);
    const launchConfigurations: any[] = launch.get("configurations") ?? [];

    const configuration = {
        name: `Debug ${target.name} with ${getArchitectureById(architecture.id)!.name} architecture`,
        type: "cdm",
        request: "launch",
        address: "ws://localhost:7001",
        target: target.generalId,
        architecture: architecture.id,
        artifacts: {
            image: "${workspaceFolder}${/}build${/}out.img",
            debug: "${workspaceFolder}${/}build${/}out.dbg.json",
        },
        preLaunchTask: `Compile ${target.name}`,
    };

    launchConfigurations.push(configuration);
    launch.update("configurations", launchConfigurations, false);
}

export async function updateTasksConfiguration(targetId: TargetGeneralId, sourceSet: string[]) {
    const workspace = vscode.workspace.workspaceFolders![0];

    await fsPromises.mkdir(pathlib.join(workspace.uri.fsPath, "build"));

    const target = getTargetByGeneralId(targetId)!;

    const tasks = vscode.workspace.getConfiguration("tasks", workspace.uri);
    const tasksConfigurations: any[] = tasks.get("tasks") ?? [];

    const configuration = {
        label: `Compile ${target.name}`,
        type: "cocas",
        target: target.generalId,
        sources: sourceSet,
        artifacts: {
            image: "${workspaceFolder}${/}build${/}out.img",
            debug: "${workspaceFolder}${/}build${/}out.dbg.json",
        },
    };

    tasksConfigurations.push(configuration);
    tasks.update("tasks", tasksConfigurations, false);
}