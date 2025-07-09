"""
Parametrization in Pytest --->
    powerful feature that lets you run the same test function with multiple sets of input data
    perfect for validating logic across a range of scenarios without duplicating code

@pytest.mark.parametrize takes:
    A string of comma-separated parameter names
    A list of tuples with values for each test run

Why It’s Useful -->
    Reduces code duplication
    Improves test coverage
    Makes failures easier to trace
    Plays well with CI/CD pipelines

pytest.param --->
    special helper used inside @pytest.mark.parametrize
    to add metadata to individual test cases, like custom IDs or marks (e.g. xfail, skip)

Why Use pytest.param -->
    Attach marks like xfail, skip, or custom markers to specific test cases
    Assign readable IDs for better test output and filtering
    Control behavior of individual parameter sets without affecting others
"""
import pytest

@pytest.mark.parametrize("a, b, expected",[
    (1,2,3),
    (5,6,11),
    (4,8,12)
])
def test_add(a,b, expected):
    assert a+b == expected

@pytest.mark.parametrize("item",["banana", "apple", "mango"])
def test_items_in_list(item):
    fruits = ["banana", "apple", "mango", "watermelon", "strawberry"]
    assert item in fruits ,"fruit is not present in list"

@pytest.mark.parametrize("text, length", [
    ("hello", 5),
    ("pytest", 6),
    ("QA", 2)
])
def test_string_length(text, length):
    assert len(text) == length

@pytest.mark.parametrize("x", [5, 10, 100])
def test_greater_than_two(x):
    assert x > 2

@pytest.mark.parametrize("num", [2, 4, 6, 8])
def test_even(num):
    assert num % 2 == 0

