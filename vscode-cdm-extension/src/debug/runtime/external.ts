import * as vscode from 'vscode';

import { CdmDebugRuntime } from './runtime';

export class ExternalDebugRuntime extends CdmDebugRuntime {
    public constructor(address: string) {
        super(address);
    }

    public shutdown(): this {
        this.ws.close();
        return this;
    }
}