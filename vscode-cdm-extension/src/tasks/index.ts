import vscode from "vscode";

import { CocasTaskProvider } from "./providers";

export function installTaskProviders(context: vscode.ExtensionContext) {
    context.subscriptions.push(
        vscode.tasks.registerTaskProvider("cocas", new CocasTaskProvider()),
    );

    console.info("Installed the 'CdM Proccesors' task provider set");
}
