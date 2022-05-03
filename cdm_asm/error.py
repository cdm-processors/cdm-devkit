from antlr4.error.Errors import CancellationException, ParseCancellationException
from antlr4.error.ErrorListener import ErrorListener
from colorama import Fore, Back, Style
from enum import Enum
from cdm_asm.generated import AsmParser


class CdmExceptionTag(Enum):
    MACRO = "Macro"
    ASM = "Assembler"
    LINK = "Linker"


class CdmException(Exception):
    def __init__(self, tag: str | CdmExceptionTag, file: str, line: int, description: str):
        if isinstance(tag, CdmExceptionTag):
            tag = tag.value
        self.tag = tag
        self.file = file
        self.line = line
        self.description = description

    def log(self):
        print(f'[{self.tag}] {Fore.RED}ERROR{Fore.RESET} at line {Style.BRIGHT}{self.line}{Style.RESET_ALL} of {Style.BRIGHT}{self.file}{Style.RESET_ALL}')
        print(f'{self.description}')




class AntlrErrorListener(ErrorListener):
    def __init__(self, tag, file):
        self.file = file
        self.tag = tag

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        if isinstance(recognizer, AsmParser.AsmParser):
            line = line - recognizer.current_offset
            self.file = recognizer.current_file
        raise CdmException(self.tag, self.file, line, msg)



