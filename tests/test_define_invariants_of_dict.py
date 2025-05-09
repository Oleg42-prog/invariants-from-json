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
        'define_invariants_of_dict_on_flatten_objects',
        'define_invariants_of_dict_on_flatten_objects_with_none_value',
        'define_invariants_of_dict_on_empty_dict'
    ]
)
def test_define_invariants_of_dict_on_flatten_objects(dict_data: dict, expected_result: dict):
    assert define_invariants_of_dict(dict_data) == expected_result


@pytest.mark.parametrize(
    'dict_data, expected_result',
    [
        (
            {
                "name": "Wilfred Snow",
                "account": {
                    "loginAttempts": 3,
                    "isBlocked": False,
                    "lastPasswordChange": "2024-03-15",
                    "preferredLanguage": "ru"
                },
                "address": {
                    "city": "Moscow",
                    "street": "Lenina 1",
                    "zipCode": "123456",
                    "isVerified": True
                }
            },
            {
                "name": Invariant.STRING_NOT_EMPTY,
                "account": {
                    "loginAttempts": Invariant.NUMBER_INTEGER,
                    "isBlocked": Invariant.LITERAL_BOOLEAN,
                    "lastPasswordChange": Invariant.STRING_NOT_EMPTY,
                    "preferredLanguage": Invariant.STRING_NOT_EMPTY
                },
                "address": {
                    "city": Invariant.STRING_NOT_EMPTY,
                    "street": Invariant.STRING_NOT_EMPTY,
                    "zipCode": Invariant.STRING_NOT_EMPTY,
                    "isVerified": Invariant.LITERAL_BOOLEAN
                }
            }
        ),
        (
            {
                "name": "Eva Kemp",
                "account": {
                    "loginAttempts": 0,
                    "isBlocked": True,
                    "lastPasswordChange": None,
                    "preferredLanguage": "en"
                },
                "address": {
                    "city": "Saint Petersburg",
                    "street": "",
                    "zipCode": None,
                    "isVerified": False
                }
            },
            {
                "name": Invariant.STRING_NOT_EMPTY,
                "account": {
                    "loginAttempts": Invariant.NUMBER_INTEGER,
                    "isBlocked": Invariant.LITERAL_BOOLEAN,
                    "lastPasswordChange": Invariant.LITERAL_NULL,
                    "preferredLanguage": Invariant.STRING_NOT_EMPTY
                },
                "address": {
                    "city": Invariant.STRING_NOT_EMPTY,
                    "street": Invariant.STRING_EMPTY,
                    "zipCode": Invariant.LITERAL_NULL,
                    "isVerified": Invariant.LITERAL_BOOLEAN
                }
            }
        )
    ],
    ids=[
        'define_invariants_of_dict_on_nested_objects_depth_1',
        'define_invariants_of_dict_on_nested_objects_depth_1_with_none_value'
    ]
)
def test_define_invariants_of_dict_on_nested_objects_depth_1(dict_data: dict, expected_result: dict):
    assert define_invariants_of_dict(dict_data) == expected_result
