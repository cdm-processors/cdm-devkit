from pathlib import Path

from cocas.ple.types import PleImage


def test_idempotency() -> None:
    with open(Path(__file__).parent / "ple.bin", "rb") as file:
        loaded = PleImage.load(file)

    with open(Path(__file__).parent / "ple.bin", "rb") as file:
        assert PleImage.dumps(loaded) == file.read()
