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
        
        // Create a new terminal to run the emulator
        this.terminal = vscode.window.createTerminal('Emulator Terminal');
        this.terminal.sendText(emulatorPath);
        this.terminal.show();
    }

    public shutdown(): this {
        console.log(`Shutting down the emulator.`);
        
        if (this.terminal) {
            this.terminal.dispose();
            this.terminal = undefined; 
        } else {
            console.warn(`No terminal found to shut down.`);
        }

        this.ws.close();
        return this;
    }
}
