// emulator state
interface ICdmState {
    registers: Record<string, number>;
    memory: number[];
}

// requests to emulator
type CdmRequest = CdmStepRequest | CdmSetBreakpointsRequest | CdmPauseRequest | CdmContinueRequest | CdmSetLineLocationsRequest | CdmPathRequest | CdmInitRequest;
interface CdmStepRequest {
    action: 'step';
}

interface CdmSetBreakpointsRequest{
    action: 'breakpoints'
    data: number[];
}

interface CdmSetLineLocationsRequest{
    action: 'line_locations'
    data: number[];
}

interface CdmPauseRequest{
    action: 'pause',
}

interface CdmContinueRequest{
    action: 'continue',
}

interface CdmPathRequest {
    'action': 'reset',
    'path': string
}
interface CdmInitRequest{
    action: 'init',
    registers: string[],
    target: string
}

// events from emulator
type CdmEvent = CdmStateEvent | CdmStopEvent | CdmErrorEvent;
interface CdmStopEvent {
    action: 'stop'
    reason: string
}

interface CdmStateEvent {
    action: 'state';
    data: ICdmState;
}

interface CdmErrorEvent {
    action: 'error'
    data: string
}