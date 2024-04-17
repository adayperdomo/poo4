import pytest

from ejemploExceptions import EjemploExcepciones

def test_ZeroDivisionError():
    ejemplo = EjemploExcepciones()
    with pytest.raises(ZeroDivisionError):
        ejemplo.zeroDivisionError(num = 2, den = 0)

    assert ejemplo.zeroDivisionError(num = 4, den = 2) == 2