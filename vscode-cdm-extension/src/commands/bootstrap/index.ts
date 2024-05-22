import vscode from "vscode";

import { updateLaunchConfigurations, updateTasksConfiguration } from "./configurations";
import { ARCHITECTURE_ITEMS, SOURCE_ITEMS, TARGET_ITEMS } from "./picks";
import { createTemplate, retrieveAssemblyFiles } from "./sources";

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

    const sourceSet = 
        discoveryStrategy.id === "template" ? await createTemplate(context, target.id) :
        discoveryStrategy.id === "scan" ? await retrieveAssemblyFiles() : [];

    updateLaunchConfigurations(target.id, architecture.id);
    await updateTasksConfiguration(target.id, sourceSet);
}
