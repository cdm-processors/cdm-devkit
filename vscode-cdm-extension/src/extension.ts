import * as vscode from "vscode";

import { CdmConfigurationProvider } from "./debug/configurations";
import { CdmDebugAdapterFactory } from "./debug/factory";
import { CdmRegistersProvider } from "./views/registers";
import { pickArch, pickTarget } from "./debug/commands";

export function activate(context: vscode.ExtensionContext) {
	let registersProvider = new CdmRegistersProvider();

	context.subscriptions.push(vscode.window.createTreeView("cdm.debug.registers", { treeDataProvider: registersProvider }));
	context.subscriptions.push(vscode.debug.registerDebugAdapterDescriptorFactory("cdm", new CdmDebugAdapterFactory(registersProvider)));
	context.subscriptions.push(vscode.debug.registerDebugConfigurationProvider("cdm", new CdmConfigurationProvider()));

	context.subscriptions.push(vscode.commands.registerCommand("cdm.debug.pickTarget", pickTarget));
	context.subscriptions.push(vscode.commands.registerCommand("cdm.debug.pickArch", pickArch));
	context.subscriptions.push(vscode.commands.registerCommand("cdm.debug.writeTarget", () => {
		console.log("Hello, World!");
	}));

	console.log("'CdM Processors' extension successfully started");
}

export function deactivate() {}
