import * as pathlib from "path";

import * as vscode from "vscode";

export class CdmConfigurationProvider implements vscode.DebugConfigurationProvider {
    resolveDebugConfiguration(
        folder: vscode.WorkspaceFolder | undefined,
        debugConfig: vscode.DebugConfiguration,
        token?: vscode.CancellationToken | undefined
    ): vscode.ProviderResult<vscode.DebugConfiguration> {
        if (debugConfig.type !== "cdm" || debugConfig.request !== "launch") {
            return debugConfig;
        }

        let filename = vscode.window.activeTextEditor?.document?.fileName;
        // if (filename?.) {
        //     vscode.window.showErrorMessage("There either no active text editor or opened file is not a assembly file, so debugging can't be started.")
        //     return undefined;
        // }

        debugConfig.address ??= "ws://localhost:7001";
        debugConfig.architecture ??= "harvard";

        return debugConfig;
    }
}
