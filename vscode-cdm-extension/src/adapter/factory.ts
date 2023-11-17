import {
    DebugAdapterDescriptor,
    DebugAdapterDescriptorFactory,
    DebugAdapterExecutable,
    DebugAdapterInlineImplementation,
    DebugSession,
    ProviderResult,
} from "vscode";

import { CdmDebugSession } from "./debugSession";

export class CdmDebugAdapterFactory implements DebugAdapterDescriptorFactory {
    createDebugAdapterDescriptor(session: DebugSession, executable: DebugAdapterExecutable | undefined): ProviderResult<DebugAdapterDescriptor> {
        return new DebugAdapterInlineImplementation(new CdmDebugSession());
    }
}
