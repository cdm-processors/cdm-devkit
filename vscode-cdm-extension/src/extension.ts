import * as vscode from "vscode";

import { CdmConfigurationProvider } from "./debug/configurations";
import { CdmDebugAdapterFactory } from "./debug/factory";
import { nextMemoryView, previousMemoryView, setViewOffset, setViewPage, setViewRange, showMemory } from "./debug/commands";

export async function activate(context: vscode.ExtensionContext) {
	context.subscriptions.push(
		vscode.commands.registerCommand("cdm.debug.showMemory", showMemory),
		vscode.commands.registerCommand("cdm.debug.previousView", previousMemoryView),
		vscode.commands.registerCommand("cdm.debug.nextView", nextMemoryView),
		vscode.commands.registerCommand("cdm.debug.setViewOffset", setViewOffset),
		vscode.commands.registerCommand("cdm.debug.setViewRange", setViewRange),
		vscode.commands.registerCommand("cdm.debug.setViewPage", setViewPage),
	);

	context.subscriptions.push(
		vscode.debug.registerDebugAdapterDescriptorFactory("cdm", new CdmDebugAdapterFactory()),
		vscode.debug.registerDebugConfigurationProvider("cdm", new CdmConfigurationProvider()),
	);

	console.log("'CdM Processors' extension successfully started");
}

export function deactivate() {}
