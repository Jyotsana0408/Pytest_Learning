"""
    Run a specific file: pytest test_file.py
    Show print() output: pytest -s test_file.py
    Verbose mode: pytest -v test_file.py
    both verbose and print: pytest -v -s test_file.py
"""

"""
assert in Python ---->

assert is used to verify that a condition is true during runtime.
If the condition is false, Python raises an AssertionError.
It’s mainly used for debugging, testing, and internal checks.

Syntax:
assert condition
assert condition, "Optional error message"

Example:
x = 10
assert x > 0, "x must be positive"
If x is not greater than 0, this will raise:
AssertionError: x must be positive

Use Cases
Validate assumptions in your code
Catch bugs early during development
Document intent (e.g., “this should never happen”)
Write test cases in Pytest using assert to compare expected vs actual

------------------------------------------------------------------------------

Advanced Insights on assert --->
1. Assertion with Expressions
You can use any expression inside assert, not just equality:

assert len(my_list) > 0, "List should not be empty"
This is great for validating state and behavior dynamically.

2. AssertionError Handling
In regular Python scripts (outside Pytest), you can catch assertion failures:

try:
    assert 5 > 10, "This should fail"
except AssertionError as e:
    print(f"Caught an assertion error: {e}")
Useful for debugging or graceful failure handling.

3. Avoid Side Effects in Assertions
Don’t rely on functions with side effects (like modifying data) inside assert.
If they fail, it might leave your app in an inconsistent state.

python
#Not ideal
assert update_user_profile() == "Success"
Instead, separate logic and validation cleanly.

4. Use in Pytest vs Production Code
In Pytest: Perfect for validating outcomes.

In production scripts: Avoid using assert to validate user input or app logic.
                       Use exceptions instead for better control and clarity.

5. Disable Behavior in Optimized Mode
Running Python with -O flag disables assertions:

python -O script.py
In this mode, all assert statements are stripped out—meaning no validation. So avoid using assert for anything critical.
"""

def login():
    return "Login successfully"

def test_login():
    result = login()
    print(result)
    assert  result == "Login successfully", "Not login successfully"


def add(a,b):
    return  a+b # You can intentionally mess this up to see failure.

def test_add():
    output = add(2,2)
    print(output)
    assert output == 4, "add(2, 2) should return 4"



