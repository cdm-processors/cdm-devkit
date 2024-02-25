import importlib
from pathlib import Path

from .abstract_code_segments import IAlignedSegment, IAlignmentPaddingSegment, ICodeSegment, IVaryingLengthSegment
from .target_instructions_protocol import TargetInstructions


def list_assembler_targets() -> set[str]:
    """Returns a set of supported assembler targets. Takes submodules of assembler/target module"""
    targets_dir = Path(__file__).parent.absolute()
    targets = map(lambda x: x.name, filter(lambda x: x.is_dir(), targets_dir.glob("[!_]*")))
    return set(targets)


def import_target(target: str) -> TargetInstructions:
    module = importlib.import_module(f'.{target}', __package__)
    if isinstance(module, TargetInstructions):
        return module
    else:
        raise TypeError("Module is not a valid target")


def mlb_path(target: str) -> Path:
    return Path(__file__).parent / target / "standard.mlb"
