import pytest
from invariants import TypeInvariant
from invariants.type_invariants import define_type_invariants_of_dict


@pytest.mark.parametrize(
    'dict_data, expected_result',
    [
        (
            {
                'name': 'Wilfred Snow',
                'mask': [True, False, True],
                'skills': ['Excel', 'Word', 'PowerPoint'],
                'languages': ['English', 'Russian', 'French'],
                'salaryHistory': [100, 125]
            },
            {
                'name': TypeInvariant.STRING_NOT_EMPTY,
                'mask': [TypeInvariant.LITERAL_BOOLEAN],
                'skills': [TypeInvariant.STRING_NOT_EMPTY],
                'languages': [TypeInvariant.STRING_NOT_EMPTY],
                'salaryHistory': [TypeInvariant.NUMBER_INTEGER]
            }
        ),
        (
            {
                'name': 'Eva Kemp',
                'skills': ['Python', 'SQL', 'Git'],
                'languages': ['English', 'Russian', '', None],
                'salaryHistory': [100, 120.5, 150.75]
            },
            {
                'name': TypeInvariant.STRING_NOT_EMPTY,
                'skills': [TypeInvariant.STRING_NOT_EMPTY],
                'languages': [TypeInvariant.STRING_NOT_EMPTY, TypeInvariant.STRING_EMPTY, TypeInvariant.LITERAL_NULL],
                'salaryHistory': [TypeInvariant.NUMBER_INTEGER, TypeInvariant.NUMBER_FLOAT]
            }
        ),
        (
            {
                'name': 'Eva Kemp',
                'mask': [],
                'skills': ['Python', 'SQL', 'Git'],
                'languages': ['English', 'Russian', '', None],
                'salaryHistory': [100, 120.5, 150.75]
            },
            {
                'name': TypeInvariant.STRING_NOT_EMPTY,
                'mask': [TypeInvariant.LIST_EMPTY],
                'skills': [TypeInvariant.STRING_NOT_EMPTY],
                'languages': [TypeInvariant.STRING_NOT_EMPTY, TypeInvariant.STRING_EMPTY, TypeInvariant.LITERAL_NULL],
                'salaryHistory': [TypeInvariant.NUMBER_INTEGER, TypeInvariant.NUMBER_FLOAT]
            }
        )
    ],
    ids=[
        'define_type_invariants_of_dict_on_flatten_objects_with_lists',
        'define_type_invariants_of_dict_on_flatten_objects_with_none_value_in_list',
        'define_type_invariants_of_dict_on_flatten_objects_with_empty_list'
    ]
)
def test_define_type_invariants_of_dict_on_flatten_objects_with_lists(dict_data: dict, expected_result: dict):
    assert define_type_invariants_of_dict(dict_data) == expected_result


