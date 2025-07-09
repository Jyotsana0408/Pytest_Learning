r"""
    Step-by-Step Pytest Installation
    1. Make Sure Python & pip Are Installed
    Run:
    python --version
    pip --version
    If either command fails, install Python from python.org.

    2. Create a Virtual Environment (Recommended)
    python -m venv .venv

    3. Activate the Virtual Environment
    On Windows:
    .\.venv\Scripts\activate
    On macOS/Linux:
    source .venv/bin/activate

    4. Install Pytest
    pip install pytest

    5. Verify Installation
    pytest --version
    You should see something like pytest 8.4.1 confirming it’s installed

    6. Bonus
    If you ever face issues with pytest not being recognized, try running it like this:
    python -m pytest
"""

r"""
    Test Discovery Rules -->
    Test files should start with test_ or end with _test.py.
    Test functions must start with test_.
    
    -----------------------------------------------------------
    
    Running Tests -->
    Run all tests: pytest
    Run a specific file: pytest test_file.py
    Show print() output: pytest -s test_file.py
    Verbose mode: pytest -v test_file.py
    
    ------------------------------------------------------------
    
    assert in Python -->
    assert is used to verify that a condition is true during runtime.
    If the condition is false, Python raises an AssertionError.
    It’s mainly used for debugging and internal checks, not for handling user errors.
    
    Syntax : 
    python
    assert condition
    assert condition, "Optional error message"
"""

def add(a,b):
    return a+b

def test_add():
    result = add(2,5)
    print(result)
    assert result< 50 ,"result is greater than 50"