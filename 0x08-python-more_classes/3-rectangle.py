#!/usr/bin/python3
"""Define a rectangle."""


class Rectangle:
    """Represents a rectangle class."""

    def __init__(self, width=0, height=0):
        """Initialize a new rectangle instance.

        Args:
            width (int):The width of the rectangle.
            height (int): The height of the rectangle.
        """
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """Retrive the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Retrive the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__heigth = value

    def area(self):
        """Calculate and return the area of the rectangle."""
        return (self.__width * self.__height)

    def perimeter(self):
        """Calculte and returns the perimeter of the rectangle."""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return (2 * (self.__width + self.__height))

    def __str__(self):
        """Returns a string representation of the rectangle with #."""
        if self.__width == 0 or self.__height == 0:
            return ("")
        rectangle_str = ""
        for _ in range(self.__height):
            rectangle_str += "#" * self.__width + "\n"
        return rectangle_str[:-1]
