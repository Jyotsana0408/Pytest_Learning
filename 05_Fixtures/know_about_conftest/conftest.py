"""
The conftest.py file in Pytest is like a central hub for shared fixtures and hooks.
It helps you organize and reuse setup logic across multiple test files without needing to import anything manually.

What Is conftest.py?

    It’s a special Pytest configuration file.
    Placed in your test directory (or subdirectories).
    Automatically discovered by Pytest during test collection.
    Used to define fixtures, hooks, and plugins that apply to all tests in that directory and below.

Relationship Between conftest.py and Fixtures:

    Fixtures defined in conftest.py are globally available to all test files in the same directory tree.
    You don’t need to import them in your test files—Pytest finds them automatically.
    This keeps your test files clean and modular.

Why Use conftest.py?

    Avoid duplication: Define once, use everywhere.
    Improve readability: Keeps test files focused on logic.
    Enable overrides: You can define a fixture in a subdirectory’s conftest.py to override a parent fixture.

Fixture Scope in Pytest

    Fixture scope controls how often a fixture is created and destroyed during a test run. Pytest supports these scopes:

    Scope	    Description
    function	Default. Fixture runs before each test function.
    class	    Fixture runs once per test class.
    module	    Fixture runs once per test module/file.
    session	    Fixture runs once for the entire test session (across all files)

"""
import pytest

@pytest.fixture(scope="function",autouse=True)
def set_up():
    print("Launch Browser")
    print("Login")
    print("Browse products")
    yield
    print("Logoff")
    print("Close Browser")

# No import needed for sample_user — Pytest handles it behind the scenes!
@pytest.fixture
def sample_user():
    return {"name": "Jyotsna", "role": "Engineer"}