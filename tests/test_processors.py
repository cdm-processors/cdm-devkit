from pathlib import Path
from typing import ClassVar

import pytest
from _pytest.python import Metafunc

from .factory import Case, Collector, skip_invalid_cases


def pytest_generate_tests(metafunc: Metafunc):
    cls = metafunc.cls

    if cls.collected is None:
        cls.collected = Collector(cls.resources)
        cls.collected.collect()

    arg_specs = cls.arg_specs
    cases = cls.collected.cases
    names = cls.collected.names

    if "logisim_emulator" in metafunc.function.__name__:
        raw_cases = cls.collected.raw_cases

        has_circuits = {
            arch.name: (arch / "circuit" / "test_circuit.circ").exists()
            for arch in cls.resources.iterdir()
        }

        filtered_cases = {}
        for name, case in raw_cases.items():
            arch, *_ = name.split("-")
            if has_circuits[arch]:
                filtered_cases[name] = (*case, cls.resources / arch / "circuit")

        arg_specs = arg_specs + ["circuit_folder"]
        cases = filtered_cases.values()
        if not filtered_cases:
            names = ["no-logisim-compatible-targets"]
        else:
            names = filtered_cases.keys()

    metafunc.parametrize(arg_specs, cases, ids=names)


class TestProcessors:
    resources: ClassVar[Path] = Path(__file__).parent / "resources"
    arg_specs: ClassVar[list[str]] = ["case"]
    collected: ClassVar[Collector | None] = None

    @skip_invalid_cases
    def test_logisim_scheme(self, case: Case) -> None:
        image, circuit_state = case.unpack()

        ...

    @skip_invalid_cases
    def test_logisim_emulator(self, case: Case, circuit_folder: Path) -> None:
        image, circuit_state = case.unpack()

        ...

    @pytest.mark.skip(reason="cocoemu is not implemented yet")
    @skip_invalid_cases
    def test_python_emulator(self, case: Case) -> None:
        image, circuit_state = case.unpack()

        ...
