class LinkerException(Exception):
    """Exception raised when sections cannot be correctly linked"""

    def __init__(self, message: str):
        self.message = message
