import {
    Logger,
    logger,
    LoggingDebugSession,
    DebugSession,
    InitializedEvent,
    TerminatedEvent,
    StoppedEvent,
    BreakpointEvent,
    OutputEvent,
    ProgressStartEvent,
    ProgressUpdateEvent,
    ProgressEndEvent,
    InvalidatedEvent,
    Thread,
    StackFrame,
    Scope,
    Source,
    Handles,
    Breakpoint,
    MemoryEvent,
    Variable,
    Response,
    Event,
    
} from '@vscode/debugadapter';
import { DebugProtocol } from '@vscode/debugprotocol';
import { ChildProcess, exec, spawn } from 'child_process';
import * as fs from 'fs';
import * as path from 'path';
import * as vscode from 'vscode';
import internal = require('stream');
import WebSocket = require('ws');
import { createResolvable } from '../util';
import {CodeMap, CodeLocation, parseCodeMap} from './codeMap';


interface ILaunchRequestArguments extends DebugProtocol.LaunchRequestArguments {
    program: string[];
    runner: 'emulator' | 'runner'
    target: string
    registersSet: string[]
}


const registersVariableReference = 1;
const memoryVariableReference = 2;
const dataMemVariableReference = 3;

export class CdmDebugSession extends DebugSession {
    emulatorProcess!: ChildProcess;
    socket: WebSocket | null = null;
    codeMap: CodeMap = new Map();
    latestState: ICdmState | null = null;
    launched = createResolvable<void>();
    breakpointsPerFile = new Map<string, number[]>();
    static threadID = 1;
    memoryViewPath: string | undefined;
    public constructor() {
        super();

        this.setDebuggerColumnsStartAt1(true);
        this.setDebuggerLinesStartAt1(true);
    }

    protected initializeRequest(response: DebugProtocol.InitializeResponse, args: DebugProtocol.InitializeRequestArguments): void {
        response.body = response.body || {};
        console.log("initializeRequest");
        this.sendResponse(response);
        this.sendEvent(new InitializedEvent());
    }

    protected async launchRequest(response: DebugProtocol.LaunchResponse, args: ILaunchRequestArguments) {

        console.log(`launched, program = ${args.program}, runner = ${args.runner}`);
        const noExtensionPath = args.program[0].replace(new RegExp(`${path.extname(args.program[0])}$`), '');
        const imgPath = noExtensionPath + '.img';
        const codeMapPath = noExtensionPath + '.dbg.json';
        this.memoryViewPath = noExtensionPath + '.cdmmem';
        asyncWriteFile(this.memoryViewPath, [0].join('\n'));
        
        const assemblerProcess = spawn("cocas", ['-t', args.target , '--debug', codeMapPath, ...args.program, "-o", imgPath]);
        assemblerProcess.on('error', (e) => {
            this.sendEvent(new OutputEvent(`ERROR: ${e.name}: ${e.message}`, 'important'));
            this.sendEvent(new TerminatedEvent());
            return;
        });

        for await (const data of assemblerProcess.stdout) {
            this.sendEvent(new OutputEvent(data.toString(), 'debug console'));
        }
        for await(const data of assemblerProcess.stderr) {
            this.sendEvent(new OutputEvent('[ASM ERROR] ' + data.toString(), 'debug console'));
        }

        await new Promise<void>((resolve) => {
            assemblerProcess.on('exit', () => {
                resolve();
            });
        });
        if(assemblerProcess.exitCode !== 0){
            this.sendEvent(new OutputEvent('Assembler exited with non-zero code', 'important'));
            this.sendEvent(new TerminatedEvent());
            return;
        }

        let emuPort!: Number;

        if(args.runner === 'emulator'){
            // TODO: add emulator support
        }else{
            emuPort = 1337;
        }
        console.log(emuPort);

        // load debug info
        // TODO: check if we successfully loaded file
        const codeMapFile = await fs.promises.open(codeMapPath, 'r');
        const codeMapData = (await codeMapFile.readFile()).toString();
        codeMapFile.close();

        this.codeMap = parseCodeMap(codeMapData);

        //connect to emulator
        this.socket = new WebSocket(`ws://127.0.0.1:${emuPort}`);
        this.socket.onmessage = (event) => {
            this.onEmulatorMessage(JSON.parse(event.data.toString()));
        };
        this.socket.onopen = ()=>{this.launched.resolve();};
        this.sendResponse(response);
        this.sendEvent(new StoppedEvent('entry', 1));
        this.sendEmulatorMessage({action: "init", registers: args.registersSet, target: args.target});
        this.sendEmulatorMessage({action: "line_locations", data: Array.from(this.codeMap.keys())});
        if(args.runner === "runner"){
            this.sendEmulatorMessage({'action': 'reset', 'path': imgPath});
        }
        showMemoryView(this.memoryViewPath);
        console.log('done initialization');
    


    }

