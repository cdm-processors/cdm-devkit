import codecs
from itertools import chain
from pathlib import Path
from typing import Any, Optional

import antlr4

from cocas.object_module import ObjectModule

from .ast_builder import build_ast
from .macro_processor import ExpandMacrosVisitor, process_macros, read_mlb
from .object_generator import generate_object_module
from .targets import TargetInstructionsInterface, import_target, mlb_path


def assemble_module(input_stream: antlr4.InputStream,
                    target_instructions: TargetInstructionsInterface,
                    macros_library: ExpandMacrosVisitor,
                    filepath: Path,
                    debug_info_path: Optional[Path] = None) -> ObjectModule:
    """
    Convert lines of an assembler file to object code

    :param input_stream: contents of file
    :param target_instructions: information how to convert mnemonics to code segments
    :param macros_library: standard macros of assembler
    :param filepath: path of the file to use in error handling
    :param debug_info_path: transformed path of the file to use in debug information
    """
    macro_expanded_input_stream = process_macros(input_stream, macros_library, str(filepath))
    r = build_ast(macro_expanded_input_stream, str(filepath))
    return generate_object_module(r, target_instructions, debug_info_path)


def get_debug_info_path(filepath: Path,
                        debug: Optional[Any],
                        relative_path: Optional[Path],
                        realpath: bool) -> Optional[Path]:
    if debug:
        debug_info_path = filepath.expanduser().absolute()
        if realpath:
            debug_info_path = debug_info_path.resolve()
        if relative_path:
            debug_info_path = debug_info_path.relative_to(relative_path)
    else:
        debug_info_path = None
    return debug_info_path


def assemble_files(target: str,
                   files: list[Path],
                   debug: bool,
                   relative_path: Optional[Path],
                   absolute_path: Optional[Path],
                   realpath: bool) -> list[tuple[Path, ObjectModule]]:
    """
    Open and assemble multiple files into object modules

    :param target: name of processor target
    :param files: list of assembler files' paths to process
    :param debug: if debug information should be collected
    :param relative_path: if debug paths should be relative to some path
    :param absolute_path: if relative paths should be converted to absolute
    :param realpath: if paths should be converted to canonical
    """
    _ = absolute_path
    target_instructions = import_target(target)
    macros_library = read_mlb(str(mlb_path(target)))
    objects = []

    for filepath in files:
        with filepath.open('rb') as file:
            data = file.read()
        data = codecs.decode(data, 'utf8', 'strict')
        if not data.endswith('\n'):
            data += '\n'

        debug_info_path = get_debug_info_path(filepath, debug, relative_path, realpath)
        input_stream = antlr4.InputStream(data)
        obj = assemble_module(input_stream, target_instructions, macros_library, filepath, debug_info_path)
        if debug_info_path:
            fp = filepath.as_posix()
            dip = debug_info_path.as_posix()
            for i in chain(obj.asects, obj.rsects):
                for j in i.code_locations.values():
                    if j.file == fp:
                        j.file = dip
                    else:
                        f = Path(j.file).absolute()
                        if realpath:
                            f = f.resolve()
                        j.file = f.relative_to(relative_path).as_posix()
        objects.append((filepath, obj))
    return objects
