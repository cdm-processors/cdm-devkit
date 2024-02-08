from antlr4.error.ErrorListener import ErrorListener

from cocas.assembler.generated import AsmParser


class ObjectFileException(Exception):
    def __init__(self, file: str, line: int, description: str):
        self.file = file
        self.line = line
        self.description = description


class AntlrErrorListener(ErrorListener):
    def __init__(self, file):
        self.file = file

    def syntaxError(self, recognizer, offending_symbol, line, column, msg, e):
        if isinstance(recognizer, AsmParser):
            line = line - recognizer.current_offset
            self.file = recognizer.current_file
        raise ObjectFileException(self.file, line, msg)
