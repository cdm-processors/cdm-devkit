from antlr4.error.ErrorListener import ErrorListener


class ObjectFileException(Exception):
    """Exception raised when given object file is invalid"""

    def __init__(self, file: str, line: int, description: str):
        self.file = file
        self.line = line
        self.description = description


class AntlrErrorListener(ErrorListener):
    def __init__(self, file):
        self.file = file

    def syntaxError(self, recognizer, offending_symbol, line, column, msg, e):
        raise ObjectFileException(self.file, line, msg)
