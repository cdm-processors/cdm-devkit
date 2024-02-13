
import { Breakpoint, Source } from "@vscode/debugadapter";
import { DebugProtocol } from "@vscode/debugprotocol";

type CodeLocation = {
    f: number;
    l: number;
    c: number;
};

type DebugInformation = {
    files: string[];
    codeLocations: Map<number, CodeLocation>;
};

export class BreakpointHandler {
    private shorten: string[];
    private full: string[];

    private direct: Map<number, CodeLocation>;
    private inverse: Map<string, number>;

    constructor(
        files: string[],
        codeLocations: Map<number, CodeLocation>,
    ) {
        this.shorten = files.map((full) => full.substring(full.lastIndexOf("/")));
        this.full = files;
        this.direct = codeLocations;
        this.inverse = new Map();
        this.direct.forEach((value, key) => this.inverse.set(`${value.f}, ${value.l}, ${value.c}`, key));
    }

    codes(): IterableIterator<number> {
        return this.direct.keys();
    }

    fromProgramCounter(pc: number): { source: Source, line: number } | undefined {
        const codeLocation = this.direct.get(pc);
        if (codeLocation === undefined) {
            return;
        }

        return {
            source: new Source(this.shorten[codeLocation.f], this.full[codeLocation.f]),
            line: codeLocation.l,
        };
    }

    fromSetBreakpointsRequest(path: string, breakpoints: DebugProtocol.SourceBreakpoint[]): { checkedBreakpoints: Breakpoint[], codes: number[] } | undefined {
        const file = this.full.indexOf(path);
        if (file === -1) {
            return;
        }

        let checkedBreakpoints = [];
        let codes = [];

        let source = new Source(this.shorten[file], path);
        let key = { f: file, l: 0, c: 0 };
        for (const breakpoint of breakpoints) {
            key.l = breakpoint.line;
            const candidate = this.inverse.get(`${key.f}, ${key.l}, ${key.c}`);
            checkedBreakpoints.push(new Breakpoint(candidate !== undefined, breakpoint.line, breakpoint.column, source));
            if (candidate !== undefined) {
                codes.push(candidate);
            }
        }

        return {
            checkedBreakpoints: checkedBreakpoints,
            codes: codes,
        };
    }
}
