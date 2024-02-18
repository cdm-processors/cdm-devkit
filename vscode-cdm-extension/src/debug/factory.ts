import * as vscode from "vscode";

import { CdmDebugSession } from "./session";

export class CdmDebugAdapterFactory implements vscode.DebugAdapterDescriptorFactory {
    public createDebugAdapterDescriptor(): vscode.ProviderResult<vscode.DebugAdapterDescriptor> {
        return new vscode.DebugAdapterInlineImplementation(new CdmDebugSession());
    }
}
