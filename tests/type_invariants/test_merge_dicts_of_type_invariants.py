from invariants import TypeInvariant
from invariants.merge import merge_dicts_of_invariants


def test_merge_dicts_of_type_invariants_on_flatten_objects():

    data = [
        {
            "name": TypeInvariant.STRING_NOT_EMPTY,
            "is_admin": TypeInvariant.LITERAL_BOOLEAN,
            "age": TypeInvariant.NUMBER_INTEGER,
            "salary": TypeInvariant.NUMBER_FLOAT,
            "workPosition": TypeInvariant.STRING_EMPTY
        },
        {
            "name": TypeInvariant.STRING_NOT_EMPTY,
            "is_admin": TypeInvariant.LITERAL_BOOLEAN,
            "age": TypeInvariant.NUMBER_INTEGER,
            "salary": TypeInvariant.LITERAL_NULL,
            "workPosition": TypeInvariant.STRING_NOT_EMPTY
        },
        {
            "name": TypeInvariant.STRING_NOT_EMPTY,
            "is_admin": TypeInvariant.LITERAL_BOOLEAN,
            "age": TypeInvariant.NUMBER_INTEGER,
            "salary": TypeInvariant.NUMBER_INTEGER,
            "workPosition": TypeInvariant.STRING_EMPTY
        }
    ]

    expected_result = {
        'name': {TypeInvariant.STRING_NOT_EMPTY},
        'is_admin': {TypeInvariant.LITERAL_BOOLEAN},
        'age': {TypeInvariant.NUMBER_INTEGER},
        'salary': {TypeInvariant.NUMBER_FLOAT, TypeInvariant.LITERAL_NULL, TypeInvariant.NUMBER_INTEGER},
        'workPosition': {TypeInvariant.STRING_EMPTY, TypeInvariant.STRING_NOT_EMPTY}
    }

    actual_result = merge_dicts_of_invariants(*data)
    assert actual_result == expected_result


def test_merge_dicts_of_type_invariants_on_nested_objects_depth_1():
    data = [
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
                "zipCode": TypeInvariant.STRING_NOT_EMPTY
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
                "zipCode": TypeInvariant.LITERAL_NULL
            }
        }
    ]

    expected_result = {
        'name': {TypeInvariant.STRING_NOT_EMPTY},
        'account': {
            'loginAttempts': {TypeInvariant.NUMBER_INTEGER},
            'isBlocked': {TypeInvariant.LITERAL_BOOLEAN},
            'lastPasswordChange': {TypeInvariant.STRING_NOT_EMPTY, TypeInvariant.LITERAL_NULL},
            'preferredLanguage': {TypeInvariant.STRING_NOT_EMPTY}
        },
        'address': {
            'city': {TypeInvariant.STRING_NOT_EMPTY},
            'street': {TypeInvariant.STRING_EMPTY, TypeInvariant.STRING_NOT_EMPTY},
            'zipCode': {TypeInvariant.STRING_NOT_EMPTY, TypeInvariant.LITERAL_NULL}
        }
    }

    actual_result = merge_dicts_of_invariants(*data)
    assert actual_result == expected_result


def test_merge_dicts_of_type_invariants_on_nested_objects_depth_2():
    data = [
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
                    "zipCode": TypeInvariant.STRING_NOT_EMPTY
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
                    "zipCode": TypeInvariant.LITERAL_NULL
                }
            }
        }
    ]

    expected_result = {
        'name': {TypeInvariant.STRING_NOT_EMPTY},
        'account': {
            'loginAttempts': {TypeInvariant.NUMBER_INTEGER},
            'isBlocked': {TypeInvariant.LITERAL_BOOLEAN},
            'lastPasswordChange': {TypeInvariant.STRING_NOT_EMPTY, TypeInvariant.LITERAL_NULL},
            'preferredLanguage': {TypeInvariant.STRING_NOT_EMPTY},
            'address': {
                'city': {TypeInvariant.STRING_NOT_EMPTY},
                'street': {TypeInvariant.STRING_EMPTY, TypeInvariant.STRING_NOT_EMPTY},
                'zipCode': {TypeInvariant.STRING_NOT_EMPTY, TypeInvariant.LITERAL_NULL}
            }
        }
    }

    actual_result = merge_dicts_of_invariants(*data)
    assert actual_result == expected_result
