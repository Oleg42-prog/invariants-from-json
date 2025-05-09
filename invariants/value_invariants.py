from enum import Enum


class ValueInvariant(Enum):

    NUMBER_INTEGER_POSITIVE = 'number_integer_positive'
    NUMBER_INTEGER_NEGATIVE = 'number_integer_negative'
    NUMBER_INTEGER_ZERO = 'number_integer_zero'
    NUMBER_FLOAT_POSITIVE = 'number_float_positive'
    NUMBER_FLOAT_NEGATIVE = 'number_float_negative'

    STRING_EMPTY = 'string_empty'
    STRING_URL_FULL = 'string_url_full'
    STRING_URL_PARTIAL = 'string_url_partial'
    STRING_EMAIL = 'string_email'
    STRING_DATE = 'string_date'
    STRING_TIME = 'string_time'
    STRING_DATETIME = 'string_datetime'
    STRING_UUID = 'string_uuid'
    STRING_INTEGER_POSITIVE = 'string_integer_positive'
    STRING_INTEGER_NEGATIVE = 'string_integer_negative'
    STRING_INTEGER_ZERO = 'string_integer_zero'
    STRING_FLOAT_POSITIVE = 'string_float_positive'
    STRING_FLOAT_NEGATIVE = 'string_float_negative'
    STRING_NOT_EMPTY_OTHER = 'string_not_empty_other'

    LITERAL_NULL = 'literal_null'
    LITERAL_BOOLEAN = 'literal_boolean'
    LITERAL_FALSE = 'literal_false'
    LITERAL_TRUE = 'literal_true'
