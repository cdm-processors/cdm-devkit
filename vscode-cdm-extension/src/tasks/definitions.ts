import * as vscode from "vscode";

import { TargetGeneralId, isTargetGeneralId } from "../protocol/targets";

export type CocasTaskDefinition = vscode.TaskDefinition & {
    type: "cocas";
    target: TargetGeneralId;
    sources: string[];
    artifacts: {
        image: string;
        debug?: string;
    };
};

export function isCocasTaskDefinition(
    definition: vscode.TaskDefinition,
): definition is CocasTaskDefinition {
    return definition.type === "cocas" &&
        isTargetGeneralId(definition.target) &&
        Array.isArray(definition.sources) &&
        definition.sources.every((value) => typeof value === "string") &&
        typeof definition.artifacts === "object" &&
        typeof definition.artifacts.image === "string" &&
        (typeof definition.artifacts.debug === "string" || typeof definition.artifacts.debug === "undefined");
}
