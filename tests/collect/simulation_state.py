from dataclasses import dataclass, field
from pathlib import Path
from typing import Optional

import strictyaml
from strictyaml import HexInt, Int, Map, MapPattern, Str, Validator
from strictyaml import Optional as OptionalKey


@dataclass
class SimulationState:
    registers: dict[str, int] = field(default_factory=dict)
    memory: dict[int, int] = field(default_factory=dict)
    max_ticks: int | None = None

    @staticmethod
    def schema() -> Validator:
        return Map({
            OptionalKey("registers"): MapPattern(Str(), Int() | HexInt()),
            OptionalKey("memory"): MapPattern(HexInt(), Int() | HexInt()),
            OptionalKey("max_ticks"): Int(),
        })

    @classmethod
    def load(cls, yaml_file: Path) -> Optional["SimulationState"]:
        yaml_document = yaml_file.read_text(encoding="UTF-8")

        try:
            loaded_yaml = strictyaml.load(yaml_document, cls.schema())
        except strictyaml.YAMLError:
            return None

        return cls(**loaded_yaml.data)
