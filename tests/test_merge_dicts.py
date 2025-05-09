from invariants import Invariant
from invariants.invariant import merge_dicts


def test_merge_dicts():

    data = [
        {
            "name": Invariant.STRING_NOT_EMPTY,
            "is_admin": Invariant.LITERAL_BOOLEAN,
            "age": Invariant.NUMBER_INTEGER,
            "salary": Invariant.NUMBER_FLOAT,
            "workPosition": Invariant.STRING_EMPTY
        },
        {
            "name": Invariant.STRING_NOT_EMPTY,
            "is_admin": Invariant.LITERAL_BOOLEAN,
            "age": Invariant.NUMBER_INTEGER,
            "salary": Invariant.LITERAL_NULL,
            "workPosition": Invariant.STRING_NOT_EMPTY
        },
        {
            "name": Invariant.STRING_NOT_EMPTY,
            "is_admin": Invariant.LITERAL_BOOLEAN,
            "age": Invariant.NUMBER_INTEGER,
            "salary": Invariant.NUMBER_INTEGER,
            "workPosition": Invariant.STRING_EMPTY
        }
    ]

    expected_result = {
        'name': {Invariant.STRING_NOT_EMPTY},
        'is_admin': {Invariant.LITERAL_BOOLEAN},
        'age': {Invariant.NUMBER_INTEGER},
        'salary': {Invariant.NUMBER_FLOAT, Invariant.LITERAL_NULL, Invariant.NUMBER_INTEGER},
        'workPosition': {Invariant.STRING_EMPTY, Invariant.STRING_NOT_EMPTY}
    }

    actual_result = merge_dicts(*data)
    assert actual_result == expected_result


def test_merge_dicts_on_nested_objects_depth_1():
    data = [
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
                "zipCode": Invariant.STRING_NOT_EMPTY
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
                "zipCode": Invariant.LITERAL_NULL
            }
        }
    ]

    expected_result = {
        'name': {Invariant.STRING_NOT_EMPTY},
        'account': {
            'loginAttempts': {Invariant.NUMBER_INTEGER},
            'isBlocked': {Invariant.LITERAL_BOOLEAN},
            'lastPasswordChange': {Invariant.STRING_NOT_EMPTY, Invariant.LITERAL_NULL},
            'preferredLanguage': {Invariant.STRING_NOT_EMPTY}
        },
        'address': {
            'city': {Invariant.STRING_NOT_EMPTY},
            'street': {Invariant.STRING_EMPTY, Invariant.STRING_NOT_EMPTY},
            'zipCode': {Invariant.STRING_NOT_EMPTY, Invariant.LITERAL_NULL}
        }
    }

    actual_result = merge_dicts(*data)
    assert actual_result == expected_result
