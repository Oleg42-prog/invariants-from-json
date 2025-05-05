import pytest
from invariants import Invariant
from invariants.invariant import define_invariant_by_value


@pytest.mark.parametrize('int_value', [25, 0, -16])
def test_define_invariant_by_int_value(int_value: int):
    invariant = define_invariant_by_value(int_value)
    assert invariant == Invariant.NUMBER_INTEGER
