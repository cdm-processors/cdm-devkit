export interface CodeLocation {
    file: string;
    line: number;
    column: number;
}

export type CodeMap = Map<number, CodeLocation>;

export function parseCodeMap(data: string): CodeMap {
    const codeMapJson = JSON.parse(data);

    let ret: CodeMap = new Map();
    for (const [key, value] of Object.entries(codeMapJson)) {
        ret.set(parseInt(key), value as CodeLocation);
    }

    return filterCodeMap(ret);
}


function locationToString(loc: CodeLocation): string{
    return `${loc.line} ${loc.file}`;
}


// retains only one occurence of line (the one with smaller PC)
function filterCodeMap(codeMap: CodeMap): CodeMap{
    const usedLocations = new Set<string>();

    const entries = Array.from(codeMap.entries());
    entries.sort((a, b) => a[0] - b[0]);
    

    let res: CodeMap = new Map();
    for(let entry of entries){
        const strKey = locationToString(entry[1]);
        if(!usedLocations.has(strKey)){
            usedLocations.add(strKey);
            res.set(entry[0], entry[1]);
        }
    }

    return res;
}