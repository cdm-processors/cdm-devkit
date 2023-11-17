import { ExtensionContext, debug } from "vscode";

import { CdmConfigurationProvider } from "./adapter/configurations";
import { CdmDebugAdapterFactory } from "./adapter/factory";

export function activate(context: ExtensionContext) {
	console.log("'CdM Processors' extension successfully started");
	context.subscriptions.push(debug.registerDebugConfigurationProvider("cdm", new CdmConfigurationProvider()));
	context.subscriptions.push(debug.registerDebugAdapterDescriptorFactory("cdm", new CdmDebugAdapterFactory()));
}

export function deactivate() {}
