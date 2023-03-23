from pathlib import Path
from typing import ClassVar

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

    if "logisim" in metafunc.function.__name__:
        raw_cases = cls.collected.raw_cases

        has_circuits = {
            arch.name: (arch / "circuits").exists()
            for arch in cls.resources.iterdir()
        }

        filtered_cases = {}
        for name, case in raw_cases.items():
            arch, *_ = name.split("-")
            if has_circuits[arch]:
                filtered_cases[name] = (*case, cls.resources / arch / "circuits")

        arg_specs = arg_specs + ["circuits"]
        cases = filtered_cases.values()
        names = filtered_cases.keys()

    metafunc.parametrize(arg_specs, cases, ids=names)


class TestEmulators:
    resources: ClassVar[Path] = Path(__file__).parent / "resources"
    arg_specs: ClassVar[list[str]] = ["case"]
    collected: ClassVar[Collector | None] = None

    @skip_invalid_cases
    def test_python(self, case: Case) -> None:
        image, circuit_state = case.unpack()

        ...

    @skip_invalid_cases
    def test_logisim(self, case: Case, circuits: Path) -> None:
        image, circuit_state = case.unpack()
        ...
