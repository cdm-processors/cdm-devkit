from dataclasses import dataclass


@dataclass
class RunnerState:
    registers: dict[str, int]
    memory: list[int]
    ticks: int


@dataclass
class RunnerFailure:
    return_code: int
    stderr: str
