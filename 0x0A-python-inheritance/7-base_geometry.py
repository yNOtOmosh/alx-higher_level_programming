#!/usr/bin/python3
"""Defines class BaseGeometry with area and integer."""


class BaseGeometry:
    """Class with area and integer_validator methods."""

    def area(self):
        """Raises an exception 'area() in not implimented."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates a given  value.

        Args:
            name (str): The name of the value being validated.
            value (int): The value to be validated.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If is less than or equal to 0.
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
