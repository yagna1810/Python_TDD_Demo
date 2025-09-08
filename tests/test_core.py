
import math
import pytest
from simple_math import add, safe_divide, sqrt_approx, average
from pytest import approx

@pytest.mark.parametrize(
    "a,b,expected",
    [
        (0.0, 0.0, 0.0),
        (1.0, 2.0, 3.0),
        (-2.5, 1.5, -1.0),
        (1e9, 1e9, 2e9),
    ],
)
def test_add_parametrized(a, b, expected):
    assert add(a, b) == approx(expected)


@pytest.mark.parametrize(
    "a,b,expected",
    [
        (10.0, 2.0, 5.0),
        (-9.0, 3.0, -3.0),
        (1.5, 0.5, 3.0),
    ],
)
def test_safe_divide_parametrized(a, b, expected):
    assert safe_divide(a, b) == expected


def test_safe_divide_raises_on_zero():
    with pytest.raises(ValueError, match="denominator must not be zero"):
        safe_divide(1.0, 0.0)


@pytest.mark.parametrize(
    "values,expected",
    [
        ([1.0], 1.0),
        ([1.0, 3.0, 5.0], 3.0),
        ([0.1, 0.2, 0.3, 0.4], 0.25),
        ([1000.0, 1002.0, 998.0], 1000.0),
    ],
)
def test_average_parametrized(values, expected):
    assert average(values) == pytest.approx(expected, rel=1e-12, abs=1e-12)


def test_average_raises_on_empty():
    with pytest.raises(ValueError, match="xs must not be empty"):
        average([])
