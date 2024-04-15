import pytest

def divide(a, b):
    if b == 0:
        raise ValueError("No se puede dividir por cero")
    return a / b

def test_exception():
    a = 0
    b = 10
    with pytest.raises(ZeroDivisionError):
        b / a

def test_divide():
    with pytest.raises(ValueError) as exception_info:
        divide(10, 0)
    
    assert str(exception_info.value) == "No se puede dividir por cero"