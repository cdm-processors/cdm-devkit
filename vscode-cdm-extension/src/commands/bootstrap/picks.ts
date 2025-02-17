import vscode from "vscode";

import { DEFINED as ARCHITECTURES, ArchitectureId } from "../../protocol/architectures";
import { DEFINED as TARGETS, TargetGeneralId } from "../../protocol/targets";
import { DEFINED as ENVIRONMENTS, EnvironmentId } from "../../debug/runtime/environment";

type IdQuickPickItem<T> = vscode.QuickPickItem & { id: T };

export const TARGET_ITEMS: IdQuickPickItem<TargetGeneralId>[] = TARGETS.map((target) => {
    return {
        label: target.name,
        description: target.description,
        id: target.generalId,
    };
});

export const ARCHITECTURE_ITEMS: IdQuickPickItem<ArchitectureId>[] = ARCHITECTURES.map((architecture) => {
    return {
        label: architecture.name,
        description: architecture.description,
        id: architecture.id,
    };
});

export const SOURCE_ITEMS = [
    {
        label: "Create a template file",
        description: "add an assembly file with the default code for the picked target",
        id: "template",
    },
    {
        label: "Add all assembly files",
        description: "iterate over all files in project and add the assembly ones",
        id: "scan",
    },
    {
        label: "Don't do anything",
        description: "you will need to add sources yourselves",
        id: "nothing",
    },
] as const;

export const ENVIRONMENT_ITEMS: IdQuickPickItem<EnvironmentId>[] = ENVIRONMENTS.map((environment) => {
    return {
        label: environment.name,
        description: environment.description,
        id: environment.id,
    };
});
