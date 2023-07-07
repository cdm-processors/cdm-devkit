import importlib
from collections.abc import Callable
from pathlib import Path

from cocodump.base_types import DecodedSection


class TargetDecoder:
    _decode_func: Callable[[bytearray], DecodedSection]

    def __init__(self, func: Callable[[bytearray], DecodedSection]) -> None:
        self._decode_func = func

    def decode(self, image: bytearray) -> DecodedSection:
        return self._decode_func(image)


def import_target_decoder(target_name: str):
    decoder_func = \
        importlib.import_module(f"cocodump.targets.{target_name}.decoder").decode

    return TargetDecoder(decoder_func)


def list_target_decoders() -> list[str]:
    # TODO: check target
    targets_dir = Path(__file__).parent / "targets"
    available_targets = list(map(lambda x: str(x.name), targets_dir.iterdir()))

    return available_targets


def normalize_target_name(name: str) -> str:
    return name.replace('-', '').lower()
