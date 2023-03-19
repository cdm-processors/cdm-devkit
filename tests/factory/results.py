from dataclasses import dataclass
from enum import Enum, auto

from .circuit_state import CircuitState


@dataclass
class Case:
    image: str
    circuit_state: CircuitState

    def unpack(self) -> tuple[str, CircuitState]:
        return self.image, self.circuit_state


class Failure(Enum):
    MISSING_PROGRAM = auto()
    MISSING_STATE = auto()
    ASSEMBLER_FAIL = auto()
    STATE_RESOLVER_FAIL = auto()
