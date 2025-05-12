import bisect
import json
import re
from pathlib import Path
from typing import Union

from cocas.object_module import CodeLocation


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
    """
    Convert debug information objects to json format

    :param code_locations: mapping from address in binary image to location in source code
    :return: string with json representation of debug information, code locations are sorted
    """
    code_locations = {addr: cl for addr, cl in code_locations.items() if cl.file is not None}
    files = sorted({cl.file for cl in code_locations.values()})
    sorted_cl = {key: value for (key, value) in sorted(code_locations.items())}
    dump = json.dumps({"files": files, "codeLocations": sorted_cl},
                      default=default_json(files), indent=4, ensure_ascii=False)
    pattern = re.compile(r"{\n\s+\"__no_breaks_begin\": \[],\n\s+([\S\s]+?),\n\s+\"__no_breaks_end\": \[]\s+}")
    dump = re.sub(pattern, lambda m: "{" + re.sub(r"\n\s+", " ", m.group(1)) + "}", dump)
    return dump


def write_debug_export(filepath: Union[Path, str], code_locations: dict[int, CodeLocation]):
    """
    Convert debug information objects to json format and write to file

    :param filepath: path to file to write
    :param code_locations: mapping from address in binary image to location in source code
    :return: json file with debug information, code locations are sorted
    """
    with open(filepath, 'w') as f:
        f.write(debug_export(code_locations))
