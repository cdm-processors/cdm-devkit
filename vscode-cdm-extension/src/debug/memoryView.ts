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
}

abstract class FileSystemManager implements MemoryViewManager {
    protected static MEMORY_VIEW_REGEXP = /^memory-view-(?<index>\d)\.hex$/g;
    protected static MEMORY_VIEWS_NUMBER = 10;
    protected static file = (index: number = 0) => `memory-view-${index}.hex`;

    protected abstract createFiles(): Promise<void>;

    protected dump: vscode.Uri;
    protected availableTabs = new Set<number>(Array(FileSystemManager.MEMORY_VIEWS_NUMBER).keys()); 

    public constructor(
        private tempDirectory: string
    ) {
        const dumpFsPath = pathlib.join(this.tempDirectory, FileSystemManager.file());
        this.dump = vscode.Uri.file(dumpFsPath);

        vscode.window.tabGroups.onDidChangeTabs((event) => {
            event.closed.forEach((tab) => {
                for (const match of tab.label.matchAll(FileSystemManager.MEMORY_VIEW_REGEXP)) {
                    this.availableTabs.add(Number.parseInt(match.groups!.index));
                }
            });
        });

        this.createFiles();
    }

    protected path(index: number): string {
        return pathlib.join(this.tempDirectory, FileSystemManager.file(index));
    }

    protected uri(index: number): vscode.Uri {
        return vscode.Uri.file(this.path(index));
    }

    public async updateDump(memory: Writable): Promise<void> {
        await fsPromises.writeFile(this.dump.fsPath, memory);
    }

    public async createTab(): Promise<void> {
        try {
            const _ = await fsPromises.lstat(this.dump.fsPath);
        } catch (err) {
            await this.createFiles();
        }

        for (let tabIndex = 0; tabIndex < FileSystemManager.MEMORY_VIEWS_NUMBER; tabIndex += 1) {
            if (this.availableTabs.has(tabIndex)) {
                this.availableTabs.delete(tabIndex);

                const _ = await vscode.commands.executeCommand("vscode.openWith", this.uri(tabIndex), "hexEditor.hexedit", {
                    preserveFocus: true,
                    viewColumn: vscode.ViewColumn.Beside,
                });

                return console.log(`Tab 'memory-view-${tabIndex}.hex' has been opened`);
            }
        }

        const _ = await vscode.window.showWarningMessage("There is no available memory views :(");
    }
}

export class SymlinkManager extends FileSystemManager {
    protected async createFiles(): Promise<void> {
        await fsPromises.writeFile(this.dump.fsPath, "");

        for (let tabIndex = 1; tabIndex < FileSystemManager.MEMORY_VIEWS_NUMBER; tabIndex += 1) {
            fsPromises.symlink(this.dump.fsPath, this.path(tabIndex)).then(() => {
                console.log(`Symlink 'memory-view-${tabIndex}.hex' has been successfully created`);
            }).catch((err) => {
                if (err?.code === "EEXIST") {
                    console.log(`Symlink 'memory-view-${tabIndex}.hex' already exists, skipping it`);
                } else {
                    console.log(`Failed to create symlink 'memory-view-${tabIndex}.hex'. ${err}`);
                    vscode.window.showWarningMessage(`Failed to create symlink 'memory-view-${tabIndex}.hex', only one memory view can be used. ${err}`);
                }
            });
        }
    }
}

export class PlainFileManager extends FileSystemManager {
    public async updateDump(memory: Writable): Promise<void> {
        await Promise.all(Array.from({ length: FileSystemManager.MEMORY_VIEWS_NUMBER }, (_, tabIndex) => fsPromises.writeFile(this.path(tabIndex), memory)));
    }

    protected async createFiles(): Promise<void> {
        this.updateDump("");
    }
}
