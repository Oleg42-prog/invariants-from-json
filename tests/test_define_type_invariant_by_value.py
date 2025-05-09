from typing import Any
import pytest
from invariants import TypeInvariant
from invariants.type_invariants import define_type_invariant_by_value


@pytest.mark.parametrize(
    'int_value',
    [25, 0, -16],
    ids=[
        'define_type_invariant_by_int_value_positive',
        'define_type_invariant_by_int_value_zero',
        'define_type_invariant_by_int_value_negative'
    ]
)
def test_define_type_invariant_by_int_value(int_value: int):
    invariant = define_type_invariant_by_value(int_value)
    assert invariant == TypeInvariant.NUMBER_INTEGER


@pytest.mark.parametrize(
    'float_value',
    [125.25, 0.00, -125.25, 4.0, -4.0],
    ids=[
        'define_type_invariant_by_float_value_positive',
        'define_type_invariant_by_float_value_zero',
        'define_type_invariant_by_float_value_negative',
        'define_type_invariant_by_float_value_positive_with_zero_after_dot',
        'define_type_invariant_by_float_value_negative_with_zero_after_dot'
    ]
)
def test_define_type_invariant_by_float_value(float_value: float):
    invariant = define_type_invariant_by_value(float_value)
    assert invariant == TypeInvariant.NUMBER_FLOAT


def test_define_type_invariant_by_empty_string_value():
    invariant = define_type_invariant_by_value('')
    assert invariant == TypeInvariant.STRING_EMPTY


def test_define_type_invariant_by_not_empty_string_value():
    invariant = define_type_invariant_by_value('Hello, world!')
    assert invariant == TypeInvariant.STRING_NOT_EMPTY


@pytest.mark.parametrize(
    'boolean_value',
    [True, False],
    ids=['define_type_invariant_by_boolean_value_true', 'define_type_invariant_by_boolean_value_false']
)
def test_define_type_invariant_by_boolean_value(boolean_value: bool):
    invariant = define_type_invariant_by_value(boolean_value)
    assert invariant == TypeInvariant.LITERAL_BOOLEAN


def test_define_type_invariant_by_none_value():
    invariant = define_type_invariant_by_value(None)
    assert invariant == TypeInvariant.LITERAL_NULL


@pytest.mark.parametrize(
    'unknown_value',
    [
        [],
        {},
        (1, 2, 3),
    ],
    ids=[
        'define_type_invariant_by_unknown_value_list',
        'define_type_invariant_by_unknown_value_dict',
        'define_type_invariant_by_unknown_value_tuple'
    ]
)
def test_define_type_invariant_by_unknown_value(unknown_value: Any):
    with pytest.raises(ValueError):
        define_type_invariant_by_value(unknown_value)
