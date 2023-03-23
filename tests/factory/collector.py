import subprocess
from collections.abc import Iterable, Mapping
from pathlib import Path
from tempfile import NamedTemporaryFile

from strictyaml import YAMLError, dirty_load

from .circuit_state import CircuitState
from .results import Case, Failure


class Collector:
    """Factory class for integration tests.

    Test cases consist out of next components:
        * a ``target`` folder, where cases will be searched;
        * ``target/architecture`` folders; note that `architecture` should match an
          existing arch of `cocas`;
        * a ``*.circ`` file for each architecture, which will be used for `logisim`
          integration test;
        * a set of folders with ``program.asm`` and ``state.yaml`` files for each arch.
    """
    _target: Path
    _cases: dict[str, tuple[Case] | tuple[Failure]]

    def __init__(self, target: Path) -> None:
        """Creates a ``Collector`` instance.

        Args:
            target:
                A folder, where all tests will be searched.
        """
        self._target = target
        self._cases = {}

    @property
    def raw_cases(self) -> Mapping[str, tuple[Case] | tuple[Failure]]:
        """Get the raw test cases representation.

        Returns:
            A mapping with names as keys and cases as values.
        """
        return self._cases

    @property
    def names(self) -> Iterable[str]:
        """Get the collected tests names.

        Returns:
            An iterable of strings.
        """
        return self._cases.keys()

    @property
    def cases(self) -> Iterable[tuple[Case] | tuple[Failure]]:
        """Get the collected tests themselves.

        Returns:
            An iterable of one-length tuples consisting of a ``Case`` or a ``Failure``.
        """
        return self._cases.values()

    @staticmethod
    def pass_to_cocas(arch: str, assembly_file: Path) -> str | None:
        """Send an assembly file to `cocas` and get, if possible, an image of it.

        Args:
            arch:
                The architecture of target processor.
            assembly_file:
                A path to assembly file.

        Returns:
            An image, if assembler exited gracefully, ``None`` otherwise.
        """
        image_file = NamedTemporaryFile(delete=False)
        image_file.close()

        process = subprocess.run([
            "cocas",
            "--target", arch,
            "--output", image_file.name,
            str(assembly_file)
        ], capture_output=True)

        return Path(image_file.name).read_text() if process.returncode == 0 else None

    def _extract_case(self, program: Path) -> Case | Failure:
        state = program.parent.parent / "output" / f"{program.stem}.yaml"

        if not program.exists():
            return Failure.MISSING_PROGRAM

        if not state.exists():
            return Failure.MISSING_STATE

        if (image := self.pass_to_cocas(program.parent.parent.name, program)) is None:
            return Failure.ASSEMBLER_FAIL

        try:
            dumped = state.read_text("UTF-8")
            loaded = dirty_load(dumped, CircuitState.schema(), allow_flow_style=True)
            circuit_state = CircuitState.load(loaded.data)
        except (YAMLError, ValueError):
            return Failure.STATE_RESOLVER_FAIL

        return Case(image, circuit_state)

    def collect(self) -> None:
        """Quite straight-forward: collect tests."""
        for arch_folder in self._target.iterdir():
            arch = arch_folder.name
            programs_dir = arch_folder / "input"
            for case_program in programs_dir.iterdir():
                case = case_program.stem
                self._cases[f"{arch}-{case}"] = (self._extract_case(case_program),)
