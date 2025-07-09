
def square(a):
    return a *a

def test_square():
    result = square(4)
    print(result)
    assert  result == 16