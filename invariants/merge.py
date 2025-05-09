from collections import defaultdict
from typing import Any


def merge_dicts_of_invariants(*dicts: dict[str, Any]) -> dict[str, Any]:

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
            result[key] = merge_dicts_of_invariants(*values)
        elif list in types:
            result[key] = list(dict.fromkeys(sum(values, [])))
        else:
            result[key] |= set(values)

    return result
