import json
from invariants import TypeInvariant, type_invariants_from_json


def test_type_invariants_from_json_on_flatten_objects(sample_users_list_json_string):

    json_data = json.loads(sample_users_list_json_string)

    expected_result = {
        'name': {TypeInvariant.STRING_NOT_EMPTY},
        'is_admin': {TypeInvariant.LITERAL_BOOLEAN},
        'age': {TypeInvariant.NUMBER_INTEGER},
        'salary': {TypeInvariant.NUMBER_FLOAT, TypeInvariant.LITERAL_NULL},
        'workPosition': {TypeInvariant.STRING_EMPTY, TypeInvariant.STRING_NOT_EMPTY},
    }

    actual_result = type_invariants_from_json(json_data)

    assert actual_result == expected_result


def test_type_invariants_from_json_on_nested_objects_depth_1():
    json_string = '''[
        {
            "name": "Wilfred Snow",
            "is_admin": true,
            "age": 25,
            "salary": 125.25,
            "workPosition": "",
            "account": {
                "loginAttempts": 3,
                "isBlocked": false,
                "lastPasswordChange": "2024-03-15",
                "preferredLanguage": "ru"
            },
            "address": {
                "city": "Moscow",
                "street": "Lenina 1",
                "zipCode": "123456",
                "isVerified": true
            }
        },
        {
            "name": "Eva Kemp",
            "is_admin": false,
            "age": 16,
            "salary": null,
            "workPosition": "Developer",
            "account": {
                "loginAttempts": 0,
                "isBlocked": true,
                "lastPasswordChange": null,
                "preferredLanguage": "en"
            },
            "address": {
                "city": "Saint Petersburg",
                "street": "",
                "zipCode": null,
                "isVerified": false
            }
        }
    ]
    '''
    json_data = json.loads(json_string)

    expected_result = {
        'name': {TypeInvariant.STRING_NOT_EMPTY},
        'is_admin': {TypeInvariant.LITERAL_BOOLEAN},
        'age': {TypeInvariant.NUMBER_INTEGER},
        'salary': {TypeInvariant.NUMBER_FLOAT, TypeInvariant.LITERAL_NULL},
        'workPosition': {TypeInvariant.STRING_EMPTY, TypeInvariant.STRING_NOT_EMPTY},
        'account': {
            'loginAttempts': {TypeInvariant.NUMBER_INTEGER},
            'isBlocked': {TypeInvariant.LITERAL_BOOLEAN},
            'lastPasswordChange': {TypeInvariant.STRING_NOT_EMPTY, TypeInvariant.LITERAL_NULL},
            'preferredLanguage': {TypeInvariant.STRING_NOT_EMPTY},
        },
        'address': {
            'city': {TypeInvariant.STRING_NOT_EMPTY},
            'street': {TypeInvariant.STRING_EMPTY, TypeInvariant.STRING_NOT_EMPTY},
            'zipCode': {TypeInvariant.STRING_NOT_EMPTY, TypeInvariant.LITERAL_NULL},
            'isVerified': {TypeInvariant.LITERAL_BOOLEAN}
        }
    }

    actual_result = type_invariants_from_json(json_data)

    assert actual_result == expected_result


def test_type_invariants_from_json_on_nested_objects_depth_2():
    json_string = '''[
        {
            "name": "Wilfred Snow",
            "is_admin": true,
            "age": 25,
            "salary": 125.25,
            "workPosition": "",
            "account": {
                "loginAttempts": 3,
                "isBlocked": false,
                "lastPasswordChange": "2024-03-15",
                "preferredLanguage": "ru",
                "address": {
                    "city": "Moscow",
                    "street": "Lenina 1",
                    "zipCode": "123456",
                    "isVerified": true
                }
            }
        },
        {
            "name": "Eva Kemp",
            "is_admin": false,
            "age": 16,
            "salary": null,
            "workPosition": "Developer",
            "account": {
                "loginAttempts": 0,
                "isBlocked": true,
                "lastPasswordChange": null,
                "preferredLanguage": "en",
                "address": {
                    "city": "Saint Petersburg",
                    "street": "",
                    "zipCode": null,
                    "isVerified": false
                }
            }
        }
    ]
    '''
    json_data = json.loads(json_string)

    expected_result = {
        'name': {TypeInvariant.STRING_NOT_EMPTY},
        'is_admin': {TypeInvariant.LITERAL_BOOLEAN},
        'age': {TypeInvariant.NUMBER_INTEGER},
        'salary': {TypeInvariant.NUMBER_FLOAT, TypeInvariant.LITERAL_NULL},
        'workPosition': {TypeInvariant.STRING_EMPTY, TypeInvariant.STRING_NOT_EMPTY},
        'account': {
            'loginAttempts': {TypeInvariant.NUMBER_INTEGER},
            'isBlocked': {TypeInvariant.LITERAL_BOOLEAN},
            'lastPasswordChange': {TypeInvariant.STRING_NOT_EMPTY, TypeInvariant.LITERAL_NULL},
            'preferredLanguage': {TypeInvariant.STRING_NOT_EMPTY},
            'address': {
                'city': {TypeInvariant.STRING_NOT_EMPTY},
                'street': {TypeInvariant.STRING_EMPTY, TypeInvariant.STRING_NOT_EMPTY},
                'zipCode': {TypeInvariant.STRING_NOT_EMPTY, TypeInvariant.LITERAL_NULL},
                'isVerified': {TypeInvariant.LITERAL_BOOLEAN}
            }
        }
    }

    actual_result = type_invariants_from_json(json_data)

    assert actual_result == expected_result


def test_type_invariants_from_json_on_empty_list():

    json_string = '[]'
    json_data = json.loads(json_string)

    expected_result = {}

    actual_result = type_invariants_from_json(json_data)

    assert actual_result == expected_result
