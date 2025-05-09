from enum import Enum
from typing import Any
from collections import defaultdict
from functools import reduce


class TypeInvariant(Enum):

    NUMBER_INTEGER = 'number_integer'
    NUMBER_FLOAT = 'number_float'

    STRING_EMPTY = 'string_empty'
    STRING_NOT_EMPTY = 'string_not_empty'

    LITERAL_NULL = 'literal_null'
    LITERAL_BOOLEAN = 'literal_boolean'


def define_type_invariant_by_value(value: Any) -> TypeInvariant:
    match value:
        case bool():
            return TypeInvariant.LITERAL_BOOLEAN
        case int():
            return TypeInvariant.NUMBER_INTEGER
        case float():
            return TypeInvariant.NUMBER_FLOAT
        case '':
            return TypeInvariant.STRING_EMPTY
        case str():
            return TypeInvariant.STRING_NOT_EMPTY
        case None:
            return TypeInvariant.LITERAL_NULL
        case _:
            raise ValueError(f'Unknown value: {value}')


def define_invariants_of_dict(dict_data: dict) -> dict[str, TypeInvariant]:
    return {
        key: define_invariants_of_dict(value) if isinstance(value, dict) else define_type_invariant_by_value(value)
        for key, value in dict_data.items()
    }


def merge_dicts(*dicts: dict[str, Any]) -> dict[str, Any]:

    result = defaultdict(set)

    keys = set()
    for d in dicts:
        keys.update(d.keys())

    for key in keys:
        values = [d[key] for d in dicts if key in d]
        types = set(type(v) for v in values)
        if len(types) > 1:
            raise ValueError(f'Types of values for key {key} are different: {types}')
        if dict in types:
            result[key] = merge_dicts(*values)
        else:
            result[key] |= set(values)

    return result


def invariants_from_json(json_data: list[dict]) -> dict[str, Any]:

    if not json_data:
        return {}

    return reduce(merge_dicts, (define_invariants_of_dict(d) for d in json_data))