    private onEmulatorMessage(message: CdmEvent) {
        if (message.action === 'state') {
            // TODO: race condition: we need to wait for first state before finishing initialization
            this.latestState = message.data;
            //console.log(message.data);
            console.log(message);
            this.sendEvent(new Event('cdmState', this.latestState));
            if (this.codeMap.has(this.latestState.registers.pc)) {
                //console.log("current state");
                //console.log(message);
                //console.log(this.codeMap.get(this.latestState.registers.pc));
            }
            console.log('got state');
            
        }else if(message.action === 'stop'){
            console.log("stop_event, reason: "+message.reason);
            if (message.reason === 'halt'){
                this.sendEvent(new TerminatedEvent());
            }
            this.sendEvent(new StoppedEvent('stop', CdmDebugSession.threadID));
        }else if(message.action === 'error'){
            console.log('emu error');
            this.sendEvent(new OutputEvent(`Emulation error: ${message.data}`, 'important'));
            this.sendEvent(new TerminatedEvent());
        }
    }

    private async  sendEmulatorMessage(msg: CdmRequest) {
        await this.launched;
        console.log(`sending: ${JSON.stringify(msg)}`);
        this.socket?.send(JSON.stringify(msg));
    }

    protected async stepInRequest(response: DebugProtocol.StepInResponse, args: DebugProtocol.StepInArguments, request?: DebugProtocol.Request) {
        this.sendEmulatorMessage({ action: 'step' });
        this.sendResponse(response);
    }

    protected async stepOutRequest(response: DebugProtocol.StepOutResponse, args: DebugProtocol.StepOutArguments, request?: DebugProtocol.Request){
        this.sendEmulatorMessage({ action: 'step' });
        this.sendResponse(response);
    }

    protected async nextRequest(response: DebugProtocol.NextResponse, args: DebugProtocol.NextArguments, request?: DebugProtocol.Request){
        this.sendEmulatorMessage({ action: 'step' });
        this.sendResponse(response);
    }




    protected threadsRequest(response: DebugProtocol.ThreadsResponse): void {
        console.log('thread request');
        // runtime supports no threads so just return a default thread.
        response.body = {
            threads: [new Thread(CdmDebugSession.threadID, 'thread 1')],
        };
        this.sendResponse(response);
    }

    protected disconnectRequest(
        response: DebugProtocol.DisconnectResponse,
        args: DebugProtocol.DisconnectArguments,
        request?: DebugProtocol.Request
    ): void {
        closeMemoryView(this.memoryViewPath!);
        console.log('disconnect');
        this.socket?.close();
        this.sendResponse(response);
    }

    // Requests go like this:
    // stackTrace -> scopes -> variables
    protected variablesRequest(
        response: DebugProtocol.VariablesResponse,
        args: DebugProtocol.VariablesArguments,
        request?: DebugProtocol.Request
    ): void {
        if (this.latestState === null) {
            this.sendResponse(response);
            return;
        }
        
        const registersArray = Object.entries(this.latestState.registers);
        registersArray.sort((a,b) => a[0].localeCompare(b[0]));
        



        console.log('variable request');
        if (args.count === undefined || args.count === 0) {
            args.count = Infinity;
        }
        if (args.start === undefined) {
            args.start = 0;
        }
        response.body = { variables: [] };
        if (args.variablesReference === registersVariableReference) {
            for (const [name, value] of registersArray) {
                const valueString = value.toString().padStart(3, ' ') + "   0x" + value.toString(16).padStart(4, '0');
                response.body.variables.push(new Variable(name, valueString));
            }
        } else if (args.variablesReference === memoryVariableReference) {
            response.body.variables.push(new Variable('Data memory', '...', dataMemVariableReference));
        } else if (args.variablesReference === dataMemVariableReference) {
            for (let i = args.start; i < Math.min(this.latestState.memory.length, args.start + args.count); i++) {
                response.body.variables.push(new Variable(`[${i.toString(16)}]`, this.latestState.memory[i].toString()));
            }
        }
        asyncWriteFile(this.memoryViewPath!, this.latestState.memory.concat([this.latestState.registers.sp]).join('\n'));

        this.sendResponse(response);
    }

