"""
    Run a specific file: pytest test_file.py
    Show print() output: pytest -s test_file.py
    Verbose mode: pytest -v test_file.py
"""

def square(a):
    return a *a

def test_square():
    result = square(4)
    print(result)
    assert  result == 16