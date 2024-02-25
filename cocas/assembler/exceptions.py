from enum import Enum

from antlr4.error.ErrorListener import ErrorListener

from .generated import AsmParser


class AssemblerExceptionTag(Enum):
    """Shows if an exception caused in macros or in usual source code"""
    MACRO = "Macro"
    TPLATE = "Template"
    ASM = "Assembler"


# this exception should be used when we don't know code location now,
# but this info is somewhere up the call stack
# it should be re-raised
# it s here to avoid except Exception
class CdmTempException(Exception):
    def __init__(self, message: str):
        self.message = message


class AssemblerException(Exception):
    """Exception raised when given source code is invalid"""

    def __init__(self, tag: AssemblerExceptionTag, file: str, line: int, description: str):
        self.tag = tag
        self.file = file
        self.line = line
        self.description = description


class AntlrErrorListener(ErrorListener):
    def __init__(self, tag, file):
        self.file = file
        self.tag = tag

    def syntaxError(self, recognizer, offending_symbol, line, column, msg, e):
        if isinstance(recognizer, AsmParser):
            line = line - recognizer.current_offset
            self.file = recognizer.current_file
        raise AssemblerException(self.tag, self.file, line, msg)
