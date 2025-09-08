
"""
Core math utilities for TDD practice.

All functions use basic `float` types only.
"""

from typing import List

def add(a: float, b: float) -> float:
    """
    Return the sum of two numbers.

    Examples:
        >>> add(1.5, 2.5)
        4.0
        >>> add(-3.0, 1.0)
        -2.0
    """
    raise NotImplementedError


def safe_divide(a: float, b: float) -> float:
    """
    Divide `a` by `b`. Raise ValueError when `b` is zero.

    Examples:
        >>> safe_divide(6.0, 3.0)
        2.0
        >>> safe_divide(1.0, 0.0)
        Traceback (most recent call last):
            ...
        ValueError: denominator must not be zero
    """
    raise NotImplementedError

def average(xs: List[float]) -> float:
    """
    Compute the arithmetic mean of a non-empty list of floats.

    Examples:
        >>> average([1.0, 3.0, 5.0])
        3.0
        >>> average([])
        Traceback (most recent call last):
            ...
        ValueError: xs must not be empty
    """
    raise NotImplementedError
