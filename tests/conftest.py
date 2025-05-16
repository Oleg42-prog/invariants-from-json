# tests/conftest.py
import json
import pytest
from invariants import TypeInvariant


@pytest.fixture(name='sample_user_data_1')
def fixture_sample_user_data_1():
    return {
        "name": "Wilfred Snow",
        "is_admin": True,
        "age": 25,
        "salary": 125.25,
        "workPosition": ""
    }


@pytest.fixture(name='sample_user_data_2')
def fixture_sample_user_data_2():
    return {
        "name": "Eva Kemp",
        "is_admin": False,
        "age": 16,
        "salary": None,
        "workPosition": "Developer"
    }


@pytest.fixture(name='sample_users_data_list')
def fixture_sample_users_data_list(sample_user_data_1, sample_user_data_2):
    return [sample_user_data_1, sample_user_data_2]


@pytest.fixture(name='sample_user_json_string_1')
def fixture_sample_user_json_string_1(sample_user_data_1):
    return json.dumps(sample_user_data_1)


@pytest.fixture(name='sample_user_json_string_2')
def fixture_sample_user_json_string_2(sample_user_data_2):
    return json.dumps(sample_user_data_2)


@pytest.fixture(name='sample_users_list_json_string')
def fixture_sample_users_list_json_string(sample_users_data_list):
    return json.dumps(sample_users_data_list)
