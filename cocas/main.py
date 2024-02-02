import argparse
from pathlib import Path
from typing import Union

import colorama

from cocas.assembler import assemble_files, list_assembler_targets
from cocas.error import CdmException, log_error
from cocas.linker import link, write_debug_export, write_image
from cocas.object_file import list_object_targets, read_object_files, write_object_file
from cocas.object_module import ObjectModule


def handle_os_error(e: OSError):
    message = e.strerror
    if e.filename is not None:
        message += f': {colorama.Style.BRIGHT}{e.filename}{colorama.Style.NORMAL}'
    log_error("MAIN", message)
    exit(1)


def main():
    colorama.init()
    available_targets = list_assembler_targets() & list_object_targets()

    parser = argparse.ArgumentParser('cocas')
    parser.add_argument('sources', type=Path, nargs='*', help='source files')
    parser.add_argument('-t', '--target', type=str, default='cdm-16', help='target processor, CdM-16 is default')
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

    if target not in available_targets:
        print('Error: unknown target ' + target)
        print('Available targets: ' + ', '.join(available_targets))
        return 2
    if len(args.sources) == 0:
        print('Error: no source files provided')
        return 2
    if args.compile and args.merge:
        print('Error: cannot use --compile and --merge options at same time')
        return 2

    objects: list[tuple[Path, ObjectModule]] = []

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

    filepath: Path
    for filepath in args.sources:
        try:
            filetype = filepath.suffix
            if not filetype:
                if args.merge:
                    filetype = '.obj'
                else:
                    filetype = '.asm'

            if filetype in ['.obj', '.lib', ]:
                if args.compile:
                    print("Error: object files should not be provided with --compile option")
                    return 2
                objects += read_object_files(target, [filepath], bool(args.debug),
                                             relative_path, absolute_path, realpath)
            else:  # filetype == '.asm'
                if args.merge:
                    print("Error: source files should not be provided with --merge option")
                    return 2
                objects += assemble_files(target, [filepath], bool(args.debug),
                                          relative_path, absolute_path, realpath)

        except CdmException as e:
            e.log()
            return 1

    if args.merge:
        write_object_file('merged.obj', [tup[1] for tup in objects], target, (args.debug or args.merge))
    elif args.compile and args.output:
        write_object_file(args.output, [tup[1] for tup in objects], target, (args.debug or args.merge))
    elif args.compile:
        for path, obj in objects:
            write_object_file(path.with_suffix('.obj').name, [obj], target, args.debug)
    else:
        data, code_locations = link(objects)
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


if __name__ == '__main__':
    result = main()
    exit(result)
