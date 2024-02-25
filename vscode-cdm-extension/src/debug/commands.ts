import * as vscode from "vscode";

export function showMemory() {
    vscode.debug.activeDebugSession?.customRequest("createMemoryView");
}

export async function setViewOffset() {
    vscode.commands.executeCommand("hexEditor.goToOffset");
}
