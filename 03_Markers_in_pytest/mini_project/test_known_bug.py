import pytest
import sys
"""
CLI Tip to See Skipped Test Reasons -->
    pytest -v -rs
"""
def login(username=None):
    if username:
        return f"Login successfully for user: {username}"
    return "Login successfully"

@pytest.mark.skip(reason="Known bug: login fails with special characters")
def test_login_with_special_chars():
    assert login("@user!") == "Login successfully"

@pytest.mark.skip(reason="Feature under development: payment gateway integration not ready")
def test_payment_gateway():
    # Test will be skipped until the feature is implemented
    assert False  # Placeholder assertion

@pytest.mark.skipif(sys.platform == "win32", reason="Test not supported on Windows")
def test_unix_specific_feature():
    assert True
