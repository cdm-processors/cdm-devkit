import importlib
from pathlib import Path
from typing import Protocol, runtime_checkable

from cocodump.base_types import DecodedSection


@runtime_checkable
class TargetDecoder(Protocol):
    def decode(self, image: bytearray, has_ivt: bool = False) -> DecodedSection: ...


def import_target_decoder(target_name: str) -> TargetDecoder:
    decoder_module = importlib.import_module(f"cocodump.targets.{target_name}.decoder")

    if isinstance(decoder_module, TargetDecoder):
        return decoder_module
    else:
        raise TypeError("Module is not a valid target decoder")


def list_target_decoders() -> list[str]:
    targets_dir = Path(__file__).parent / "targets"
    available_targets = list(map(lambda x: str(x.name), targets_dir.iterdir()))

    return available_targets


def normalize_target_name(name: str) -> str:
    return name.replace('-', '').lower()
