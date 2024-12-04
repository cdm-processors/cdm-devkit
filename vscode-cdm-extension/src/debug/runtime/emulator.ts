import * as vscode from 'vscode';

import { CdmDebugRuntime } from './runtime';

export class EmulatorDebugRuntime extends CdmDebugRuntime {
    private terminal: vscode.Terminal | undefined;

    public constructor(address: string, emulatorPath: string) {
        super(address);
        this.startEmulator(emulatorPath);
    }

    private startEmulator(emulatorPath: string): void {
        console.log(`Starting emulator at path: ${emulatorPath}`);
        
        this.terminal = vscode.window.createTerminal('Emulator Terminal');
        this.terminal.sendText(emulatorPath);
        this.terminal.show();
    }

    public shutdown(): this {
        console.log(`Shutting down the emulator.`);
        
        if (this.ws) {
            this.ws.close();
            console.log(`WebSocket connection closed.`);
        } else {
            console.warn(`No WebSocket connection found to shut down.`);
        }

        if (this.terminal) {
            this.terminal.dispose();
            this.terminal = undefined; 
        } else {
            console.warn(`No terminal found to shut down.`);
        }

        return this;
    }
}
