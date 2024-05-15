import * as vscode from "vscode";
import { isCocasTaskDefinition } from "./definitions";

export class CocasTaskProvider implements vscode.TaskProvider<vscode.Task> {
    public provideTasks(
        _token: vscode.CancellationToken,
    ): vscode.ProviderResult<vscode.Task[]> {
        return [];
    }

    public async resolveTask(
        task: vscode.Task,
        _token: vscode.CancellationToken,
    ): Promise<vscode.Task | undefined> {
        const definition = task.definition;
        if (!isCocasTaskDefinition(definition)) {
            return undefined;
        }

        const args = [
            "--target", definition.target,
            "--output", definition.artifacts.image,
        ];
        if (definition.artifacts.debug) {
            args.push("--debug", definition.artifacts.debug);
        }
        args.push(...definition.sources);

        const path = vscode.workspace.getConfiguration("cdm.path");
        const shellExecution = new vscode.ShellExecution(path.get("assembler") as string, args);

        return new vscode.Task(
            definition,
            task.scope ?? vscode.TaskScope.Workspace,
            task.name,
            definition.type,
            shellExecution,
        );
    }
}
