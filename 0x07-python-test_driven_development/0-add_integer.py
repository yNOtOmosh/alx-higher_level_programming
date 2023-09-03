#!/usr/bin/python3
"""Defines addition function."""

def add_integer(a, b=98):
    """Return the integer addition of a and b.

    :param a: The first number (integer or float).
    :param b: The second number (integer or float, default is 98).

    Raises:
        TypeError: if either a or b is non-integer and non-float.
    """
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    return (int(a) + int(b))
