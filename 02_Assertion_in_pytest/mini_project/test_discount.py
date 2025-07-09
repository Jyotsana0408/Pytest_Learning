import pytest
from discount import calculate_discount

"""
    Run a specific file: pytest test_file.py
    Show print() output: pytest -s test_file.py
    Verbose mode: pytest -v test_file.py
    both verbose and print: pytest -v -s test_file.py
"""

def test_electronic_price():
    assert calculate_discount(12000,"electronics") == 12000*0.9

def test_fashion_price():
    assert calculate_discount(6000, "fashion") == 6000 * 0.8

def test_grocery_price():
    assert calculate_discount(1000, "grocery") == 1000

def test_invalid_category():
    with pytest.raises(ValueError):
        calculate_discount(2000,"toys")