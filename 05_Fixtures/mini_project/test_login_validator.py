import pytest

def validate_login(username, password):
    return username == "admin" and password == "secure123"

@pytest.fixture
def login_data():
    return [
        {"username": "admin", "password": "secure123", "expected": True},
        {"username": "admin", "password": "wrongpass", "expected": False},
        {"username": "guest", "password": "secure123", "expected": False},
        {"username": "admin", "password": "", "expected": False}
    ]

def test_login_validator(login_data):
    for case in login_data:
        result = validate_login(case["username"], case["password"])
        assert result == case["expected"]


