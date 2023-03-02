import subprocess
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable, TypeAlias, TypedDict

from .simulation_state import SimulationState

Image: TypeAlias = bytes
Architecture: TypeAlias = str
Name: TypeAlias = str


@dataclass
class Report:
    return_code: int
    log: bytes


class CollectedTests(TypedDict):
    argvalues: Iterable[tuple[Image | Report, SimulationState | None]]
    ids: Iterable[Name]


def pass_to_cocas(target: str, assembly_file: Path) -> Image | Report:
    image = subprocess.run(["cocas", "-t", target, str(assembly_file)], capture_output=True)

    if image.returncode == 0:
        return image.stdout
    else:
        return Report(image.returncode, image.stdout)


def get_output_file(assembly_file: Path) -> Path:
    return assembly_file.parent.parent / "output" / f"{assembly_file.stem}.yaml"


def collect_tests() -> CollectedTests:
    resources = Path(__file__).parent.parent / "resources"
    sets: list[tuple[Image | Report, SimulationState | None]] = []
    names: list[str] = []

    for arch_folder in resources.iterdir():
        arch = arch_folder.name
        for assembly_file in (arch_folder / "input").iterdir():
            test = assembly_file.stem
            report = pass_to_cocas(arch, assembly_file)
            state = SimulationState.load(get_output_file(assembly_file))

            sets.append((report, state))
            names.append(f"{arch}-{test}")

    return {"argvalues": sets, "ids": names}
