import json
import subprocess
import warnings
from enum import IntEnum
from pathlib import Path
from tempfile import NamedTemporaryFile


import pytest

from ..factory import Case
from .runner import RUNNER_TIMEOUT, ReturnCode
from .runner_state import RunnerFailure, RunnerState


def execute_emulator_runner(program_img: Path) -> RunnerState | RunnerFailure:
    output_image = NamedTemporaryFile(delete=False)
    output_image.close()

    process = subprocess.run(
        [
            "java", "-jar", Path(__file__).parent.parent / "resources" / "cdm16" / "circuits" / "standalone-all.jar",
            program_img.absolute(),
            output_image.name,
            str(RUNNER_TIMEOUT)
        ],
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
