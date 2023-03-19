from dataclasses import dataclass, field
from typing import Self, TypedDict

from strictyaml import HexInt, Int, Map, MapPattern, Optional, Str, Validator

from .memory import Memory, SerializedMemory


class SerializedCircuitState(TypedDict, total=False):
    """A ``TypedDict``, which describes serialized from of ``CircuitState``.

    Registers should be a dictionary with register names as keys and registers values as
    dictionary values.

    Memory should be a serialized form of ``Memory`` instance.

    Maximal ticks is an int value, which restricts the time of program execution.

    Notice that all requirements are optional, so if you really want you can create an
    empty specification.
    """
    registers: dict[str, int]
    memory: SerializedMemory
    max_ticks: int


@dataclass
class CircuitState:
    """Describes state of the circuit at the end of program execution."""
    registers: dict[str, int] = field(default_factory=dict)
    memory: Memory = field(default_factory=Memory)
    max_ticks: int | None = None

    @staticmethod
    def schema() -> Validator:
        """A ``strictyaml.Validator`` schema for state loading from YAML document.

        Returns:
            The YAML schema for user-defined circuit state.
        """
        return Map({
            Optional("registers"): MapPattern(Str(), Int() | HexInt()),
            Optional("memory"): Memory.schema(),
            Optional("max_ticks"): Int(),
        })

    @classmethod
    def load(cls, state: SerializedCircuitState) -> Self:
        """Creates a ``CircuitState`` instance from serialized state.

        Args:
            state:
                A serialized ``CircuitState``. Check ``SerializedCircuitState`` for
                additional information.

        Returns:
            A ``CircuitState`` instance.

        Raises:
            ValueError:
                If memory resolving failed.
        """
        if "memory" in state:
            state["memory"] = Memory.resolve(state["memory"])  # type: ignore

        return cls(**state)
