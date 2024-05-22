import vscode from "vscode";

import { CdmDebugAdapterFactory } from "./factory";

export function installDebugAdapterFactories(context: vscode.ExtensionContext, temporaryDirectory: string) {
    context.subscriptions.push(
        vscode.debug.registerDebugAdapterDescriptorFactory("cdm", new CdmDebugAdapterFactory(temporaryDirectory)),
    );

    console.info("Installed the 'CdM Proccesors' debug adapter set");
}
