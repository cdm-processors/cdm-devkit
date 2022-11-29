from dataclasses import dataclass


@dataclass
class CodeLocation:
    file: str = "unknown"
    line: int = 0
    column: int = 0
