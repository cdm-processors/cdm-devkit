import argparse
import codecs
import importlib
import json
import os
import pathlib
import pkgutil
from dataclasses import asdict
from typing import Union

import antlr4
import colorama

from cocas.assembler import assemble
from cocas.ast_builder import build_ast
from cocas.error import CdmException, CdmExceptionTag, CdmLinkException, log_error
from cocas.linker import link
from cocas.macro_processor import process_macros, read_mlb
from cocas.object_file import import_object
from cocas.object_module import export_objects


def write_image(filename: str, arr: bytearray):
    """
    Write the contents or array into file in logisim-compatible format

    :param filename: Path to output file
    :param arr: Bytearray to be written
    """
    f = open(filename, mode='wb')
    f.write(bytes("v2.0 raw\n", 'UTF-8'))
    zeroes = 0
    for i, byte in enumerate(arr):
        if byte == 0:
            zeroes += 1
        else:
            if zeroes != 0:
                if zeroes > 4:
                    f.write(bytes(f'{zeroes}*00\n', 'UTF-8'))
                    f.write(bytes(f'# {i:#2x}\n', 'UTF-8'))
                else:
                    for _ in range(zeroes):
                        f.write(bytes('00\n', 'UTF-8'))
                zeroes = 0
            f.write(bytes(f'{byte:02x}\n', 'UTF-8'))
    f.close()


def handle_os_error(e: OSError):
    message = e.strerror
    if e.filename is not None:
        message += f': {colorama.Style.BRIGHT}{e.filename}{colorama.Style.NORMAL}'
    log_error("MAIN", message)
    exit(1)


def main():
    colorama.init()
    targets_dir = os.path.join(os.path.dirname(__file__), "targets")
    available_targets = list(map(lambda i: i.name, pkgutil.iter_modules([targets_dir])))

    parser = argparse.ArgumentParser('cocas')
    parser.add_argument('sources', type=pathlib.Path, nargs='*', help='source files')
    parser.add_argument('-t', '--target', type=str, default='cdm-16', help='target processor, CdM-16 is default')
    parser.add_argument('-T', '--list-targets', action='count', help='list available targets and exit')
    parser.add_argument('-c', '--compile', action='store_true', help='compile into object files without linking')
    parser.add_argument('-m', '--merge', action='store_true', help='merge object files into one')
    parser.add_argument('-o', '--output', type=str, help='specify output file name')
    debug_group = parser.add_argument_group('debug')
    debug_group.add_argument('--debug', type=str, nargs='?', const='out.dbg.json', help='export debug information')
    debug_path_group = debug_group.add_mutually_exclusive_group()
    debug_path_group.add_argument('--relative-path', type=pathlib.Path,
                                  help='convert source files paths in debug information to relative from given path')
    debug_path_group.add_argument('--absolute-path', type=pathlib.Path, nargs='?', const=None,
                                  help='covert source files paths in debug information to absolute, starting from '
                                       'given or current working directory (default behaviour)')
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

    target_instructions = importlib.import_module(f'cocas.targets.{target}.target_instructions',
                                                  'cocas').TargetInstructions
    code_segments = importlib.import_module(f'cocas.targets.{target}.code_segments', 'cocas').CodeSegments
    target_params = importlib.import_module(f'cocas.targets.{target}.target_params', 'cocas').TargetParams

    library_macros = read_mlb(str(pathlib.Path(__file__).parent.joinpath(f'targets/{target}/standard.mlb').absolute()))
    objects = []

    if args.relative_path:
        relative_path: Union[pathlib.Path, None] = args.relative_path.resolve()
    else:
        relative_path = None

    raw_path: pathlib.Path
    for raw_path in args.sources:
        dbg_info_path = raw_path.expanduser().absolute()
        if relative_path:
            try:
                dbg_info_path = dbg_info_path.resolve().relative_to(relative_path)
            except ValueError as e:
                print('Error:', e)
                return 2
        try:
            with raw_path.open('rb') as file:
                data = file.read()
        except OSError as e:
            handle_os_error(e)
        data = codecs.decode(data, 'utf8', 'strict')
        if not data.endswith('\n'):
            data += '\n'

        try:
            filetype = dbg_info_path.suffix
            if not filetype:
                if args.merge:
                    filetype = '.obj'
                else:
                    filetype = '.asm'

            if filetype == '.obj':
                if args.compile:
                    print("Error: object files should not be provided with --compile option")
                    return 2
                input_stream = antlr4.InputStream(data)
                for obj in import_object(input_stream, str(dbg_info_path.absolute()), target_params):
                    objects.append((dbg_info_path, obj))
            else:
                if args.merge:
                    print("Error: source files should not be provided with --merge option")
                    return 2
                input_stream = antlr4.InputStream(data)
                macro_expanded_input_stream = process_macros(input_stream, library_macros, str(dbg_info_path))
                r = build_ast(macro_expanded_input_stream, str(dbg_info_path))
                obj = assemble(r, target_instructions, code_segments, dbg_info_path)
                objects.append((dbg_info_path, obj))
        except CdmException as e:
            e.log()
            return 1

    if args.merge or args.compile and args.output:
        if args.output:
            obj_path = args.output
        else:
            obj_path = pathlib.Path.cwd() / 'merged.obj'
        lines = export_objects([tup[1] for tup in objects], target_params, args.debug)
        try:
            with open(obj_path, 'w') as file:
                file.writelines(lines)
        except OSError as e:
            handle_os_error(e)
    elif args.compile:
        for dbg_info_path, obj in objects:
            obj_path = pathlib.Path.cwd() / ((dbg_info_path.name[:-4] if dbg_info_path.name.endswith('.asm') else dbg_info_path.name) + '.obj')
            lines = export_objects([obj], target_params, args.debug)
            try:
                with open(obj_path, 'w') as file:
                    file.writelines(lines)
            except OSError as e:
                handle_os_error(e)
    else:
        try:
            data, code_locations = link(objects, target_params)
        except CdmLinkException as e:
            log_error(CdmExceptionTag.LINK.value, e.message)
            return 1
        try:
            if args.output:
                write_image(args.output, data)
            else:
                write_image("out.img", data)
        except OSError as e:
            handle_os_error(e)

        if args.debug:
            code_locations = {key: asdict(loc) for key, loc in code_locations.items()}
            json_locations = json.dumps(code_locations, indent=4, sort_keys=True)
            try:
                with open(args.debug, 'w') as f:
                    f.write(json_locations)
            except OSError as e:
                handle_os_error(e)


if __name__ == '__main__':
    result = main()
    exit(result)
