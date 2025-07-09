"""
markers --->
    labels you attach to test functions to categorize, filter, or modify their behavior during test execution.
    They’re incredibly useful for organizing large test suites and running targeted subsets of tests

Common Built-in Markers -->
    Marker	                        Purpose
    @pytest.mark.skip	            Skip a test unconditionally
    @pytest.mark.skipif(condition)	Skip if a condition is true
    @pytest.mark.xfail	            Mark a test as expected to fail
    @pytest.mark.parametrize	    Run a test with multiple input sets
    @pytest.mark.usefixtures	    Apply fixtures to a test function

Custom Markers
You can define your own markers like sanity, regression, smoke, etc. To avoid warnings, register them in pytest.ini:

The pytest.ini -->
configuration file used by Pytest to customize and control how your tests run.
It lives in the root directory of your project and helps you avoid repeating command-line options every time you run tests

What Does pytest.ini Do?
    It allows you to:
    Register custom markers like sanity, regression, smoke
    Set default CLI options (e.g. verbosity, maxfail, durations)
    Define test discovery rules (e.g. file naming patterns)
    Control logging behavior (e.g. log level, format, output file)
    Specify required plugins or minimum Pytest version

Why It’s Useful -->
Keeps your test commands clean and consistent
Prevents marker warnings like PytestUnknownMarkWarning
Makes your test suite easier to maintain and scale
Plays nicely with CI/CD tools like GitHub Actions and Jenkins

Example -->
    pytest.ini
        ini
        [pytest]
        minversion = 6.0
        addopts = -v --maxfail=2 --durations=5
        testpaths = tests
        markers =
            sanity: marks tests as part of the sanity suite
            regression: marks tests as part of the regression suite
        log_cli = true
        log_level = INFO
        log_format = %(asctime)s %(levelname)s %(message)s
        log_date_format = %Y-%m-%d %H:%M:%S

Running Tests by Marker -->
    Use the -m flag to run specific markers:
    pytest -v -m sanity
    pytest -v -m "sanity or regression"
    pytest -v -m "not regression"
"""
import sys
import time
import pytest

# 1. Check string equality
@pytest.mark.sanity
def test_greeting():
    assert "Hello" == "Hello"

# 2. Check arithmetic result
@pytest.mark.sanity
def test_sum():
    assert 2 + 3 == 5

# 3. Check list membership
@pytest.mark.regression
def test_item_in_list():
    assert "apple" in ["banana", "apple", "grape"]

# 4. Check list length
def test_list_length():
    assert len([1, 2, 3]) == 3

# 5. Check boolean expression
@pytest.mark.xfail
def test_true_condition():
    assert 10 > 11

# 6. Check dictionary value
@pytest.mark.regression
def test_dict_key_value():
    user = {"name": "Jyotsna", "role": "QA"}
    assert user["role"] == "QA"

# 7. Check type of variable
@pytest.mark.skip
def test_type_check():
    assert isinstance(100, int)

# 8. Check multiple conditions with `and`
@pytest.mark.regression
def test_multiple_conditions():
    assert (2 + 2 == 4) and (5 > 1)

# 9. Check float precision
@pytest.mark.slow
def test_float_rounding():
    assert round(3.14159, 2) == 3.14

# 10. Check set equality
@pytest.mark.slow
def test_set_equality():
    assert set([1, 2, 3]) == {3, 2, 1}

@pytest.mark.skipif(sys.version_info < (3, 10), reason="Requires Python 3.10 or higher")
def test_python_feature():
    assert True

# Slow Marker Example
# def heavy_calculation():
#     time.sleep(2)  # Simulates delay
#     return sum(range(10000))
#
# @pytest.mark.slow
# def test_heavy_calculation():
#     result = heavy_calculation()
#     assert result == 49995000
