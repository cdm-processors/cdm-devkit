export const DEFINED = [
    {
        name: "Harvard",
        id: "harvard",
        description: "separate storages"
    },
    {
        name: "Von Neumann",
        id: "vonNeumann",
        description: "shared storage"
    },
] as const;

export const NAMES = DEFINED.map(arch => arch.name);
export const IDS = DEFINED.map(arch => arch.id);

export type Architecture = typeof DEFINED[number];
export type ArchitectureName = Architecture["name"];
export type ArchitectureId = Architecture["id"];


export function isArchitectureName(name?: string): name is ArchitectureName {
    return NAMES.includes(name as any);
}

export function isArchitectureId(id?: string): id is ArchitectureId {
    return NAMES.includes(id as any);
}


export function getArchitectureByName(name?: string): Architecture | undefined {
    return DEFINED.find(arch => arch.name === name);
}

export function getArchitectureById(id?: string): Architecture | undefined {
    return DEFINED.find(arch => arch.id === id);
}
