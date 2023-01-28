import argparse
import codecs
import importlib
import json
import pathlib
from dataclasses import asdict

import antlr4
import colorama

from cocas.assembler import assemble
from cocas.ast_builder import build_ast
from cocas.error import CdmException, log_error, CdmLinkException, CdmExceptionTag
from cocas.linker import link
from cocas.macro_processor import process_macros, read_mlb

available_targets = ['cdm8e']


def write_image(filename: str, arr: list):
    """
    Write the contents or array into file in logisim-compatible format

    :param filename: Path to output file
    :param arr: Array to be written
    """
    f = open(filename, mode='wb')
    f.write(bytes("v2.0 raw\n", 'UTF-8'))
    for byte in arr:
        f.write(bytes(f'{byte:02x}\n', 'UTF-8'))
    f.close()


def main():
    colorama.init()
    parser = argparse.ArgumentParser('cocas')
    parser.add_argument('-t', '--target', type=str, default='cdm-8e',
                        help='target processor, CdM-16 is default')
    parser.add_argument('-T', '--list-targets', action='count', help='list available targets and exit')
    # TODO: enable object file generation (if stand-alone linker will be ready)
    # parser.add_argument('-c', '--compile', type=str, help='generate object files without linking')
    parser.add_argument('-o', '--output', type=str, help='specify output file name')
    parser.add_argument('--debug', type=str, help=argparse.SUPPRESS)
    parser.add_argument('sources', type=str, nargs='*', help='source files')
    args = parser.parse_args()
    if args.list_targets:
        print('Available targets: ' + ', '.join(available_targets))
        return

    target: str = args.target.replace('-', '').lower()
    if target not in available_targets:
        print('Error: unknown target ' + target)
        print('Available targets: ' + ', '.join(available_targets))
        return

    if len(args.sources) == 0:
        print('Error: no source files provided')

    target_instructions = importlib.import_module(f'cocas.targets.{target}.target_instructions',
                                                  'cocas').TargetInstructions
    code_segments = importlib.import_module(f'cocas.targets.{target}.code_segments', 'cocas').CodeSegments

    library_macros = read_mlb(str(pathlib.Path(__file__).parent.joinpath(f'targets/{target}/standard.mlb').absolute()))
    objects = []

    for filepath in args.sources:
        try:
            with open(filepath, 'rb') as file:
                data = file.read()
        except OSError as e:
            message = e.strerror
            if e.filename is not None:
                message += f': {colorama.Style.BRIGHT}{e.filename}{colorama.Style.NORMAL}'
            log_error("MAIN", message)
            return 1
        data = codecs.decode(data, 'utf8', 'strict')
        # tolerate files without newline at the end
        if data[-1] != '\n':
            data += '\n'

        try:
            input_stream = antlr4.InputStream(data)
            # Macros (tst, clr but not if) are replaced to commands and wrapped by tags
            # Remove comments
            macro_expanded_input_stream = process_macros(input_stream, library_macros,
                                                         str(pathlib.Path(filepath).absolute()))
            r = build_ast(macro_expanded_input_stream, str(pathlib.Path(filepath).absolute()))
            obj = assemble(r, target_instructions, code_segments)

            objects.append(obj)
        except CdmException as e:
            e.log()
            return 1

    try:
        data, code_locations = link(objects)
    except CdmLinkException as e:
        log_error(str(CdmExceptionTag.LINK), e.message)
        return 1

    try:
        if args.output is not None:
            write_image(args.output, data)
        else:
            write_image("out.img", data)
    except OSError as e:
        message = e.strerror
        if e.filename is not None:
            message += f': {colorama.Style.BRIGHT}{e.filename}{colorama.Style.NORMAL}'
        log_error("MAIN", message)
        return 1

    # write code locations(debug info)
    if args.debug is not None:
        code_locations = {key: asdict(loc) for key, loc in code_locations.items()}
        json_locations = json.dumps(code_locations, indent=4, sort_keys=True)
        try:
            with open(args.debug, 'w') as f:
                f.write(json_locations)
        except OSError as e:
            message = e.strerror
            if e.filename is not None:
                message += f': {colorama.Style.BRIGHT}{e.filename}{colorama.Style.NORMAL}'
            log_error("MAIN", message)
            return 1


if __name__ == '__main__':
    result = main()
    exit(result)
