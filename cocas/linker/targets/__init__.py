import json
from dataclasses import dataclass
from pathlib import Path


def list_linker_targets() -> set[str]:
    """Returns a set of supported linker targets. Takes files from of linker/target module"""
    targets_dir = Path(__file__).parent.absolute()
    targets = map(lambda x: x.name[:-5], targets_dir.glob("*.json"))
    return set(targets)


@dataclass
class TargetParams:
    name: str
    image_size: int


def import_target(target: str) -> TargetParams:
    path = Path(__file__).parent / (target + '.json')
    with path.open('r') as f:
        return json.load(f, object_hook=lambda d: TargetParams(**d))
