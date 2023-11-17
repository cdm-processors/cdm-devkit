import {
    CancellationToken,
    DebugConfiguration,
    DebugConfigurationProvider,
    ProviderResult,
    WorkspaceFolder,
    window,
} from "vscode";

import { languages, targets, targetNames } from "../adapterServerProtocol";

export class CdmConfigurationProvider implements DebugConfigurationProvider {
    resolveDebugConfiguration(folder: WorkspaceFolder | undefined, debugConfiguration: DebugConfiguration, token?: CancellationToken | undefined): ProviderResult<DebugConfiguration> {
        if (!debugConfiguration.type && !debugConfiguration.request && !debugConfiguration.name) {
            const editor = window.activeTextEditor;
            if (editor === undefined) {
                return window.showInformationMessage("Cannot find a program to debug").then(_ => {
                    return undefined;
                });
            }

            let index = languages.indexOf(editor.document.languageId);
            if (index !== -1) {
                debugConfiguration.type = "cdm";
				debugConfiguration.name = `Debug ${targetNames[index]} with Logisim`;
				debugConfiguration.request = "launch";
                debugConfiguration.serverAddress = "ws://localhost:7001";
                debugConfiguration.target = targets[index];
                debugConfiguration.program = "${file}";
            }
        }

        return debugConfiguration;
    }
}
