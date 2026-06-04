import importlib
from pathlib import Path

from cocas.assembler.target_parser import TargetInfo

from .abstract_code_segments import IAlignedSegment, IAlignmentPaddingSegment, ICodeSegment, IVaryingLengthSegment
from .target_instructions_protocol import TargetInstructions


def list_assembler_targets() -> set[str]:
    """Returns a set of supported assembler targets. Takes submodules of assembler/target module"""
    targets_dir = Path(__file__).parent.absolute()
    targets = map(lambda x: x.name, filter(lambda x: x.is_dir(), targets_dir.glob("[!_]*")))
    return set(targets)

def list_target_extensions(target: str) -> set[str]:
    """Returns a set of supported target extensions"""
    base_dir = Path(__file__).parent / target / "extensions"
    if not base_dir.exists() or not base_dir.is_dir():
        return set()  # target has no extensions directory
    extensions = map(
        lambda x: x.name,
        filter(lambda x: x.is_dir(), base_dir.glob("[!_]*"))
    )
    return set(extensions)

def load_extensions(target: TargetInfo):
    all_handlers = []
    for ext in target.extensions:
        mod = importlib.import_module(f".{ext}.target_instructions",
                            package=f"cocas.assembler.targets.{target.base}.extensions")
        all_handlers.extend(mod.handlers)
    return all_handlers

def import_target(target: TargetInfo) -> TargetInstructions:
    module = importlib.import_module(f'.{target.base}', __package__)
    base_handlers = module.handlers

    if target.extensions:
        ext_handlers = load_extensions(target)

        merged_map = {}
        for h in base_handlers:
            merged_map.setdefault(h.handler, {}).update(h.instructions)
        for h in ext_handlers:
            merged_map.setdefault(h.handler, {}).update(h.instructions)

        from cocas.assembler.targets.cdm16.target_instructions import Handler
        merged_handlers = [Handler(handler_callable, instr_dict)
                        for handler_callable, instr_dict in merged_map.items()]
        module.update_handlers(merged_handlers)

    if isinstance(module, TargetInstructions):
        return module
    else:
        raise TypeError("Module is not a valid target")


def standard_mlb(target: str) -> Path:
    return Path(__file__).parent / target / "standard.mlb"
