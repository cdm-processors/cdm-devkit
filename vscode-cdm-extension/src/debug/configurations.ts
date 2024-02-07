import * as vscode from "vscode";

export class CdmConfigurationProvider implements vscode.DebugConfigurationProvider {
    resolveDebugConfiguration(
        folder: vscode.WorkspaceFolder | undefined,
        debugConfig: vscode.DebugConfiguration,
        token?: vscode.CancellationToken | undefined
    ): vscode.ProviderResult<vscode.DebugConfiguration> {
        if (debugConfig.type || debugConfig.request || debugConfig.name) {
            return debugConfig;
        }

        debugConfig.type = "cdm";
        debugConfig.request = "launch";
        debugConfig.artifacts = {
            image: "${fileDirname}/${fileBasenameNoExtension}.img",
            debug: "${fileDirname}/${fileBasenameNoExtension}.dbg"
        };

        return debugConfig;
    }
}
