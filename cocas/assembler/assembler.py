from pathlib import Path
from typing import Optional

from antlr4 import InputStream

from cocas.object_module import ObjectModule

from .ast_builder import build_ast
from .macro_processor import ExpandMacrosVisitor, process_macros
from .object_generator import generate_object_module
from .targets import CodeSegmentsInterface, TargetInstructionsInterface


def assemble_module(input_stream: InputStream, target_instructions: TargetInstructionsInterface,
                    code_segments: CodeSegmentsInterface, library_macros: ExpandMacrosVisitor,
                    filepath: Path, debug_info_path: Optional[Path] = None) -> ObjectModule:
    """
    Convert lines of an assembler file to object code
    :param input_stream: contents of file
    :param target_instructions: information how to convert mnemonics to code segments
    :param code_segments: information how to compile segments into machine code
    :param library_macros: standard macros of assembler
    :param filepath: path of the file to use in error handling
    :param debug_info_path: transformed path of the file to use in debug information
    """
    macro_expanded_input_stream = process_macros(input_stream, library_macros, str(filepath))
    r = build_ast(macro_expanded_input_stream, str(filepath))
    return generate_object_module(r, target_instructions, code_segments, debug_info_path)
