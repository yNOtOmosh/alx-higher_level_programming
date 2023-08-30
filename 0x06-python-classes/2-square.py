#!/usr/bin/python3
"""Defines a square."""

class Square:
    """This class represents a square.
    
    It defines a square by the size.

    Attributes:
    __size (int): The size of the square.
    """

    def __init__(self, size=0):
        """Initializes a square with an optional size.

        Args:
            size (int, optional): The size of the square. Default is 0.

        Raises:
            TypeError: if the sise is not an integer.
            ValueError: if size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size
