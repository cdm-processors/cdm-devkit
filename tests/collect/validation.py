import warnings
from collections.abc import Callable
from functools import wraps
from typing import TypeVar

import pytest

from .collected_tests import Image, Report
from .simulation_state import SimulationState

R = TypeVar("R")


class AssemblerWarning(Warning):
    pass


def validate_resources(
    func: Callable[[Image, SimulationState], R]
) -> Callable[[Image | Report, SimulationState | None], R]:
    @wraps(func)
    def wrapped_func(image: Image | Report, state: SimulationState | None) -> R:
        if isinstance(image, Report):
            warnings.warn(AssemblerWarning(f"\n{image.log.decode()}"))
            pytest.skip(
                f"cocas (return code = {image.return_code}) can't process "
                f"assembly file, check warnings for details"
            )

        if state is None:
            pytest.skip("simulation state does not match the schema")

        return func(image, state)

    return wrapped_func
