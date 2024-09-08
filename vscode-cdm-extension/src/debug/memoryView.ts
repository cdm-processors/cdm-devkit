import * as fsPromises from "fs/promises";
import * as pathlib from "path";
import { Stream } from "stream";

import * as vscode from "vscode";

type Writable =
    | string
    | NodeJS.ArrayBufferView
    | Iterable<string | NodeJS.ArrayBufferView>
    | AsyncIterable<string | NodeJS.ArrayBufferView>
    | Stream;

export interface MemoryViewManager {
    updateDump: (memory: Writable) => Promise<void>;
    createTab: () => Promise<void>;
    closeAllTabs: () => Promise<void>;
}

export class SymlinkManager implements MemoryViewManager {
    private static MEMORY_VIEW_REGEXP = /^memory-view-(?<index>\d)\.hex$/g;
    private static MEMORY_VIEWS_NUMBER = 10;

    private static file(index: number = 0): string {
        return `memory-view-${index}.hex`;
    }

    private path(index: number): string {
        return pathlib.join(this.tempDirectory, SymlinkManager.file(index));
    }

    private uri(index: number): vscode.Uri {
        return vscode.Uri.file(this.path(index));
    }

    private dump: vscode.Uri;
    private availableTabs = new Set<number>(Array(SymlinkManager.MEMORY_VIEWS_NUMBER).keys()); 

    public constructor(
        private tempDirectory: string
    ) {
        const dumpFsPath = pathlib.join(this.tempDirectory, SymlinkManager.file());
        this.dump = vscode.Uri.file(dumpFsPath);

        vscode.window.tabGroups.onDidChangeTabs((event) => {
            event.closed.forEach((tab) => {
                for (const match of tab.label.matchAll(SymlinkManager.MEMORY_VIEW_REGEXP)) {
                    this.availableTabs.add(Number.parseInt(match.groups!.index));
                }
            });
        });
    }

    public async updateDump(memory: Writable): Promise<void> {
        await fsPromises.writeFile(this.dump.fsPath, memory);
    }

    private async createDump(): Promise<void> {
        await fsPromises.writeFile(this.dump.fsPath, "");

        for (let tabIndex = 1; SymlinkManager.MEMORY_VIEWS_NUMBER; tabIndex += 1) {
            const _ = await fsPromises.symlink(this.dump.fsPath, this.path(tabIndex), "file").then(() => {
                console.log(`Symlink 'memory-view-${tabIndex}.hex' has been successfully created`);
            }).catch((err) => {
                if (err?.code === "EEXIST") {
                    console.log(`Symlink 'memory-view-${tabIndex}.hex' already exists, skipping it`);
                } else {
                    console.log(`Failed to create symlink 'memory-view-${tabIndex}.hex'. ${err}`);
                }
            });
        }
    }

    public async createTab(): Promise<void> {
        try {
            const _ = await fsPromises.lstat(this.dump.fsPath);
        } catch (err) {
            await this.createDump();
        }

        for (let tabIndex = 0; tabIndex < SymlinkManager.MEMORY_VIEWS_NUMBER; tabIndex += 1) {
            if (this.availableTabs.has(tabIndex)) {
                const _ = await vscode.commands.executeCommand("vscode.openWith", this.uri(tabIndex), "hexEditor.hexedit", {
                    preserveFocus: true,
                    viewColumn: vscode.ViewColumn.Beside,
                });

                return console.log(`Tab 'memory-view-${tabIndex}.hex' has been opened`);
            }
        }

        const _ = await vscode.window.showWarningMessage("There is no available memory views :(");
    }

    public async closeAllTabs(): Promise<void> {
        const viewTabs = [];
        for (const group of vscode.window.tabGroups.all) {
            for (const tab of group.tabs) {
                for (const _ of tab.label.matchAll(SymlinkManager.MEMORY_VIEW_REGEXP)) {
                    viewTabs.push(tab);
                }
            }
        }

        const _ = await vscode.window.tabGroups.close(viewTabs);
    }
}
