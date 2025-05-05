import json
from invariants import Invariant, invariants_from_json


def test_invariants_from_json():

    json_string = '''[
        {
            "name": "Wilfred Snow",
            "is_admin": true,
            "age": 25,
            "salary": 125.25,
            "workPosition": ""
        },
        {
            "name": "Eva Kemp",
            "is_admin": false,
            "age": 16,
            "salary": null,
            "workPosition": "Developer"
        }
    ]
    '''
    json_data = json.loads(json_string)

    expected_result = {
        'name': {Invariant.STRING_NOT_EMPTY},
        'is_admin': {Invariant.LITERAL_BOOLEAN},
        'age': {Invariant.NUMBER_INTEGER},
        'workPosition': {Invariant.STRING_EMPTY, Invariant.STRING_NOT_EMPTY},
    }

    invariants = invariants_from_json(json_data)

    assert invariants == expected_result
