from dataclasses import dataclass, field


@dataclass
class CdmState:
    regs: dict[str, int]
    mem: list[int]
    runner_name: str = field(compare=False)