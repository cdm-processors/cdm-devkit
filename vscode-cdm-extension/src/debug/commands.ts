import * as vscode from "vscode";

export function showMemory() {
    vscode.debug.activeDebugSession?.customRequest("createMemoryView");
}

export function previousMemoryView(uri: vscode.Uri) {
    vscode.debug.activeDebugSession?.customRequest("previousMemoryView", { path: uri.path });
}

export function nextMemoryView(uri: vscode.Uri) {
    vscode.debug.activeDebugSession?.customRequest("nextMemoryView", { path: uri.path });
}

export async function setViewOffset(uri: vscode.Uri) {
    const offset = await vscode.window.showInputBox({
        title: "Set a new Memory View Offset",
        placeHolder: "a non-negative offset number",
        validateInput: (raw) => {
            let cand;
            try {
                cand = parseInt(raw);
            } catch {
                return `${raw} cannot be parsed as a number`;
            }

            if (cand < 0) {
                return "A view offset should be a non-negative number";
            }
        }
    });

    if (offset) {
        vscode.debug.activeDebugSession?.customRequest("setViewOffset", { path: uri.path, offset: parseInt(offset) });
    }
}

export async function setViewRange(uri: vscode.Uri) {
    const range = await vscode.window.showInputBox({
        title: "Set a new Memory View Range",
        placeHolder: "a positive range number",
        validateInput: (raw) => {
            let cand;
            try {
                cand = parseInt(raw);
            } catch {
                return `${raw} cannot be parsed as a number`;
            }

            if (cand <= 0) {
                return "A view range should be a positive number";
            }
        }
    });

    if (range) {
        vscode.debug.activeDebugSession?.customRequest("setViewRange", { path: uri.path, range: parseInt(range) });
    }
}

export async function setViewPage(uri: vscode.Uri) {
    const page = await vscode.window.showInputBox({
        title: "Set a new Memory View Page",
        placeHolder: "a non-negative page number",
        validateInput: (raw) => {
            let cand;
            try {
                cand = parseInt(raw);
            } catch {
                return `${raw} cannot be parsed as a number`;
            }

            if (cand <= 0) {
                return "A view page should be a non-negative number";
            }
        }
    });

    if (page) {
        vscode.debug.activeDebugSession?.customRequest("setViewPage", { path: uri.path, page: parseInt(page) });
    }
}
