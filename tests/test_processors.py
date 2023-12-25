from pathlib import Path
from typing import ClassVar

from _pytest.python import Metafunc

from .factory import Case, Collector, skip_invalid_cases
from .runners import run_test, execute_logisim_runner, execute_emulator_runner

LOGISIM_NATIVE_TEST_CIRCUIT = "test_circuit.circ"
LOGISIM_EMULATOR_TEST_CIRCUIT = "test_circuit_emu.circ"


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

        has_circuits = None

        if "logisim_scheme" in metafunc.function.__name__:
            has_circuits = {
                arch.name: (arch / "circuits" / LOGISIM_NATIVE_TEST_CIRCUIT).exists()
                for arch in cls.resources.iterdir()
            }

        elif "logisim_emulator" in metafunc.function.__name__:
            has_circuits = {
                arch.name: (arch / "circuits" / LOGISIM_EMULATOR_TEST_CIRCUIT).exists()
                for arch in cls.resources.iterdir()
            }

        filtered_cases = {}
        for name, case in raw_cases.items():
            arch, *_ = name.split("-")
            if has_circuits[arch]:
                filtered_cases[name] = (*case, cls.resources / arch / "circuits")

        arg_specs = arg_specs + ["circuit_folder"]
        cases = filtered_cases.values()
        if not filtered_cases:
            names = ["no-logisim-compatible-targets"]
        else:
            names = filtered_cases.keys()
    elif 'standalone' in metafunc.function.__name__:
        raw_cases = cls.collected.raw_cases

        filtered_cases = {}
        for name, case in raw_cases.items():
            arch, *_ = name.split("-")
            if arch == 'cdm16':
                filtered_cases[name] = (*case,)

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
    def test_logisim_scheme(self, case: Case, circuit_folder: Path) -> None:
        run_test(case, lambda img: execute_logisim_runner(img, circuit_folder, LOGISIM_NATIVE_TEST_CIRCUIT))

    @skip_invalid_cases
    def test_logisim_emulator(self, case: Case, circuit_folder: Path) -> None:
        run_test(case, lambda img: execute_logisim_runner(img, circuit_folder, LOGISIM_EMULATOR_TEST_CIRCUIT))

    @skip_invalid_cases
    def test_standalone_emulator(self, case: Case) -> None:
        run_test(case, lambda img: execute_emulator_runner(img))
