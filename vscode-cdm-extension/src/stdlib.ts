import fs from "fs";
import fsPromises from "fs/promises";
import os from "os";
import pathlib from "path";

import vscode from "vscode";

export function isErrnoException(obj: any): obj is NodeJS.ErrnoException {
    return obj instanceof Error;
}

export async function tmpdir(name: string): Promise<{ path: string, dispose: () => void }> {
	const temporaryDirectory = pathlib.join(os.tmpdir(), name);
	try {
		await fsPromises.mkdir(temporaryDirectory);
	} catch (error) {
		if (isErrnoException(error) && error?.code !== "EEXIST") {
			throw error;
		}
	}

	return {
		path: temporaryDirectory,
		dispose: () => {
			fs.rm(temporaryDirectory, { recursive: true, force: true }, (error) => {
				const _ = vscode.window.showWarningMessage(`Failed to remove a temporary directory at ${temporaryDirectory}. ${error}`);
			});
		},
	};
}

export async function sleep(ms: number) {
	await new Promise((r) => setTimeout(r, ms));
}
