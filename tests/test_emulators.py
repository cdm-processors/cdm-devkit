from pathlib import Path
from typing import ClassVar

from _pytest.python import Metafunc

from .factory import Case, Collector, skip_invalid_cases


def pytest_generate_tests(metafunc: Metafunc):
    cls = metafunc.cls

    if cls.collected is None:
        cls.collected = Collector(cls.resources)
        cls.collected.collect()

    metafunc.parametrize(cls.arg_specs, cls.collected.cases, ids=cls.collected.names)


class TestEmulators:
    resources: ClassVar[Path] = Path(__file__).parent / "resources"
    arg_specs: ClassVar[list[str]] = ["case"]
    collected: ClassVar[Collector | None] = None

    @skip_invalid_cases
    def test_python(self, case: Case) -> None:
        image, circuit_state = case.unpack()

        ...

    @skip_invalid_cases
    def test_logisim(self, case: Case) -> None:
        image, circuit_state = case.unpack()

        ...
