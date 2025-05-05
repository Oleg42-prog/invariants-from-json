import pytest
from invariants import Invariant
from invariants.invariant import define_invariant_by_value


@pytest.mark.parametrize('int_value', [25, 0, -16])
def test_define_invariant_by_int_value(int_value: int):
    invariant = define_invariant_by_value(int_value)
    assert invariant == Invariant.NUMBER_INTEGER


@pytest.mark.parametrize('float_value', [125.25, 0.00, -125.25, 4.0, -4.0])
def test_define_invariant_by_float_value(float_value: float):
    invariant = define_invariant_by_value(float_value)
    assert invariant == Invariant.NUMBER_FLOAT
