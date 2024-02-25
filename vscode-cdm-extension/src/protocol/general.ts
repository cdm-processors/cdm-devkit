 import { ArchitectureID } from "./architectures";
import { TargetID } from "./targets";

export const INITIALIZE = "init";
export const LOAD_IMAGE = "load";
export const SET_BREAKPOINTS = "setBreakpoints";
export const SET_LINES = "setLineLocations";
export const RUN_EXECUTION = "run";
export const RESET_EXECUTION = "reset";
export const PAUSE_EXECUTION = "pause";
export const REQUEST_REGISTERS = "getRegisters";
export const REQUEST_MEMORY = "getMemory";
export const WRITE_MEMORY = "setMemory";
export const EXECUTION_STOPPED = "debugEvent";

export const MARKERS = [
    INITIALIZE,
    LOAD_IMAGE,
    SET_BREAKPOINTS,
    SET_LINES,
    RUN_EXECUTION,
    RESET_EXECUTION,
    PAUSE_EXECUTION,
    REQUEST_REGISTERS,
    REQUEST_MEMORY,
    WRITE_MEMORY,
    EXECUTION_STOPPED,
] as const;
export type Marker = typeof MARKERS[number];


export const EXCEPTION = "exception";
export const FETCH = "fetch";
export const STEP = "line";
export const BREAKPOINT = "breakpoint";
export const STOP = "halt";
export const PAUSE = "pause";
export const UNKNOWN = "unknown";

export const BREAK_CONDITIONS = [EXCEPTION, FETCH, STEP, BREAKPOINT] as const;
export type BreakCondition = typeof BREAK_CONDITIONS[number];
export const REASONS = [...BREAK_CONDITIONS, STOP, PAUSE, UNKNOWN] as const;
export type Reason = typeof REASONS[number];


export const SUCCESS = "OK";
export const FAILURE = "FAIL";


export const LOAD_FROM_PATH = "path";
export const LOAD_FROM_BYTESTREAM = "bytes";


export type Message = {
    action: Marker,
};

export type Response = Message & {
    status: typeof SUCCESS | typeof FAILURE,
};

export type InitializationMessage = Message & {
    action: typeof INITIALIZE,
    target: TargetID,
    memoryConfiguration: ArchitectureID,
};

export type InitializationResponse = Response & {
    action: typeof INITIALIZE,
    supportsExceptions: boolean,
    registerNames: string[],
    registerSizes: number[],
    ramSize: number,
};

export type LoadImageMessage = Message & {
    action: typeof LOAD_IMAGE,
    source: typeof LOAD_FROM_PATH | typeof LOAD_FROM_BYTESTREAM,
};

export type PathLoadMessage = LoadImageMessage & {
    source: typeof LOAD_FROM_PATH,
    path: string,
};

export type BytesLoadMessage = LoadImageMessage & {
    source: typeof LOAD_FROM_BYTESTREAM,
    bytes: number[],
};

export type SetBreakpointsMessage = Message & {
    action: typeof SET_BREAKPOINTS,
    breakpoints: number[],
};

export type SetLinesMessage = Message & {
    action: typeof SET_LINES,
    lineLocations: number[],
};

export type RunExecutionMessage = Message & {
    action: typeof RUN_EXECUTION,
    stopConditions: BreakCondition[],
};

export type ResetExecutionMessage = Message & {
    action: typeof RESET_EXECUTION,
};

export type PauseExecutionMessage = Message & {
    action: typeof PAUSE_EXECUTION,
};

export type RequestRegistersMessage = Message & {
    action: typeof REQUEST_REGISTERS,
};

export type RequestRegistersResponse = Response & {
    action: typeof REQUEST_REGISTERS,
    registers: number[],
};

export type RequestMemoryMessage = Message & {
    action: typeof REQUEST_MEMORY,
    offset: number,
    size: number,
};

export type RequestMemoryResponse = Response & {
    action: typeof REQUEST_MEMORY,
    bytes: number[],
};

export type WriteMemoryMessage = Message & {
    action: typeof WRITE_MEMORY,
    offset: number,
    value: number,
};

export type ExecutionStop = Response & {
    action: typeof EXECUTION_STOPPED,
    reason: Reason,
};
