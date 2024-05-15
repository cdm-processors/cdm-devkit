export const DEFINED = [
    { name: "Harvard (separate storages)",  id: "harvard"       },
    { name: "Von Neumann (shared storage)", id: "vonNeumann"    },
] as const;

export const IDS = DEFINED.map(arch => arch.id);
export const NAMES = DEFINED.map(arch => arch.name);

export type ArchitectureId = typeof DEFINED[number]["id"];
export type ArchitectureName = typeof DEFINED[number]["name"];

export function idByName(name: string): ArchitectureId | undefined {
    return DEFINED.find(arch => arch.name === name)?.id;
}

export function nameById(id: string): ArchitectureName | undefined {
    return DEFINED.find(arch => arch.id === id)?.name;
}
