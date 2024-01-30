import importlib
from pathlib import Path

from .abstract_code_segments import IAlignedSegment, IAlignmentPaddingSegment, ICodeSegment, IVaryingLengthSegment
from .abstract_instructions import TargetInstructionsInterface


def list_assembler_targets() -> set[str]:
    targets_dir = Path(__file__).parent.absolute()
    targets = map(lambda x: x.name, filter(lambda x: x.is_dir(), targets_dir.glob("[!_]*")))
    return set(targets)


def import_target(target: str) -> TargetInstructionsInterface:
    module = importlib.import_module(f'.{target}', __package__)
    return module.TargetInstructions


def mlb_path(target: str) -> Path:
    return Path(__file__).parent / target / "standard.mlb"
