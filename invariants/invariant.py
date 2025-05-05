from enum import Enum
from typing import Any


class Invariant(Enum):

    NUMBER_INTEGER = 'number_integer'
    NUMBER_FLOAT = 'number_float'

    STRING_EMPTY = 'string_empty'
    STRING_NOT_EMPTY = 'string_not_empty'

    LITERAL_NULL = 'literal_null'
    LITERAL_BOOLEAN = 'literal_boolean'


def define_invariant_by_value(value: Any) -> Invariant:
    if isinstance(value, int):
        return Invariant.NUMBER_INTEGER
    raise ValueError(f'Unknown value: {value}')


def invariants_from_json(json_data: dict) -> dict[str, Invariant]:
    raise NotImplementedError
