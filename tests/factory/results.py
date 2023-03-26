from dataclasses import dataclass
from enum import Enum, auto
from pathlib import Path

from .circuit_state import CircuitState


@dataclass
class Case:
    image_file: Path
    circuit_state: CircuitState

    def unpack(self) -> tuple[Path, CircuitState]:
        return self.image_file, self.circuit_state


class Failure(Enum):
    MISSING_PROGRAM = auto()
    MISSING_STATE = auto()
    ASSEMBLER_FAIL = auto()
    STATE_RESOLVER_FAIL = auto()
