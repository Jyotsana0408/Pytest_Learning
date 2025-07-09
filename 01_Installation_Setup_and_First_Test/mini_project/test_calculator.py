def add(x,y):
    return x+y

def subtract(x,y):
    return x-y

def multiplication(x,y):
    return x*y

def division(x,y):
    return x/y

def test_calc():

    result1 = add(6,3)
    print(result1)
    assert result1 == 9

    result2 = subtract(6, 3)
    print(result2)
    assert result2 == 3

    result3 = multiplication(6, 3)
    print(result3)
    assert result3 == 18

    result4 = division(6, 3)
    print(result4)
    assert result4 == 2.0