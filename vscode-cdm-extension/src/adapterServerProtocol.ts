export const targets = ["cdm8", "cdm8e", "cdm16", "generic"] as const;
export const targetNames = ["CdM-8", "CdM-8e", "CdM-16", "Generic CdM"];
export const languages = ["cdm8-assembly", "cdm8e-assembly", "cdm16-assembly"];
export type Target = typeof targets[number];

export const reasons = ["breakpoint", "line", "exception", "halt"] as const;
export type Reason = typeof reasons[number];

export const stopConditions = ["breakpoint", "exception", "line"] as const;
export type StopCondition = typeof stopConditions[number];

export const actions = [
    "init",
    "load",
    "setBreakpoints",
    "setLineLocations",
    "run",
    "reset",
    "pause",
    "getRegisters",
    "getMemory",
    "setMemory",
    "debugEvent",
] as const;
export type Action = typeof actions[number];

export interface DAPMessage {
    action: Action;
}

export interface DAPResponse extends DAPMessage {
    status: "OK" | "FAIL";
}

export interface InitializationMessage extends DAPMessage {
    action: "init";
    target: Target;
    memoryConfiguration: "vonNeumann" | "harvard";
}

export interface InitializationResponse extends DAPResponse {
    action: "init";
    supportsExceptions: Boolean;
    registers: Array<String>;
    ramSize: Number;
}

export interface LoadMessage extends DAPMessage {
    action: "load";
    source: "path" | "bytes";
}

export interface PathLoadMessage extends LoadMessage {
    source: "path";
    path: String;
}

export interface BytesLoadMessage extends LoadMessage {
    source: "bytes";
    bytes: Uint8Array;
}

export interface SetBreakpointsMessage extends DAPMessage {
    action: "setBreakpoints";
    breakpoints: Array<Number>;
}

export interface SetLineLocationsMessage extends DAPMessage {
    action: "setLineLocations"
    locations: Array<Number>;
}

export interface RunMessage extends DAPMessage {
    action: "run";
    stopConditions: Set<StopCondition>;
}

export interface RestartMessage extends DAPMessage {
    action: "reset";
}

export interface PauseMessage extends DAPMessage {
    action: "pause";
}

export interface GetRegistersMessage extends DAPMessage {
    action: "getRegisters";
}

export interface GetRegistersResponse extends DAPResponse {
    action: "getRegisters";
    registers: BigUint64Array;
}

export interface GetMemoryMessage extends DAPMessage {
    action: "getMemory";
    offset: Number;
    size: Number;
}

export interface SetMemoryMessage extends DAPMessage {
    action: "setMemory";
    offset: Number;
    value: Number; 
}

export interface GetMemoryResponse extends DAPResponse {
    action: "getMemory";
    bytes: Uint8Array;
}

export interface DebugEvent extends DAPResponse {
    action: "debugEvent";
    reason: Reason;
}
