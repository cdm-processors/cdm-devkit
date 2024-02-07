import * as vscode from "vscode";

import { CdmConfigurationProvider } from "./debug/configurations";
import { CdmDebugAdapterFactory } from "./debug/factory";

export function activate(context: vscode.ExtensionContext) {
	context.subscriptions.push(vscode.debug.registerDebugAdapterDescriptorFactory("cdm", new CdmDebugAdapterFactory()));
	context.subscriptions.push(vscode.debug.registerDebugConfigurationProvider("cdm", new CdmConfigurationProvider()));

	console.log("'CdM Processors' extension successfully started");
}

export function deactivate() {}
