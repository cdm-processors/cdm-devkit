import * as vscode from "vscode";

import { CdmDebugSession } from "./session";
import { CdmRegistersProvider } from "../views/registers";

export class CdmDebugAdapterFactory implements vscode.DebugAdapterDescriptorFactory {
    constructor(
        private readonly registers: CdmRegistersProvider
    ) {}

    createDebugAdapterDescriptor(session: vscode.DebugSession, executable: vscode.DebugAdapterExecutable | undefined): vscode.ProviderResult<vscode.DebugAdapterDescriptor> {
        return new vscode.DebugAdapterInlineImplementation(new CdmDebugSession(this.registers));
    }
}
