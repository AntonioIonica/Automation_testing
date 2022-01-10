import pytest
from utils.accumulator import Accumulator


# Fixtures (a function which always has to return something)

@pytest.fixture(autouse=True)
def accum():
    return Accumulator()
