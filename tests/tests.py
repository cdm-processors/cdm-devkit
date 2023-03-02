import pytest

from .collect import Image, SimulationState, collect_tests, validate_resources


@validate_resources
@pytest.mark.parametrize(["image", "state"], **collect_tests())
def test_via_emulator(image: Image, state: SimulationState):  # TODO
    assert True


@validate_resources
@pytest.mark.parametrize(["image", "state"], **collect_tests())
def test_via_logisim(image: Image, state: SimulationState):  # TODO
    assert True
