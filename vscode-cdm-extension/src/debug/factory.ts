import * as vscode from "vscode";

import { CdmDebugSession } from "./session";

export class CdmDebugAdapterFactory implements vscode.DebugAdapterDescriptorFactory {
    private temporaryDirectory: string;

    public constructor(temporaryDirectory: string) {
        this.temporaryDirectory = temporaryDirectory;
    }

    public createDebugAdapterDescriptor(): vscode.ProviderResult<vscode.DebugAdapterDescriptor> {
        return new vscode.DebugAdapterInlineImplementation(new CdmDebugSession(this.temporaryDirectory));
    }
}