@pytest.mark.parametrize(
    'dict_data, expected_result',
    [
        (
            {
                'name': 'Wilfred Snow',
                'account': {
                    'loginAttempts': 3,
                    'mask': [True, False, True],
                    'skills': ['Excel', 'Word', 'PowerPoint'],
                    'languages': ['English', 'Russian', 'French'],
                    'salaryHistory': [100, 125]
                },
                'address': {
                    'city': 'Saint Petersburg',
                    'mask': [True, False, True],
                    'skills': [],
                    'languages': ['English', 'Russian', 'French'],
                    'salaryHistory': [None, 125.5]
                }
            },
            {
                'name': TypeInvariant.STRING_NOT_EMPTY,
                'account': {
                    'loginAttempts': TypeInvariant.NUMBER_INTEGER,
                    'mask': [TypeInvariant.LITERAL_BOOLEAN],
                    'skills': [TypeInvariant.STRING_NOT_EMPTY],
                    'languages': [TypeInvariant.STRING_NOT_EMPTY],
                    'salaryHistory': [TypeInvariant.NUMBER_INTEGER]
                },
                'address': {
                    'city': TypeInvariant.STRING_NOT_EMPTY,
                    'mask': [TypeInvariant.LITERAL_BOOLEAN],
                    'skills': [TypeInvariant.LIST_EMPTY],
                    'languages': [TypeInvariant.STRING_NOT_EMPTY],
                    'salaryHistory': [TypeInvariant.LITERAL_NULL, TypeInvariant.NUMBER_FLOAT]
                }
            }
        ),
        (
            {
                'name': 'Eva Kemp',
                'account': {
                    'loginAttempts': 0,
                    'skills': ['Python', 'SQL', 'Git'],
                    'languages': ['English', 'Russian', '', None],
                    'salaryHistory': [100, 120.5, 150.75]
                },
                'address': {
                    'city': 'New York',
                    'mask': [False, False],
                    'languages': ['English'],
                    'salaryHistory': [50.5, 125.5]
                }
            },
            {
                'name': TypeInvariant.STRING_NOT_EMPTY,
                'account': {
                    'loginAttempts': TypeInvariant.NUMBER_INTEGER,
                    'skills': [TypeInvariant.STRING_NOT_EMPTY],
                    'languages': [TypeInvariant.STRING_NOT_EMPTY, TypeInvariant.STRING_EMPTY, TypeInvariant.LITERAL_NULL],
                    'salaryHistory': [TypeInvariant.NUMBER_INTEGER, TypeInvariant.NUMBER_FLOAT]
                },
                'address': {
                    'city': TypeInvariant.STRING_NOT_EMPTY,
                    'mask': [TypeInvariant.LITERAL_BOOLEAN],
                    'languages': [TypeInvariant.STRING_NOT_EMPTY],
                    'salaryHistory': [TypeInvariant.NUMBER_FLOAT]
                }
            }
        ),
        (
            {
                'name': 'Eva Kemp',
                'account': {
                    'loginAttempts': 0,
                    'mask': [],
                    'skills': ['Python', 'SQL', 'Git'],
                    'languages': ['English', 'Russian', '', None],
                    'salaryHistory': [100, 120.5, 150.75]
                },
                'address': {
                    'city': 'New York',
                    'mask': [False, False],
                    'skills': [],
                    'languages': ['English'],
                    'salaryHistory': [50.5, 125.5]
                }
            },
            {
                'name': TypeInvariant.STRING_NOT_EMPTY,
                'account': {
                    'loginAttempts': TypeInvariant.NUMBER_INTEGER,
                    'mask': [TypeInvariant.LIST_EMPTY],
                    'skills': [TypeInvariant.STRING_NOT_EMPTY],
                    'languages': [TypeInvariant.STRING_NOT_EMPTY, TypeInvariant.STRING_EMPTY, TypeInvariant.LITERAL_NULL],
                    'salaryHistory': [TypeInvariant.NUMBER_INTEGER, TypeInvariant.NUMBER_FLOAT]
                },
                'address': {
                    'city': TypeInvariant.STRING_NOT_EMPTY,
                    'mask': [TypeInvariant.LITERAL_BOOLEAN],
                    'skills': [TypeInvariant.LIST_EMPTY],
                    'languages': [TypeInvariant.STRING_NOT_EMPTY],
                    'salaryHistory': [TypeInvariant.NUMBER_FLOAT]
                }
            }
        )
    ],
    ids=[
        'define_type_invariants_of_dict_on_nested_objects_depth_1_with_lists',
        'define_type_invariants_of_dict_on_nested_objects_depth_1_with_none_value_in_list',
        'define_type_invariants_of_dict_on_nested_objects_depth_1_with_empty_list'
    ]
)
def test_define_type_invariants_of_dict_on_nested_objects_depth_1_with_lists(dict_data: dict, expected_result: dict):
    assert define_type_invariants_of_dict(dict_data) == expected_result


