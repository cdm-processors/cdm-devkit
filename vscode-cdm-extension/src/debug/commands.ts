import * as vscode from "vscode";

import * as targets from "../protocol/targets";

const ARCH_REPR = ["Von Neumann (shared storage)", "Harvard (separate storages)"];

export async function pickTarget(): Promise<string | undefined> {
    let target = await vscode.window.showQuickPick(targets.NAMES, {
        title: "Pick the target processor",
        canPickMany: false,
        placeHolder: "supported-CdM-family-processor"
    });

    if (target) {
        target = targets.idByName(target);
    }

    return target;
}

export async function pickArch(): Promise<string | undefined> {
    let arch = await vscode.window.showQuickPick(ARCH_REPR, {
        title: "Pick the memory architecture",
        canPickMany: false,
        placeHolder: "shared or separate"
    });

    if (arch) {
        arch = ["vonNeumann", "harvard"][ARCH_REPR.indexOf(arch)];
    }

    return arch;
}
