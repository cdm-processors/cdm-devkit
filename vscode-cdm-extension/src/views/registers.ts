import * as vscode from "vscode";

export class RegisterValue extends vscode.TreeItem {

}


export class CdmRegistersProvider implements vscode.TreeDataProvider<Register> {
    private emitter: vscode.EventEmitter<Register> = new vscode.EventEmitter();

    onDidChangeTreeData = this.emitter.event;

    getChildren(element?: Register): vscode.ProviderResult<Register[]> {
        if (element === undefined) {
            return [
                new Register("RC", 0),
                new Register("SP", 0),
                new Register("r0", 0),
            ];
        }

        return null;
    }

    getParent?(element: Register): vscode.ProviderResult<Register> {
        return null;
    }

    resolveTreeItem?(item: vscode.TreeItem, element: Register, token: vscode.CancellationToken): vscode.ProviderResult<vscode.TreeItem> {
        throw new Error("Method not implemented.");
    }

    getTreeItem(element: Register): vscode.TreeItem | Thenable<vscode.TreeItem> {
        return element;
    }
}

export class Register extends vscode.TreeItem {
    constructor(
        label: string,
        value: number,
    ) {
        super(`${label} = ${value}`);
    }
}
