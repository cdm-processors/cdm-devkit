from collections.abc import Callable
from functools import wraps
from typing import TypeVar

import pytest

from .collector import Case, Failure

R = TypeVar("R")


def skip_invalid_cases(
    test_routine: Callable[[Case], R]
) -> Callable[[Case | Failure], R]:
    @wraps(test_routine)
    def wrapped_routine(*args, **kwargs) -> R:
        case = kwargs["case"]

        match case:
            case Failure.MISSING_PROGRAM:
                return pytest.skip("assembly file is missing")
            case Failure.MISSING_STATE:
                return pytest.skip("circuit state specification is missing")
            case Failure.ASSEMBLER_FAIL:
                return pytest.skip("assembly file contains invalid code")
            case Failure.STATE_RESOLVER_FAIL:
                return pytest.skip("circuit state specification parsing failed")
            case _:
                return test_routine(*args, **kwargs)

    return wrapped_routine
