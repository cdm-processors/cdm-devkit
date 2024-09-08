import * as fsPromises from "fs/promises";
import * as pathlib from "path";
import { Stream } from "stream";

import * as vscode from "vscode";

const IS_MEMORY_VIEW_TAB = /^memory-view-(?<index>\d)\.hex$/g;

export class MemoryViewProvider {
    private static VIEWS_NUMBER = 20;

    private view: vscode.Uri;
    private available = new Set(Array(MemoryViewProvider.VIEWS_NUMBER).keys());

    private entry(index: number): vscode.Uri {
        if (index === 0) {
            return this.view;
        } else {
            return vscode.Uri.file(pathlib.join(this.temporaryDirectory, `memory-view-${index}.hex`));
        }
    }

    public constructor(private temporaryDirectory: string) {
        this.view = vscode.Uri.file(pathlib.join(temporaryDirectory, "memory-view-0.hex"));

        fsPromises.writeFile(this.view.fsPath, "").then(() => {
            for (let index = 1; index < MemoryViewProvider.VIEWS_NUMBER; index += 1) {
                fsPromises.symlink(this.view.fsPath, pathlib.join(temporaryDirectory, `memory-view-${index}.hex`)).then(() => {
                    console.log(`Symlink 'memory-view-${index}.hex' has been successfully created`);
                }).catch(() => {
                    console.log(`Symlink 'memory-view-${index}.hex' already exists`);
                });
            }
        });

        vscode.window.tabGroups.onDidChangeTabs((event) => {
            event.closed.forEach((tab) => {
                for (const match of tab.label.matchAll(IS_MEMORY_VIEW_TAB)) {
                    console.log(match);
                    if (match.groups?.index !== undefined) {
                        this.available.add(Number.parseInt(match.groups.index));
                    }
                }
            });
        });
    }

    public async open(): Promise<void> {
        for (let index = 0; index < MemoryViewProvider.VIEWS_NUMBER; index += 1) {
            if (this.available.has(index)) {
                console.log(`Entry 'memory-view-${index}.hex' is available, picking it`);

                this.available.delete(index);
                return await vscode.commands.executeCommand("vscode.openWith", this.entry(index), "hexEditor.hexedit", {
                    preserveFocus: true,
                    viewColumn: vscode.ViewColumn.Beside,
                });
            }
        }

        vscode.window.showWarningMessage("There is no available memory views :(");
    }

    public set dump(memory: 
        | string
        | NodeJS.ArrayBufferView
        | Iterable<string | NodeJS.ArrayBufferView>
        | AsyncIterable<string | NodeJS.ArrayBufferView>
        | Stream
    ) {
        fsPromises.writeFile(this.view.fsPath, memory);
    }

    public async close(): Promise<void> {
        const tabs = [];
        for (const group of vscode.window.tabGroups.all) {
            for (const tab of group.tabs) {
                for (const _ of tab.label.matchAll(IS_MEMORY_VIEW_TAB)) {
                    console.log(tab.label);
                    tabs.push(tab);
                }
            }
        }

        const _ = await vscode.window.tabGroups.close(tabs);
    }
}
