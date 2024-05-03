import argparse
import itertools
from pathlib import Path
from sys import stderr
from typing import Union

import colorama

from cocas import exception_handlers as handlers
from cocas.assembler import AssemblerException, assemble_files, list_assembler_targets, read_mlb
from cocas.exception_handlers import log_error
from cocas.linker import LinkerException, list_linker_targets, target_link, write_debug_export, write_image
from cocas.object_file import ObjectFileException, list_object_targets, read_object_files, write_object_file
from cocas.object_module import ObjectModule


def main():
    colorama.init()
    available_targets = sorted(list_assembler_targets() & list_object_targets() & list_linker_targets())

    parser = argparse.ArgumentParser('cocas')
    parser.add_argument('sources', type=Path, nargs='*', help='source files, object files and macro libraries')
    parser.add_argument('-t', '--target', type=str, default='cdm-16',
                        help='target processor, CdM-16 is default. May omit "cdm"')
    parser.add_argument('-T', '--list-targets', action='count', help='list available targets and exit')
    parser.add_argument('-c', '--compile', action='store_true', help='compile into object files without linking')
    parser.add_argument('-m', '--merge', action='store_true', help='merge object files into one')
    parser.add_argument('-o', '--output', type=Path, help='specify output file name')
    debug_group = parser.add_argument_group('debug')
    debug_group.add_argument('--debug', type=Path, nargs='?', const=True, help='export debug information')
    debug_path_group = debug_group.add_mutually_exclusive_group()
    debug_path_group.add_argument('--relative-path', type=Path,
                                  help='convert source files paths to relative in debug info and object files')
    debug_path_group.add_argument('--absolute-path', type=Path,
                                  help='convert all debug paths to absolute, concatenating with given path')
    debug_group.add_argument('--realpath', action='store_true',
                             help='canonicalize paths by following symlinks and resolving . and ..')
    args = parser.parse_args()
    if args.list_targets:
        print('Available targets: ' + ', '.join(available_targets))
        return
    target: str = args.target.replace('-', '').lower()
    if target[:1].isdecimal():
        target = 'cdm' + target

    if target not in available_targets:
        log_error("Main", 'Unknown target ' + target)
        print('Available targets: ' + ', '.join(available_targets), file=stderr)
        return 2
    if len(args.sources) == 0:
        log_error("Main", 'No source files provided')
        return 2
    if args.compile and args.merge:
        log_error("Main", 'Cannot use --compile and --merge options at same time')
        return 2

    realpath = bool(args.realpath)
    if args.relative_path:
        relative_path: Union[Path, None] = args.relative_path.absolute()
        if realpath:
            relative_path = relative_path.resolve()
    else:
        relative_path = None
    if args.absolute_path:
        absolute_path: Union[Path, None] = args.absolute_path.absolute()
        if realpath:
            absolute_path = absolute_path.resolve()
    else:
        absolute_path = None

    asm_files = []
    obj_files = []
    mlb_files = []
    filepath: Path
    for filepath in args.sources:
        filetype = filepath.suffix or args.merge and '.obj' or '.asm'
        if filetype in ['.obj', '.lib', ]:
            obj_files.append(filepath)
        elif filetype == '.mlb':
            mlb_files.append(filepath)
        else:
            asm_files.append(filepath)
    if asm_files and args.merge:
        log_error("Main", 'Source files should not be provided with --merge option')
        return 2
    if obj_files and args.compile:
        log_error("Main", 'Object files should not be provided with --compile option')
        return 2
    objects: list[tuple[Path, ObjectModule]]
    try:
        macro_libraries = [read_mlb(mlb) for mlb in mlb_files]
        objects: list[tuple[Path, ObjectModule]] = list(itertools.chain(
            assemble_files(target, asm_files, bool(args.debug), relative_path, absolute_path, realpath,
                           macro_libraries=macro_libraries),
            read_object_files(target, obj_files, bool(args.debug), relative_path, absolute_path, realpath)
        ))
    except AssemblerException as e:
        handlers.log_asm_exception(e)
        return 1
    except ObjectFileException as e:
        handlers.log_object_file_exception(e)
        return 1
    except OSError as e:
        handlers.log_os_error(e)
        return 3

    try:
        if args.merge:
            write_object_file((args.output or 'merged.obj'), [tup[1] for tup in objects],
                              target, bool(args.debug or args.merge))
        elif args.compile and args.output:
            write_object_file(args.output, [tup[1] for tup in objects], target, bool(args.debug))
        elif args.compile:
            for path, obj in objects:
                write_object_file(path.with_suffix('.obj').name, [obj], target, bool(args.debug))
        else:
            data, code_locations = target_link(objects, target)
            if args.output:
                write_image(args.output, data)
            else:
                write_image("out.img", data)
            if args.debug:
                if args.debug is True:
                    if args.output:
                        filename = Path(args.output).with_suffix('.dbg.json')
                    else:
                        filename = Path('out.dbg.json')
                else:
                    filename = args.debug
                write_debug_export(filename, code_locations)
    except LinkerException as e:
        handlers.log_link_exception(e)
        return 1
    except OSError as e:
        handlers.log_os_error(e)
        return 3


if __name__ == '__main__':
    result = main()
    exit(result)
