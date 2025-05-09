from enum import Enum
from typing import Any
from functools import reduce
from invariants.merge import merge_dicts_of_invariants


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


def define_type_invariants_of_dict(dict_data: dict) -> dict[str, TypeInvariant]:
    return {
        key: define_type_invariants_of_dict(value) if isinstance(value, dict) else define_type_invariant_by_value(value)
        for key, value in dict_data.items()
    }


def type_invariants_from_json(json_data: list[dict]) -> dict[str, Any]:

    if not json_data:
        return {}

    return reduce(merge_dicts_of_invariants, (define_type_invariants_of_dict(d) for d in json_data))
