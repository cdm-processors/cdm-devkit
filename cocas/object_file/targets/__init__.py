import json
from dataclasses import dataclass
from pathlib import Path


def list_object_targets() -> set[str]:
    """Returns a set of supported object file targets. Takes files from of object_file/target module"""
    targets_dir = Path(__file__).parent.absolute()
    targets = map(lambda x: x.name[:-5], targets_dir.glob("*.json"))
    return set(targets)


@dataclass
class TargetParams:
    name: str
    header: str
    default_alignment: int
    max_entry_size: int


def import_target(target: str) -> TargetParams:
    path = Path(__file__).parent / (target + '.json')
    with path.open('r') as f:
        return json.load(f, object_hook=lambda d: TargetParams(**d))
