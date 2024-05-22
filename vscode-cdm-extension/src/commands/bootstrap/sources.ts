import fsPromises from "fs/promises";
import pathlib from "path";

import vscode from "vscode";

import { TargetGeneralId } from "../../protocol/targets";

export async function createTemplate(context: vscode.ExtensionContext, targetId: TargetGeneralId): Promise<string[]> {
    const template = context.asAbsolutePath(pathlib.join("resources", `${targetId}-template.asm`));
    const folder = vscode.workspace.workspaceFolders![0];

    const generated = pathlib.join(folder.uri.fsPath, "main.asm");
    await fsPromises.copyFile(template, generated);

    return [generated];
}

export async function retrieveAssemblyFiles(): Promise<string[]> {
    const workspace = vscode.workspace.workspaceFolders![0];
    const files = [];

    for (const entry of await fsPromises.readdir(workspace.uri.fsPath, { recursive: true })) {
        const path = pathlib.join(workspace.uri.fsPath, entry);
        const stats = await fsPromises.stat(path);
        if (stats.isFile() && pathlib.extname(path) === ".asm") {
            files.push(path);
        }
    }

    return files;
}