import pytest
from main import Calculator

calc = Calculator()


@pytest.mark.parametrize("a,b,expected", [
    (2, 3, 5),
    (-1, 1, 0),
    (0, 0, 0)
])
def test_add(a, b, expected):
    assert calc.add(a, b) == expected


@pytest.mark.parametrize("a,b,expected", [
    (10, 5, 5),
    (0, 7, -7),
    (-3, -3, 0)
])
def test_subtract(a, b, expected):
    assert calc.subtract(a, b) == expected


@pytest.mark.parametrize("a,b,expected", [
    (2, 3, 6),
    (-1, 5, -5),
    (0, 9, 0)
])
def test_multiply(a, b, expected):
    assert calc.multiply(a, b) == expected


@pytest.mark.parametrize("a,b,expected", [
    (10, 2, 5),
    (9, 3, 3),
    (5, 2, 2.5)
])
def test_divide(a, b, expected):
    assert calc.divide(a, b) == expected


def test_divide_by_zero():
    with pytest.raises(ValueError):
        calc.divide(10, 0)


@pytest.mark.parametrize("n,expected", [
    (2, True),
    (3, True),
    (4, False),
    (17, True),
    (20, False)
])
def test_is_prime_number(n, expected):
    assert calc.is_prime_number(n) == expected
