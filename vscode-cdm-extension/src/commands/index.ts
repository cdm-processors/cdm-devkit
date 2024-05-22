import vscode from "vscode";

import { bootstrapEnvironment } from "./bootstrap";

const openMemoryView = () => vscode.debug.activeDebugSession?.customRequest("openMemoryView");
const setViewOffset = () => vscode.commands.executeCommand("hexEditor.goToOffset");

export function installCommands(context: vscode.ExtensionContext) {
    context.subscriptions.push(
        vscode.commands.registerCommand("cdm.debug.openMemoryView", openMemoryView),
		vscode.commands.registerCommand("cdm.debug.setViewOffset", setViewOffset),
        vscode.commands.registerCommand("cdm.environment.bootstrap", async () => await bootstrapEnvironment(context)),
    );

    console.info("Installed the 'CdM Proccesors' command set");
}
