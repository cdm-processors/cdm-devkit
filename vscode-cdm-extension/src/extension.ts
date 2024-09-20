import vscode from "vscode";

import { installCommands } from "./commands";
import { installDebugAdapterFactories } from "./debug";
import { installTaskProviders } from "./tasks";
import { tmpdir } from "./stdlib";

export async function activate(context: vscode.ExtensionContext) {
	let temporaryDirectory;
	try {
		temporaryDirectory = await tmpdir(context.extension.id);
	} catch (error) {
		return vscode.window.showErrorMessage(`Failed to create a directory for temporary files. ${error}`);
	}

	context.subscriptions.push(temporaryDirectory);

	installCommands(context);
	installDebugAdapterFactories(context, temporaryDirectory.path);
	installTaskProviders(context);

	console.info("'CdM Processors' extension successfully started");
}

export function deactivate() {}
