import pytest
from invariants import Invariant
from invariants.invariant import define_invariants_of_dict


@pytest.mark.parametrize(
    'dict_data, expected_result',
    [
        (
            {
                "name": "Wilfred Snow",
                "is_admin": True,
                "age": 25,
                "salary": 125.25,
                "workPosition": ""
            },
            {
                "name": Invariant.STRING_NOT_EMPTY,
                "is_admin": Invariant.LITERAL_BOOLEAN,
                "age": Invariant.NUMBER_INTEGER,
                "salary": Invariant.NUMBER_FLOAT,
                "workPosition": Invariant.STRING_EMPTY
            }
        ),
        (
            {
                "name": "Eva Kemp",
                "is_admin": False,
                "age": 16,
                "salary": None,
                "workPosition": "Developer"
            },
            {
                "name": Invariant.STRING_NOT_EMPTY,
                "is_admin": Invariant.LITERAL_BOOLEAN,
                "age": Invariant.NUMBER_INTEGER,
                "salary": Invariant.LITERAL_NULL,
                "workPosition": Invariant.STRING_NOT_EMPTY
            }
        ),
        (
            {},
            {}
        )
    ],
    ids=[
        'define_invariants_of_dict_on_user',
        'define_invariants_of_dict_on_user_with_none_value',
        'define_invariants_of_dict_on_empty_dict'
    ]
)
def test_define_invariants_of_dict_on_users(dict_data: dict, expected_result: dict):
    assert define_invariants_of_dict(dict_data) == expected_result
