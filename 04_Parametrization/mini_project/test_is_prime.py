import pytest

def is_prime(n):
    if n>1:
        for i in range(2,n):
            if n%i ==0:
                return False
                break
        else:
                return True
    else:
        return False

@pytest.mark.parametrize("number,expected",[
    (2, True),
    (3, True),
    (4, False),
    (5, True),
    (9, False),
    (11, True),
    (1, False),
    (0, False),
    (-7, False)
] )
def test_is_prime(number,expected):
    assert is_prime(number) == expected
