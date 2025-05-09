import json
from invariants import TypeInvariant, type_invariants_from_json


def test_type_invariants_from_json_on_flatten_objects_with_lists():

    json_string = '''[
        {
            "name": "Wilfred Snow",
            "mask": [true, false, true],
            "skills": ["Excel", "Word", "PowerPoint"],
            "languages": ["English", "Russian", "French"],
            "salaryHistory": [100, 125]
        },
        {
            "name": "Eva Kemp",
            "mask": [],
            "skills": ["Python", "SQL", "Git"],
            "languages": ["English", "Russian", "", null],
            "salaryHistory": [100, 120.5, 150.75]
        }
    ]
    '''
    json_data = json.loads(json_string)

    expected_result = {
        'name': {TypeInvariant.STRING_NOT_EMPTY},
        'mask': [TypeInvariant.LITERAL_BOOLEAN, TypeInvariant.LIST_EMPTY],
        'skills': [TypeInvariant.STRING_NOT_EMPTY],
        'languages': [TypeInvariant.STRING_NOT_EMPTY, TypeInvariant.STRING_EMPTY, TypeInvariant.LITERAL_NULL],
        'salaryHistory': [TypeInvariant.NUMBER_INTEGER, TypeInvariant.NUMBER_FLOAT]
    }

    actual_result = type_invariants_from_json(json_data)

    assert actual_result == expected_result


def test_type_invariants_from_json_on_nested_objects_depth_1_with_lists():
    json_string = '''[
        {
            "name": "Wilfred Snow",
            "account": {
                "loginAttempts": 3,
                "mask": [true, false, true],
                "skills": ["Excel", "Word", "PowerPoint"],
                "languages": ["English", "Russian", "French"],
                "salaryHistory": [100, 125]
            },
            "address": {
                "city": "Saint Petersburg",
                "mask": [true, false, true],
                "skills": [],
                "languages": ["English", "Russian", "French"],
                "salaryHistory": [null, 125.5]
            }
        },
        {
            "name": "Eva Kemp",
            "account": {
                "loginAttempts": 0,
                "mask": [],
                "skills": ["Python", "SQL", "Git"],
                "languages": ["English", "Russian", "", null],
                "salaryHistory": [100, 120.5, 150.75]
            },
            "address": {
                "city": "New York",
                "mask": [false, false],
                "skills": [],
                "languages": ["English"],
                "salaryHistory": [50.5, 125.5]
            }
        }
    ]
    '''
    json_data = json.loads(json_string)

    expected_result = {
        'name': {TypeInvariant.STRING_NOT_EMPTY},
        'account': {
            'loginAttempts': {TypeInvariant.NUMBER_INTEGER},
            'mask': [TypeInvariant.LITERAL_BOOLEAN, TypeInvariant.LIST_EMPTY],
            'skills': [TypeInvariant.STRING_NOT_EMPTY],
            'languages': [TypeInvariant.STRING_NOT_EMPTY, TypeInvariant.STRING_EMPTY, TypeInvariant.LITERAL_NULL],
            'salaryHistory': [TypeInvariant.NUMBER_INTEGER, TypeInvariant.NUMBER_FLOAT]
        },
        'address': {
            'city': {TypeInvariant.STRING_NOT_EMPTY},
            'mask': [TypeInvariant.LITERAL_BOOLEAN],
            'skills': [TypeInvariant.LIST_EMPTY],
            'languages': [TypeInvariant.STRING_NOT_EMPTY],
            'salaryHistory': [TypeInvariant.LITERAL_NULL, TypeInvariant.NUMBER_FLOAT]
        }
    }

    actual_result = type_invariants_from_json(json_data)

    assert actual_result == expected_result


def test_type_invariants_from_json_on_nested_objects_depth_2_with_lists():
    json_string = '''[
        {
            "name": "Wilfred Snow",
            "account": {
                "loginAttempts": 3,
                "mask": [true, false, true],
                "skills": ["Excel", "Word", "PowerPoint"],
                "languages": ["English", "Russian", "French"],
                "salaryHistory": [100, 125],
                "address": {
                    "city": "Saint Petersburg",
                    "mask": [true, false, true],
                    "skills": [],
                    "languages": ["English", "Russian", "French"],
                    "salaryHistory": [null, 125.5]
                }
            }
        },
        {
            "name": "Eva Kemp",
            "account": {
                "loginAttempts": 0,
                "mask": [],
                "skills": ["Python", "SQL", "Git"],
                "languages": ["English", "Russian", "", null],
                "salaryHistory": [100, 120.5, 150.75],
                "address": {
                    "city": "New York",
                    "mask": [false, false],
                    "skills": [],
                    "languages": ["English"],
                    "salaryHistory": [50.5, 125.5]
                }
            }
        }
    ]
    '''
    json_data = json.loads(json_string)

    expected_result = {
        'name': {TypeInvariant.STRING_NOT_EMPTY},
        'account': {
            'loginAttempts': {TypeInvariant.NUMBER_INTEGER},
            'mask': [TypeInvariant.LITERAL_BOOLEAN, TypeInvariant.LIST_EMPTY],
            'skills': [TypeInvariant.STRING_NOT_EMPTY],
            'languages': [TypeInvariant.STRING_NOT_EMPTY, TypeInvariant.STRING_EMPTY, TypeInvariant.LITERAL_NULL],
            'salaryHistory': [TypeInvariant.NUMBER_INTEGER, TypeInvariant.NUMBER_FLOAT],
            'address': {
                'city': {TypeInvariant.STRING_NOT_EMPTY},
                'mask': [TypeInvariant.LITERAL_BOOLEAN],
                'skills': [TypeInvariant.LIST_EMPTY],
                'languages': [TypeInvariant.STRING_NOT_EMPTY],
                'salaryHistory': [TypeInvariant.LITERAL_NULL, TypeInvariant.NUMBER_FLOAT]
            }
        }
    }

    actual_result = type_invariants_from_json(json_data)

    assert actual_result == expected_result
