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
    # TODO: enable object file generation (when stand-alone linker will be ready)
    parser = argparse.ArgumentParser('Cdm8e assembler')
    # parser.add_argument('-o', '--object', type=str, help='Object file directory (object files will be stored here)')
    parser.add_argument('-i', '--image', type=str, help='Image file path')
    parser.add_argument('-d', '--debug', type=str, help='Debug info path')
    parser.add_argument('sources', type=str, nargs='+', help='Source files')
    args = parser.parse_args()

    colorama.init()

    isa_name = 'cdm8e'
    target_instructions = importlib.import_module(f'targets.{isa_name}.target_instructions', 'cocas').TargetInstructions
    code_segments = importlib.import_module(f'targets.{isa_name}.code_segments', 'cocas').CodeSegments

    library_macros = read_mlb(
        str(pathlib.Path(__file__).parent.joinpath(f'standard.mlb').absolute()))
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
            # InputStream: Vacuum all input from a string and then treat it like a buffer.
            input_stream = antlr4.InputStream(data)
            # Assembler code but with one tag in the beginning
            # Macros (tst, clr but not if) are replaced to commands and wrapped by tags
            # Number in tags - begin/end line numbers and macro number
            # Hash of source file name
            # Remove comments
            macro_expanded_input_stream = process_macros(input_stream, library_macros,
                                                         str(pathlib.Path(filepath).absolute()))
            # print(macro_expanded_input_stream)
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
        if args.image is not None:
            write_image(args.image, data)
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
    result = 0 if result is None else result
    exit(result)
