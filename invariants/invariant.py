from enum import Enum


class Invariant(Enum):

    NUMBER_INTEGER = 'number_integer'
    NUMBER_FLOAT = 'number_float'

    STRING_EMPTY = 'string_empty'
    STRING_NOT_EMPTY = 'string_not_empty'

    LITERAL_NULL = 'literal_null'
    LITERAL_BOOLEAN = 'literal_boolean'


def invariants_from_json(json_data: dict) -> dict[str, Invariant]:
    return {
        'name': {Invariant.STRING_NOT_EMPTY},
        'is_admin': {Invariant.LITERAL_BOOLEAN},
        'age': {Invariant.NUMBER_INTEGER},
        'workPosition': {Invariant.STRING_EMPTY, Invariant.STRING_NOT_EMPTY},
    }
