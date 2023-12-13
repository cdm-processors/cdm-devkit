import * as vscode from "vscode";

export class ServerAddress extends vscode.TreeItem {
}

export class Target extends vscode.TreeItem {

}

export class Architecture extends vscode.TreeItem {

}

type SettingsValue = ServerAddress | Target | Architecture;

export class CdmSettingsProvider implements vscode.TreeDataProvider<SettingsValue> {
    constructor() {
    }

    onDidChangeTreeData?: vscode.Event<void | SettingsValue | null | undefined> | undefined;
    getTreeItem(element: SettingsValue): vscode.TreeItem | Thenable<vscode.TreeItem> {
        throw new Error("Method not implemented.");
    }
    getChildren(element?: SettingsValue | undefined): vscode.ProviderResult<SettingsValue[]> {
        throw new Error("Method not implemented.");
    }
    getParent?(element: SettingsValue): vscode.ProviderResult<SettingsValue> {
        throw new Error("Method not implemented.");
    }
    resolveTreeItem?(item: vscode.TreeItem, element: SettingsValue, token: vscode.CancellationToken): vscode.ProviderResult<vscode.TreeItem> {
        throw new Error("Method not implemented.");
    }
}
