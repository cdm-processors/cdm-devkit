import { CdmDebugRuntime } from ".";
import { EmulatorDebugRuntime } from "./emulator";
import { ExternalDebugRuntime } from "./external";

export const DEFINED = [
    {
        name: "External",
        id: "external",
        description: "run in external environment (e.g. Logisim)",
        create: (address: string) => new ExternalDebugRuntime(address)
    },
    {
        name: "Emulator",
        id: "emulator",
        description: "run in integrated emulator",
        create: (address: string) => new EmulatorDebugRuntime(address)
    }
] as const;

export const NAMES = DEFINED.map(env => env.name);
export const IDS = DEFINED.map(env => env.id);

export type Environment = typeof DEFINED[number];
export type EnvironmentName = Environment["name"];
export type EnvironmentId = Environment["id"];


export function isEnvironmentName(name?: string): name is EnvironmentName {
    return NAMES.includes(name as any);
}

export function isEnvironmentId(id?: string): id is EnvironmentId {
    return NAMES.includes(id as any);
}


export function getEnvironmentByName(name?: string): Environment | undefined {
    return DEFINED.find(env => env.name === name);
}

export function getEnvironmentById(id?: string): Environment | undefined {
    return DEFINED.find(env => env.id === id);
}

export function createDebugRuntime(id: string, address: string): CdmDebugRuntime | undefined {
    return getEnvironmentById(id)?.create(address);
}
