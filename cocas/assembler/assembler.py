import codecs
from itertools import chain
from pathlib import Path
from typing import Any, Optional

import antlr4

from cocas.object_module import ObjectModule

from .ast_builder import build_ast
from .exceptions import AssemblerException, AssemblerExceptionTag
from .macro_processor import MacroDefinition, process_macros, read_mlb
from .object_generator import generate_object_module
from .targets import TargetInstructions, import_target, standard_mlb


def assemble_module(input_stream: antlr4.InputStream,
                    target_instructions: TargetInstructions,
                    macros_library: dict[str, dict[int, MacroDefinition]],
                    filepath: Path) -> ObjectModule:
    """
    Convert lines of an assembler file to object code

    :param input_stream: contents of file
    :param target_instructions: information how to convert mnemonics to code segments
    :param macros_library: standard macros of assembler
    :param filepath: path of the file to use in error handling
    """
    macro_expanded_input_stream = process_macros(input_stream, macros_library, filepath)
    r = build_ast(macro_expanded_input_stream, filepath)
    return generate_object_module(r, target_instructions)


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
                   realpath: bool,
                   macro_libraries: list[dict[str, dict[int, MacroDefinition]]] = None
                   ) -> list[tuple[Path, ObjectModule]]:
    """
    Open and assemble multiple files into object modules

    :param target: name of processor, should be valid
    :param files: list of assembler files' paths to process
    :param debug: if debug information should be collected
    :param relative_path: if debug paths should be relative to some path
    :param absolute_path: if relative paths should be converted to absolute
    :param realpath: if paths should be converted to canonical
    :param macro_libraries: user's .mlb files, different from standard .mlb
    :return: list of pairs [source file path, object module]
    """
    _ = absolute_path
    target_instructions = import_target(target)
    macros = read_mlb(standard_mlb(target))
    if macro_libraries:
        for lib in macro_libraries:
            for name in lib.keys():
                for i in lib[name].keys() & macros.get(name, {}).keys():
                    if lib[name][i] != macros[name][i]:
                        raise AssemblerException(AssemblerExceptionTag.MACRO,
                                                 lib[name][i].location.file, lib[name][i].location.line,
                                                 description=f"Redefinition of macro {name}/{i} with different body")
            macros |= lib

    objects = []

    for filepath in files:
        with filepath.open('rb') as file:
            data = file.read()
        data = codecs.decode(data, 'utf8', 'strict')
        if not data.endswith('\n'):
            data += '\n'
        input_stream = antlr4.InputStream(data)
        obj = assemble_module(input_stream, target_instructions, macros, filepath)

        debug_info_path = get_debug_info_path(filepath, debug, relative_path, realpath)
        if debug_info_path:
            obj.source_file_path = debug_info_path
            fp = filepath.absolute().as_posix()
            dip = debug_info_path.as_posix()
            for lib in chain(obj.asects, obj.rsects):
                for j in lib.code_locations.values():
                    if j.file == fp:
                        j.file = dip
                    elif j.file is not None:
                        p = get_debug_info_path(Path(j.file), debug, relative_path, realpath)
                        j.file = str(p) if p is not None else None
        objects.append((filepath, obj))
    return objects
