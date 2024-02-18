import * as vscode from "vscode";

export function showMemory() {
    vscode.debug.activeDebugSession?.customRequest("createMemoryView");
}

export async function setViewOffset(uri: vscode.Uri) {
    vscode.commands.executeCommand("hexEditor.goToOffset");
}
