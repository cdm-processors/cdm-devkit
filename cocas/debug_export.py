import bisect
import json
import re

from cocas.location import CodeLocation


def default_json_(o, files):
    # if some json object should be in one line, without \n, wrap it with these __no_breaks
    # do not cascade __no_breaks, regex will break (e.g. {begin, {begin, ..., end}, end}
    if isinstance(o, CodeLocation):
        return {
            "__no_breaks_begin": [],
            "f": bisect.bisect_left(files, o.file), "l": o.line, "c": o.column,
            "__no_breaks_end": []
        }
    else:
        raise TypeError(f'Object of type {o.__class__.__name__} '
                        f'is not JSON serializable')


def default_json(files):
    return lambda x: default_json_(x, files)


def code_location_json(files, cl: CodeLocation):
    return {"f": bisect.bisect_left(files, cl.file), "l": cl.line, "c": cl.column}


def debug_export(code_locations: dict[int, CodeLocation]) -> str:
    files = sorted(set(map(lambda x: x.file, code_locations.values())))
    dump = json.dumps({"files": files, "codeLocations": code_locations},
                      default=default_json(files), indent=4, ensure_ascii=False)
    pattern = re.compile(r"{\n\s+\"__no_breaks_begin\": \[],\n\s+([\S\s]+?),\n\s+\"__no_breaks_end\": \[]\s+}")
    dump = re.sub(pattern, lambda m: "{" + re.sub(r"\n\s+", " ", m.group(1)) + "}", dump)
    return dump
