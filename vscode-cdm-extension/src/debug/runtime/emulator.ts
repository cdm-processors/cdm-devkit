import * as vscode from 'vscode';

import { CdmDebugRuntime } from '.';
import { parseAddress, sleep } from '../../stdlib';

export class EmulatorDebugRuntime extends CdmDebugRuntime {
    private terminal!: vscode.Terminal;

    public constructor(address: string) {
        super(address);
    }

    public async start() {
        const emulatorConfiguration = vscode.workspace.getConfiguration("cdm.emulator");

        const cocoemuExecutable = emulatorConfiguration.get("path") as string;
        const { port } = parseAddress(this.address)!;

        this.startEmulator(cocoemuExecutable, port);

        // Wait for emulator to start
        // TODO: rewrite
        const emulatorConnectionDelay = emulatorConfiguration.get("delay") as number;
        await sleep(emulatorConnectionDelay);

        await super.start();
    }

    private startEmulator(path: string, port: number): void {
        console.log(`Starting emulator at path: ${path} on port ${port}`);

        const terminalString = `${path} --port ${port}`;

        this.terminal = vscode.window.createTerminal('Emulator Terminal');
        this.terminal.sendText(terminalString);
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