@pytest.mark.parametrize(
    'dict_data, expected_result',
    [
        (
            {
                'name': 'Wilfred Snow',
                'account': {
                    'loginAttempts': 3,
                    'mask': [True, False, True],
                    'skills': ['Excel', 'Word', 'PowerPoint'],
                    'languages': ['English', 'Russian', 'French'],
                    'salaryHistory': [100, 125],
                    'address': {
                        'city': 'Saint Petersburg',
                        'mask': [True, False, True],
                        'skills': [],
                        'languages': ['English', 'Russian', 'French'],
                        'salaryHistory': [None, 125.5]
                    }
                }
            },
            {
                'name': TypeInvariant.STRING_NOT_EMPTY,
                'account': {
                    'loginAttempts': TypeInvariant.NUMBER_INTEGER,
                    'mask': [TypeInvariant.LITERAL_BOOLEAN],
                    'skills': [TypeInvariant.STRING_NOT_EMPTY],
                    'languages': [TypeInvariant.STRING_NOT_EMPTY],
                    'salaryHistory': [TypeInvariant.NUMBER_INTEGER],
                    'address': {
                        'city': TypeInvariant.STRING_NOT_EMPTY,
                        'mask': [TypeInvariant.LITERAL_BOOLEAN],
                        'skills': [TypeInvariant.LIST_EMPTY],
                        'languages': [TypeInvariant.STRING_NOT_EMPTY],
                        'salaryHistory': [TypeInvariant.LITERAL_NULL, TypeInvariant.NUMBER_FLOAT]
                    }
                }
            }
        ),
        (
            {
                'name': 'Eva Kemp',
                'account': {
                    'loginAttempts': 0,
                    'skills': ['Python', 'SQL', 'Git'],
                    'languages': ['English', 'Russian', '', None],
                    'salaryHistory': [100, 120.5, 150.75],
                    'address': {
                        'city': 'New York',
                        'mask': [False, False],
                        'languages': ['English'],
                        'salaryHistory': [50.5, 125.5]
                    }
                }
            },
            {
                'name': TypeInvariant.STRING_NOT_EMPTY,
                'account': {
                    'loginAttempts': TypeInvariant.NUMBER_INTEGER,
                    'skills': [TypeInvariant.STRING_NOT_EMPTY],
                    'languages': [TypeInvariant.STRING_NOT_EMPTY, TypeInvariant.STRING_EMPTY, TypeInvariant.LITERAL_NULL],
                    'salaryHistory': [TypeInvariant.NUMBER_INTEGER, TypeInvariant.NUMBER_FLOAT],
                    'address': {
                        'city': TypeInvariant.STRING_NOT_EMPTY,
                        'mask': [TypeInvariant.LITERAL_BOOLEAN],
                        'languages': [TypeInvariant.STRING_NOT_EMPTY],
                        'salaryHistory': [TypeInvariant.NUMBER_FLOAT]
                    }
                }
            }
        ),
        (
            {
                'name': 'Eva Kemp',
                'account': {
                    'loginAttempts': 0,
                    'mask': [],
                    'skills': ['Python', 'SQL', 'Git'],
                    'languages': ['English', 'Russian', '', None],
                    'salaryHistory': [100, 120.5, 150.75],
                    'address': {
                        'city': 'New York',
                        'mask': [False, False],
                        'skills': [],
                        'languages': ['English'],
                        'salaryHistory': [50.5, 125.5]
                    }
                }
            },
            {
                'name': TypeInvariant.STRING_NOT_EMPTY,
                'account': {
                    'loginAttempts': TypeInvariant.NUMBER_INTEGER,
                    'mask': [TypeInvariant.LIST_EMPTY],
                    'skills': [TypeInvariant.STRING_NOT_EMPTY],
                    'languages': [TypeInvariant.STRING_NOT_EMPTY, TypeInvariant.STRING_EMPTY, TypeInvariant.LITERAL_NULL],
                    'salaryHistory': [TypeInvariant.NUMBER_INTEGER, TypeInvariant.NUMBER_FLOAT],
                    'address': {
                        'city': TypeInvariant.STRING_NOT_EMPTY,
                        'mask': [TypeInvariant.LITERAL_BOOLEAN],
                        'skills': [TypeInvariant.LIST_EMPTY],
                        'languages': [TypeInvariant.STRING_NOT_EMPTY],
                        'salaryHistory': [TypeInvariant.NUMBER_FLOAT]
                    }
                }
            }
        )
    ],
    ids=[
        'define_type_invariants_of_dict_on_nested_objects_depth_2_with_lists',
        'define_type_invariants_of_dict_on_nested_objects_depth_2_with_none_value_in_list',
        'define_type_invariants_of_dict_on_nested_objects_depth_2_with_empty_list'
    ]
)
def test_define_type_invariants_of_dict_on_nested_objects_depth_2_with_lists(dict_data: dict, expected_result: dict):
    assert define_type_invariants_of_dict(dict_data) == expected_result
