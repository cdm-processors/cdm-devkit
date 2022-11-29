import codecs
import json

import colorama
from antlr4 import *

from cdm_asm.error import CdmException, log_error, CdmLinkException, CdmExceptionTag
from cdm_asm.macro_processor import process_macros, read_mlb
from cdm_asm.assembler import ObjectModule, assemble
from cdm_asm.ast_builder import build_ast
from cdm_asm.linker import link
import os.path
import sys
from dataclasses import asdict
import pathlib
import os
import argparse


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

    try:
        # Contains information from standard.mlb
        # Definitions of macros and how to convert them into commands
        library_macros = read_mlb(str(pathlib.Path(__file__).parent.joinpath('standard.mlb').absolute()))
        source_files = args.sources
        objects = []
        for filepath in source_files:
            with open(filepath, 'rb') as file:
                data = file.read()
                data = codecs.decode(data, 'utf8', 'strict')
                # tolerate files without newline at the end
                if data[-1] != '\n':
                    data += '\n'
                # InputStream: Vacuum all input from a string and then treat it like a buffer.
                input_stream = InputStream(data)

            # Assembler code but with one tag in the beginning
            # Macros (tst, clr but not if) are replaced to commands and wrapped by tags
            # Number in tags - begin/end line numbers and macro number
            # Hash of source file name
            # Remove comments
            macro_expanded_input_stream = process_macros(input_stream, library_macros,
                                                         str(pathlib.Path(filepath).absolute()))
            # print(macro_expanded_input_stream)
            r = build_ast(macro_expanded_input_stream, str(pathlib.Path(filepath).absolute()))
            obj = assemble(r)

            objects.append(obj)

        data, code_locations = link(objects)
        image_root, _ = os.path.splitext(source_files[0])
        if args.image is not None:
            write_image(args.image, data)
        else:
            write_image("out.img", data)

        # write code locations(debug info)
        code_locations = {key: asdict(loc) for key, loc in code_locations.items()}
        json_locations = json.dumps(code_locations, indent=4, sort_keys=True)
        if args.debug is not None:
            with open(args.debug, 'w') as f:
                f.write(json_locations)
    except CdmException as e:
        e.log()
        exit(1)
    except OSError as e:
        message = e.strerror
        if e.filename is not None:
            message += f': {colorama.Style.BRIGHT}{e.filename}{colorama.Style.NORMAL}'
        if e.filename2 is not None:
            message += f', {colorama.Style.BRIGHT}{e.filename2}{colorama.Style.NORMAL}'
        log_error("MAIN", message)
        exit(1)
    except CdmLinkException as e:
        log_error(CdmExceptionTag.LINK.value, e.message)
        exit(1)


if __name__ == '__main__':
    main()
