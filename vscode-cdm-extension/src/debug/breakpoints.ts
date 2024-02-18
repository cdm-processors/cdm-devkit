import * as vscode from "vscode";
import { Breakpoint, Source } from "@vscode/debugadapter";
import { DebugProtocol } from "@vscode/debugprotocol";

type Location = {
    source: Source;
    line: number;
};

export class DebugInfoHander {
    private breakpointLocations = new Map<string, number[]>();

    private constructor(
        private sources: Source[],
        private locations: Map<number, Location>,
        private addresses: Map<string, number>,
        private collectedAddresses: number[],
    ) {}

    public static parse(obj: any): DebugInfoHander {
        const paths = obj?.files;
        if (!Array.isArray(paths)) {
            const message = "Failed to parse the debug information: 'files' property is either missing or not an array";
            console.error(message);
            throw new Error(message);
        }

        const sources: Source[] = [];
        for (const [index, path] of paths.entries()) {
            if (typeof path !== "string") {
                const message = `Failed to parse the debug information: 'files[${index}]' is not a string`;
                console.error(message);
                throw new Error(message);
            }

            const uriParsed = vscode.Uri.parse("file:" + path).fsPath;
            const filename = uriParsed.lastIndexOf("/");
            sources.push(new Source(uriParsed.substring(filename + 1), uriParsed));
        }

        const rawLocations = obj?.codeLocations;
        if (rawLocations && typeof rawLocations !== "object") {
            const message = "Failed to parse the debug information: 'codeLocations' property is either missing or not an object";
            console.error(message);
            throw new Error(message);
        }

        const locations = new Map<number, Location>();
        const addresses = new Map<string, number>();
        const collectedAddresses = [];
        for (const [rawAddress, location] of Object.entries(rawLocations)) {
            const address = parseInt(rawAddress);
            if (Number.isNaN(address)) {
                const message = `Failed to parse the debug information: address '${rawAddress}' can't be parsed as a number`;
                console.error(message);
                throw new Error(message);
            }

            if (location && typeof location === "object" &&
                "f" in location && typeof location.f === "number" &&
                "l" in location && typeof location.l === "number" &&
                "c" in location && typeof location.c === "number") {

                const { f, l, c } = location;
                locations.set(address, { source: sources[f], line: l });
                addresses.set([f, l, c].join(", "), address);
                collectedAddresses.push(address);
            } else {
                const message = `Failed to parse the debug information: address '${rawAddress}' profile contains invalid data`;
                console.error(message);
                throw new Error(message);
            }
        }

        return new DebugInfoHander(sources, locations, addresses, collectedAddresses);
    }

    public stepLocations(): number[] {
        return this.collectedAddresses;
    }

    public restoreSourceLocation(address: number): Location | undefined {
        return this.locations.get(address);
    }

    public validateBreakpoints(path: string, breakpoints: DebugProtocol.SourceBreakpoint[]): Breakpoint[] {
        const uriParsed = vscode.Uri.parse("file:" + path).fsPath;
        const sourceIndex = this.sources.findIndex((source) => source.path === uriParsed);
        if (sourceIndex === -1) {
            const message = `Failed to retrieve a Source object for file at '${uriParsed}'`;
            console.error(message);
            throw new Error(message);
        }

        const source = this.sources[sourceIndex];
        const validated = [];
        const locations = [];
        for (const { column, line } of breakpoints) {
            let verified = false;
            let address = this.addresses.get([sourceIndex, line, 0].join(", "));

            if (address !== undefined) {
                verified = true;
                locations.push(address);
            }

            validated.push(new Breakpoint(verified, line, column, source));
        }

        this.breakpointLocations.set(uriParsed, locations);

        return validated;
    }

    public emitBreakpointLocations(): number[] {
        const collected: number[] = [];
        this.breakpointLocations.forEach((locations) => collected.push(...locations));
        return collected;
    }
}