    protected stackTraceRequest(
        response: DebugProtocol.StackTraceResponse,
        args: DebugProtocol.StackTraceArguments,
        request?: DebugProtocol.Request
    ): void {
        // TODO: source reference
        console.log('stack request');
        response.body = { stackFrames: [] };
        if (this.latestState !== null && this.codeMap.has(this.latestState.registers.pc)) {
            const location = this.codeMap.get(this.latestState.registers.pc)!;

            const frame = new StackFrame(0, 'frame', new Source(path.parse(location.file).base, location.file), location.line);
            response.body.totalFrames = 1;
            response.body.stackFrames.push(frame);
        } else {
            response.body.totalFrames = 0;
            response.body.stackFrames = [];
        }
        this.sendResponse(response);
    }

    protected scopesRequest(response: DebugProtocol.ScopesResponse, args: DebugProtocol.ScopesArguments, request?: DebugProtocol.Request): void {
        // TODO: do no hardcode frameID
        if (args.frameId === 0) {
            const registersScope = new Scope('Registers', registersVariableReference);
            const memoryScope = new Scope('Memory', memoryVariableReference);
            response.body = { scopes: [registersScope, memoryScope] };
        }

        this.sendResponse(response);
    }


    protected async setBreakPointsRequest(response: DebugProtocol.SetBreakpointsResponse, args: DebugProtocol.SetBreakpointsArguments, request?: DebugProtocol.Request) {
        await this.launched;
        //console.log(args);
        let pcBreakpoints: number[] = [];
        response.body = {breakpoints: []};
        // TODO: ineficient breakpoint set: O(n*m), n = program_length, m = breakpoints amount
        for(const breakpoint of args.breakpoints || []){
            for(const [pc, location] of this.codeMap.entries()){
                // TODO: relative pathes
                if(vscode.Uri.file(location.file).fsPath === vscode.Uri.file(args.source.path as string).fsPath && location.line === breakpoint.line){
                    pcBreakpoints.push(pc);
                response.body.breakpoints.push(new Breakpoint(true));
                }
            }
        }
        this.breakpointsPerFile.set(args.source.path!, pcBreakpoints);
        

        this.sendEmulatorMessage({action: 'breakpoints', data: Array.from(this.breakpointsPerFile.values()).flat()});

        this.sendResponse(response);
    }

    protected continueRequest(response: DebugProtocol.ContinueResponse, args: DebugProtocol.ContinueArguments, request?: DebugProtocol.Request): void {
        response.body = {allThreadsContinued: true};
        this.sendEmulatorMessage({action:'continue'});
        this.sendResponse(response);
    }

    protected pauseRequest(response: DebugProtocol.PauseResponse, args: DebugProtocol.PauseArguments, request?: DebugProtocol.Request): void {
        this.sendEmulatorMessage({action:'pause'});
        this.sendResponse(response);
    }

    /**
     * Called at the end of the configuration sequence.
     * Indicates that all breakpoints etc. have been sent to the DA and that the 'launch' can start.
     */
    protected configurationDoneRequest(response: DebugProtocol.ConfigurationDoneResponse, args: DebugProtocol.ConfigurationDoneArguments): void {
        super.configurationDoneRequest(response, args);

        // notify the launchRequest that configuration has finished
        // this._configurationDone.notify();
        console.log('config done');
    }
}

async function asyncWriteFile(filename: string, data: any) {
    fs.writeFileSync(Buffer.from(filename), data, {flag: 'w',});
  }
async function showMemoryView(memoryViewPath: string) {
    const uri = vscode.Uri.file(memoryViewPath);
    const targetEditor = 'cdmDebug.cdmMem';
    await vscode.commands.executeCommand('vscode.openWith', uri, targetEditor, { viewColumn: vscode.ViewColumn.Beside});
}
function closeMemoryView(memoryViewPath: string){
    const visibleDocuments = vscode.workspace.textDocuments;
    //console.log(vscode.workspace.textDocuments.forEach((editor) => console.log(editor.fileName)));
    //console.log(visibleEditors);
    /*
    const memoryMapView = visibleDocuments.find((document) => path.extname(document.fileName) === ".cdmmem");
    const index = visibleDocuments.indexOf((document) => path.extname(document.fileName) === ".cdmmem");
    if (memoryMapView){
        vscode.window.showTextDocument(memoryMapView, {preserveFocus: true}).then(() => {
            vscode.commands.executeCommand('workbench.action.closeActiveEditor');
        });
    }*/
}