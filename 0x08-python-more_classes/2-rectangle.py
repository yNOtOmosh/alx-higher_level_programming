#!/usr/bin/python3
"""Defines a rectangle."""


class Rectangle:
    """Represents a rectangle class."""

    def __init__(self, width=0, height=0):
        """Initialize a new rectangle instance.

        Args:
            width (int): The widthe of the rectangle.
            height (int): The hieght of the rectanglr.
        """
        self.width = width
        self.height = height

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
        self.__height = value

    def area(self):
        """Calculate and return the area of the rectangle."""
        return (self.__width * self.__height)

    def perimeter(self):
        """Calculate and return the perimeter of the rectangle."""
        return 2 * (self.__width + self.__height)
