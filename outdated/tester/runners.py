import sys
import pathlib
# TODO: i don't know how to do imports properly
sys.path.append(str(pathlib.Path(__file__).parent.parent))
from abc import ABC, abstractmethod, abstractproperty
from enum import Enum
from subprocess import run, PIPE
import pathlib
from tempfile import NamedTemporaryFile
import json
import cdm_emu.emulator as emulator
import time
from state import CdmState
import os




class RunnerStatus(Enum):
    SUCCESS = "ok"
    TIMEOUT = "timeout"
    CRASH = "runner terminated with non-zero exit code"
    PARSE_ERROR = "failed to parse runner output"


class Runner(ABC):
    @abstractmethod
    def run(self, image_file: str, timeout: int) -> tuple[RunnerStatus, CdmState | None]:
        pass

    @property
    @abstractmethod
    def name(self) -> str:
        pass



class LogisimRunner(Runner):
    @property
    def name(self) -> str:
        return "Logisim"

    jar_path = pathlib.Path(__file__).parent.parent.joinpath(pathlib.Path("bin/logisim_runner.jar"))

    def run(self, image_file: str, timeout: int = 10000) -> tuple[RunnerStatus, CdmState | None]:
        result_file = NamedTemporaryFile(mode='r', delete=True)
        process = run(["java", "-jar", str(self.jar_path.absolute()), image_file, result_file.name, str(timeout)],
                      stdout=PIPE, stderr=PIPE)
        result_data = result_file.read()
        result_file.close()
        if process.returncode != 0:
            if "Timeout" in process.stdout.decode():
                return RunnerStatus.TIMEOUT, None
            else:
                return RunnerStatus.CRASH, None
        else:
            try:
                result: dict = json.loads(result_data)
                mem = result['mem']
                result.pop('mem')
                return RunnerStatus.SUCCESS, CdmState(result, mem, self.name)
            except (json.JSONDecodeError, KeyError):
                return RunnerStatus.PARSE_ERROR, None


class EmulatorRunner(Runner):
    @property
    def name(self) -> str:
        return "Emulator"

    def run(self, image_file: str, timeout: int = 10000) -> tuple[RunnerStatus, CdmState | None]:
        emu = emulator.CDM8Emu()
        emu.loadImg(image_file)
        start_time = time.time()
        while not emu.HALT:
            emu.step()
            if start_time + (timeout/1000) < time.time():
                return RunnerStatus.TIMEOUT, None

        # PC + 1 to match logisim's pc after halt
        regs = {
            'r0': emu.regs[0],
            'r1': emu.regs[1],
            'r2': emu.regs[2],
            'r3': emu.regs[3],
            'sp': emu.SP,
            'pc': (emu.PC + 1) % 2**16,
            'ps': emu.CVZN,
        }
        return RunnerStatus.SUCCESS, CdmState(regs, emu.datamem, self.name)
