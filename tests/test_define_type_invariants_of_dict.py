import pytest
from invariants import TypeInvariant
from invariants.type_invariants import define_type_invariants_of_dict


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
                "name": TypeInvariant.STRING_NOT_EMPTY,
                "is_admin": TypeInvariant.LITERAL_BOOLEAN,
                "age": TypeInvariant.NUMBER_INTEGER,
                "salary": TypeInvariant.NUMBER_FLOAT,
                "workPosition": TypeInvariant.STRING_EMPTY
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
                "name": TypeInvariant.STRING_NOT_EMPTY,
                "is_admin": TypeInvariant.LITERAL_BOOLEAN,
                "age": TypeInvariant.NUMBER_INTEGER,
                "salary": TypeInvariant.LITERAL_NULL,
                "workPosition": TypeInvariant.STRING_NOT_EMPTY
            }
        ),
        (
            {},
            {}
        )
    ],
    ids=[
        'define_type_invariants_of_dict_on_flatten_objects',
        'define_type_invariants_of_dict_on_flatten_objects_with_none_value',
        'define_type_invariants_of_dict_on_empty_dict'
    ]
)
def test_define_type_invariants_of_dict_on_flatten_objects(dict_data: dict, expected_result: dict):
    assert define_type_invariants_of_dict(dict_data) == expected_result


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
                "name": TypeInvariant.STRING_NOT_EMPTY,
                "account": {
                    "loginAttempts": TypeInvariant.NUMBER_INTEGER,
                    "isBlocked": TypeInvariant.LITERAL_BOOLEAN,
                    "lastPasswordChange": TypeInvariant.STRING_NOT_EMPTY,
                    "preferredLanguage": TypeInvariant.STRING_NOT_EMPTY
                },
                "address": {
                    "city": TypeInvariant.STRING_NOT_EMPTY,
                    "street": TypeInvariant.STRING_NOT_EMPTY,
                    "zipCode": TypeInvariant.STRING_NOT_EMPTY,
                    "isVerified": TypeInvariant.LITERAL_BOOLEAN
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
                "name": TypeInvariant.STRING_NOT_EMPTY,
                "account": {
                    "loginAttempts": TypeInvariant.NUMBER_INTEGER,
                    "isBlocked": TypeInvariant.LITERAL_BOOLEAN,
                    "lastPasswordChange": TypeInvariant.LITERAL_NULL,
                    "preferredLanguage": TypeInvariant.STRING_NOT_EMPTY
                },
                "address": {
                    "city": TypeInvariant.STRING_NOT_EMPTY,
                    "street": TypeInvariant.STRING_EMPTY,
                    "zipCode": TypeInvariant.LITERAL_NULL,
                    "isVerified": TypeInvariant.LITERAL_BOOLEAN
                }
            }
        )
    ],
    ids=[
        'define_type_invariants_of_dict_on_nested_objects_depth_1',
        'define_type_invariants_of_dict_on_nested_objects_depth_1_with_none_value'
    ]
)
def test_define_type_invariants_of_dict_on_nested_objects_depth_1(dict_data: dict, expected_result: dict):
    assert define_type_invariants_of_dict(dict_data) == expected_result


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
                    "preferredLanguage": "ru",
                    "address": {
                        "city": "Moscow",
                        "street": "Lenina 1",
                        "zipCode": "123456",
                        "isVerified": True
                    }
                }
            },
            {
                "name": TypeInvariant.STRING_NOT_EMPTY,
                "account": {
                    "loginAttempts": TypeInvariant.NUMBER_INTEGER,
                    "isBlocked": TypeInvariant.LITERAL_BOOLEAN,
                    "lastPasswordChange": TypeInvariant.STRING_NOT_EMPTY,
                    "preferredLanguage": TypeInvariant.STRING_NOT_EMPTY,
                    "address": {
                        "city": TypeInvariant.STRING_NOT_EMPTY,
                        "street": TypeInvariant.STRING_NOT_EMPTY,
                        "zipCode": TypeInvariant.STRING_NOT_EMPTY,
                        "isVerified": TypeInvariant.LITERAL_BOOLEAN
                    }
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
                    "preferredLanguage": "en",
                    "address": {
                        "city": "Saint Petersburg",
                        "street": "",
                        "zipCode": None,
                        "isVerified": False
                    }
                }
            },
            {
                "name": TypeInvariant.STRING_NOT_EMPTY,
                "account": {
                    "loginAttempts": TypeInvariant.NUMBER_INTEGER,
                    "isBlocked": TypeInvariant.LITERAL_BOOLEAN,
                    "lastPasswordChange": TypeInvariant.LITERAL_NULL,
                    "preferredLanguage": TypeInvariant.STRING_NOT_EMPTY,
                    "address": {
                        "city": TypeInvariant.STRING_NOT_EMPTY,
                        "street": TypeInvariant.STRING_EMPTY,
                        "zipCode": TypeInvariant.LITERAL_NULL,
                        "isVerified": TypeInvariant.LITERAL_BOOLEAN
                    }
                }
            }
        )
    ],
    ids=[
        'define_type_invariants_of_dict_on_nested_objects_depth_2',
        'define_type_invariants_of_dict_on_nested_objects_depth_2_with_none_value'
    ]
)
def test_define_type_invariants_of_dict_on_nested_objects_depth_2(dict_data: dict, expected_result: dict):
    assert define_type_invariants_of_dict(dict_data) == expected_result
