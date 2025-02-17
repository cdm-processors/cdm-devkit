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

export type Address = {
	protocol: string,
	host: string,
	port: number,
}

export function parseAddress(address: string): Address | undefined {
	const stringParts = address.split(":");

	if (stringParts.length != 3) {
		return undefined;
	}

	const port = Number(stringParts[2]);

	if (Number.isNaN(port)) {
		return undefined;
	}

	return {
		protocol: stringParts[0],
		host: stringParts[1],
		port: port,
	};
}
