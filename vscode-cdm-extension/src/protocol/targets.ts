const DEFINED = [
    { name: "CdM-8",    generalId: "cdm8",  extensionId: "cdm8-assembly"  },
    { name: "CdM-8e",   generalId: "cdm8e", extensionId: "cdm8e-assembly" },
    { name: "CdM-16",   generalId: "cdm16", extensionId: "cdm16-assembly" },
] as const;

const NAMES = DEFINED.map(target => target.name);
const GENERAL_IDS = DEFINED.map(target => target.generalId);
const EXTENSION_IDS = DEFINED.map(target => target.extensionId);

export type Target = typeof DEFINED[number];
export type TargetName = Target["name"];
export type TargetGeneralId = Target["generalId"];
export type TargetExtensionId = Target["extensionId"];


export function isTargetName(name?: string): name is TargetName {
    return NAMES.includes(name as any);
}

export function isTargetGeneralId(generalId?: string): generalId is TargetGeneralId {
    return GENERAL_IDS.includes(generalId as any);
}

export function isTargetExtensionId(extensionId?: string): extensionId is TargetExtensionId {
    return EXTENSION_IDS.includes(extensionId as any);
}


export function getTargetByName(name?: string): Target | undefined {
    return DEFINED.find(target => target.name === name);
}

export function getTargetByGeneralId(generalId?: string): Target | undefined {
    return DEFINED.find(target => target.generalId === generalId);
}

export function getTargetByExtensionId(extensionId?: string): Target | undefined {
    return DEFINED.find(target => target.extensionId === extensionId);
}
