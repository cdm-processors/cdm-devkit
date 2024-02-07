const DEFINED = [
    { name: "CdM-8",    id: "cdm8"  },
    { name: "CdM-8e",   id: "cdm8e" },
    { name: "CdM-16",   id: "cdm16" },
] as const;

export const IDS = DEFINED.map(target => target.id);
export const NAMES = DEFINED.map(target => target.name);

export type TargetID = typeof DEFINED[number]["id"];
export type TargetName = typeof DEFINED[number]["name"];

export function idByName(name: string): TargetID | undefined {
    return DEFINED.find(target => target.name === name)?.id;
}

export function nameByID(id: string): TargetName | undefined {
    return DEFINED.find(target => target.id === id)?.name;
}
