import * as vscode from 'vscode';

import { CdmDebugRuntime } from '.';
import { sleep } from '../../stdlib';

export class EmulatorDebugRuntime extends CdmDebugRuntime {
    private terminal!: vscode.Terminal;

    public constructor(address: string) {
        super(address);
    }

    public async start() {
        const emulatorConfiguration = vscode.workspace.getConfiguration("cdm.emulator");
        
        const cocoemuExecutable = emulatorConfiguration.get("path") as string;
        this.startEmulator(cocoemuExecutable);

        // Wait for emulator to start
        // TODO: rewrite
        const emulatorConnectionDelay = emulatorConfiguration.get("delay") as number;
        await sleep(emulatorConnectionDelay);

        await super.start();
    }

    private startEmulator(emulatorPath: string): void {
        console.log(`Starting emulator at path: ${emulatorPath}`);

        this.terminal = vscode.window.createTerminal('Emulator Terminal');
        this.terminal.sendText(emulatorPath);
    }

    public shutdown(): this {
        super.shutdown();
        
        console.log(`Shutting down the emulator.`);
        if (this.terminal) {
            this.terminal.dispose();
        } else {
            console.warn(`No terminal found to shut down.`);
        }

        return this;
    }
}
