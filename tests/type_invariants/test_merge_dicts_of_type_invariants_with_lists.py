from invariants import TypeInvariant
from invariants.merge import merge_dicts_of_invariants


def test_merge_dicts_of_type_invariants_on_flatten_objects_with_lists():

    data = [
        {
            'name': TypeInvariant.STRING_NOT_EMPTY,
            'mask': [TypeInvariant.LITERAL_BOOLEAN],
            'skills': [TypeInvariant.STRING_NOT_EMPTY],
            'languages': [TypeInvariant.STRING_NOT_EMPTY],
            'salaryHistory': [TypeInvariant.NUMBER_INTEGER]
        },
        {
            'name': TypeInvariant.STRING_NOT_EMPTY,
            'mask': [TypeInvariant.LIST_EMPTY],
            'skills': [TypeInvariant.STRING_NOT_EMPTY],
            'languages': [TypeInvariant.STRING_NOT_EMPTY, TypeInvariant.STRING_EMPTY, TypeInvariant.LITERAL_NULL],
            'salaryHistory': [TypeInvariant.NUMBER_INTEGER, TypeInvariant.NUMBER_FLOAT]
        }
    ]

    expected_result = {
        'name': {TypeInvariant.STRING_NOT_EMPTY},
        'mask': [TypeInvariant.LITERAL_BOOLEAN, TypeInvariant.LIST_EMPTY],
        'skills': [TypeInvariant.STRING_NOT_EMPTY],
        'languages': [TypeInvariant.STRING_NOT_EMPTY, TypeInvariant.STRING_EMPTY, TypeInvariant.LITERAL_NULL],
        'salaryHistory': [TypeInvariant.NUMBER_INTEGER, TypeInvariant.NUMBER_FLOAT]
    }

    actual_result = merge_dicts_of_invariants(*data)

    assert actual_result == expected_result
