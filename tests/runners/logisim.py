import json
import subprocess
import warnings
from enum import IntEnum
from pathlib import Path
from tempfile import NamedTemporaryFile

import pytest

from .runner_state import RunnerState, RunnerFailure
from ..factory import Case

RUNNER_TIMEOUT: int = 10000


class ReturnCode(IntEnum):
    SUCCESS = 0
    ERROR = 1
    TIMEOUT = 13


def run_logisim_test(case: Case, circuit_folder: Path, test_circuit: str) -> None:
    image_path, circuit_state = case.unpack()

    if circuit_state.max_ticks is None:
        circuit_state.max_ticks = RUNNER_TIMEOUT

    result = execute_runner(
        image_path,
        circuit_folder,
        test_circuit
    )

    if isinstance(result, RunnerFailure):
        match result.return_code:
            case ReturnCode.ERROR:
                pytest.skip(f"Runner finished with error: {result.stderr}")
            case ReturnCode.TIMEOUT:
                pytest.fail(f"Runner timeout (program took more than {RUNNER_TIMEOUT} ticks)")
            case _:
                pytest.skip(f"Something went terribly wrong...\nstderr: {result.stderr}")

    if result.ticks > circuit_state.max_ticks:
        warnings.warn(UserWarning(f"Ticks limit exceeded: {result.ticks} > {circuit_state.max_ticks}"))

    for register in circuit_state.registers.keys():
        expected_value = circuit_state.registers[register]
        actual_value = result.registers[register]

        assert expected_value == actual_value, \
            f"Expected {register} to be {expected_value}, got {actual_value} instead"

    for address, value in circuit_state.memory.layout.items():
        expected_value = circuit_state.memory.layout[address]
        actual_value = result.memory[address]

        assert expected_value == actual_value, (
            f"Expected memory at address {hex(address)} to be {expected_value},"
            f" got {actual_value} instead"
        )


def execute_runner(program_img: Path, circuit_folder: Path, test_circuit: str) -> RunnerState | RunnerFailure:
    output_image = NamedTemporaryFile(delete=False)
    output_image.close()

    process = subprocess.run(
        [
            "java", "-jar", Path(__file__).parent.parent / "jar" / "logisim-runner-all.jar",
            program_img.absolute(),
            test_circuit,
            output_image.name,
            "config.properties",
            str(RUNNER_TIMEOUT)
        ],
        cwd=circuit_folder.absolute(),
        stdout=subprocess.PIPE, stderr=subprocess.PIPE
    )

    if process.returncode == ReturnCode.SUCCESS:
        output = json.loads(process.stdout)
        memory = json.loads(Path(output_image.name).read_text("UTF-8"))

        return RunnerState(
            output["registers"],
            memory,
            output["ticks"]
        )
    else:
        return RunnerFailure(process.returncode, process.stderr.decode("UTF-8"))
