import * as vscode from "vscode";

import { CdmConfigurationProvider } from "./debug/configurations";
import { CdmDebugAdapterFactory } from "./debug/factory";
import { showMemory, setViewOffset } from "./debug/commands";

export async function activate(context: vscode.ExtensionContext) {
	context.subscriptions.push(
		vscode.commands.registerCommand("cdm.debug.showMemory", showMemory),
		vscode.commands.registerCommand("cdm.debug.setViewOffset", setViewOffset),
	);

	context.subscriptions.push(
		vscode.debug.registerDebugAdapterDescriptorFactory("cdm", new CdmDebugAdapterFactory()),
		vscode.debug.registerDebugConfigurationProvider("cdm", new CdmConfigurationProvider()),
	);

	console.log("'CdM Processors' extension successfully started");
}

export function deactivate() {}
