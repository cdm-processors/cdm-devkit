import * as vscode from 'vscode';
import {ProviderResult} from 'vscode';
// import { getCdmPath } from './cdmPath';
import { CdmDebugSession } from './debugSession';

export const cdmDebugSessionType = 'cdm';

export function activateCdmDebug(context: vscode.ExtensionContext){
    

    const factory = new InlineDebugAdapterFactory();
    context.subscriptions.push(vscode.debug.registerDebugAdapterDescriptorFactory(cdmDebugSessionType, factory));
    if ('dispose' in factory) {
        context.subscriptions.push(factory as unknown as { dispose(): any });
    }
}



class InlineDebugAdapterFactory implements vscode.DebugAdapterDescriptorFactory {
    createDebugAdapterDescriptor(_session: vscode.DebugSession): ProviderResult<vscode.DebugAdapterDescriptor> {
        return new vscode.DebugAdapterInlineImplementation(new CdmDebugSession());
    }
}
