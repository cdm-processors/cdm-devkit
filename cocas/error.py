from enum import Enum
from typing import Union

from antlr4.error.ErrorListener import ErrorListener
from colorama import Fore, Style

from cocas.assembler.generated import AsmParser


class CdmExceptionTag(Enum):
    MACRO = "Macro"
    ASM = "Assembler"
    OBJ = "Object files"
    LINK = "Linker"


# this exception should be used when we don't know code location now,
# but this info is somewhere up the call stack
# it should be re-raised
# it s here to avoid except Exception
class CdmTempException(Exception):
    def __init__(self, message: str):
        self.message = message


class CdmLinkException(Exception):
    def __init__(self, message: str):
        self.message = message


class CdmException(Exception):
    def __init__(self, tag: Union[str, CdmExceptionTag], file: str, line: int, description: str):
        if isinstance(tag, CdmExceptionTag):
            tag = tag.value
        self.tag = tag
        self.file = file
        self.line = line
        self.description = description

    def log(self):
        print(
            f'[{self.tag}] {Fore.RED}ERROR{Fore.RESET} at line {Style.BRIGHT}{self.line}{Style.RESET_ALL} of '
            f'{Style.BRIGHT}{self.file}{Style.RESET_ALL}')
        print(f'{self.description}')


def log_error(tag: str, message: str):
    print(
        f'[{tag}] {Fore.RED}ERROR{Fore.RESET}')
    print(message)


class AntlrErrorListener(ErrorListener):
    def __init__(self, tag, file):
        self.file = file
        self.tag = tag

    def syntaxError(self, recognizer, offending_symbol, line, column, msg, e):
        if isinstance(recognizer, AsmParser):
            line = line - recognizer.current_offset
            self.file = recognizer.current_file
        raise CdmException(self.tag, self.file, line, msg)
