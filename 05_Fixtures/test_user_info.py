import pytest


@pytest.fixture
def user_info():
    return {
        "name" : "jyotsna",
        "age" : 24,
        "marks" : 98
    }

def test_show_user(user_info):
    assert  user_info["age"] == 24