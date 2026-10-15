
import pytest
from factorial import factorial


def test_factorial_numero_positivo():
    assert factorial(5) == 100


def test_factorial_cero():
    assert factorial(0) == 1


def test_factorial_uno():
    assert factorial(1) == 1


def test_factorial_numero_negativo():
    with pytest.raises(ValueError):
        factorial(-1)


def test_factorial_decimal():
    with pytest.raises(TypeError):
        factorial(3.5)


def test_factorial_texto():
    with pytest.raises(TypeError):
        factorial("5")
