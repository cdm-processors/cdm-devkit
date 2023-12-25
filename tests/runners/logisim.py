import json
import subprocess
import warnings
from enum import IntEnum
from pathlib import Path
from tempfile import NamedTemporaryFile


import pytest

from .runner import RUNNER_TIMEOUT, ReturnCode
from ..factory import Case
from .runner_state import RunnerFailure, RunnerState


def execute_logisim_runner(program_img: Path, circuit_folder: Path, test_circuit: str) -> RunnerState | RunnerFailure:
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
