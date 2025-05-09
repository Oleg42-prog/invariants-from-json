from enum import Enum
from typing import Any
from collections import defaultdict
from functools import reduce


class Invariant(Enum):

    NUMBER_INTEGER = 'number_integer'
    NUMBER_FLOAT = 'number_float'

    STRING_EMPTY = 'string_empty'
    STRING_NOT_EMPTY = 'string_not_empty'

    LITERAL_NULL = 'literal_null'
    LITERAL_BOOLEAN = 'literal_boolean'


def define_invariant_by_value(value: Any) -> Invariant:
    match value:
        case bool():
            return Invariant.LITERAL_BOOLEAN
        case int():
            return Invariant.NUMBER_INTEGER
        case float():
            return Invariant.NUMBER_FLOAT
        case '':
            return Invariant.STRING_EMPTY
        case str():
            return Invariant.STRING_NOT_EMPTY
        case None:
            return Invariant.LITERAL_NULL
        case _:
            raise ValueError(f'Unknown value: {value}')


def define_invariants_of_dict(dict_data: dict) -> dict[str, Invariant]:
    return {
        key: define_invariants_of_dict(value) if isinstance(value, dict) else define_invariant_by_value(value)
        for key, value in dict_data.items()
    }


def merge_dicts(*dicts: dict[str, Invariant]) -> dict[str, Invariant]:
    result = defaultdict(set)
    for d in dicts:
        for k, v in d.items():
            result[k].add(v)
    return result


def invariants_from_json(json_data: list[dict]) -> dict[str, Invariant]:

    if not json_data:
        return {}

    return reduce(merge_dicts, (define_invariants_of_dict(d) for d in json_data))
