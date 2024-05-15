import * as fs from "fs";
import * as fsPromises from "fs/promises";
import * as os from "os";
import * as pathlib from "path";
import * as vscode from "vscode";

import { showMemory, setViewOffset } from "./debug/commands";
import { CdmDebugAdapterFactory } from "./debug/factory";
import { CocasTaskProvider } from "./tasks/providers";

export async function activate(context: vscode.ExtensionContext) {
	const temporaryDirectory = pathlib.join(os.tmpdir(), context.extension.id);
	try {
		await fsPromises.mkdir(temporaryDirectory);
	} catch (error) {
		// @ts-ignore: ignore error, if the directory already exists
		if (error!.code !== "EEXIST") {
			const _ = vscode.window.showErrorMessage(`Failed to create a directory for temporary files. ${error}`);
			return;
		}	
	}

	const removeTemporaryDirectory = () => {
		fs.rm(temporaryDirectory, { recursive: true, force: true }, (error) => {
			const _ = vscode.window.showWarningMessage(`Failed to remove a temporary directory at ${temporaryDirectory}. ${error}`);
		});
	};

	context.subscriptions.push(
		{ dispose: removeTemporaryDirectory },

		vscode.commands.registerCommand("cdm.debug.showMemory", showMemory),
		vscode.commands.registerCommand("cdm.debug.setViewOffset", setViewOffset),

		vscode.debug.registerDebugAdapterDescriptorFactory("cdm", new CdmDebugAdapterFactory(temporaryDirectory)),

		vscode.tasks.registerTaskProvider("cocas", new CocasTaskProvider())
	);

	console.info("'CdM Processors' extension successfully started");
}

export function deactivate() {}
