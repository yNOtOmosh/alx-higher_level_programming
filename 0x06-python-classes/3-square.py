#!/usr/bin/python3
"""
Defines the square.
"""
class Square:
    """
    This class represents a square.

    Attributes:
        __size (int): The size of the square.
    """
    def __init__(self, size=0):
        """
        Initializes a square with an optional size.

        Args:
            size (int, optional): The size of the square.

        Raises:
            TypeError: If the size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size

    def area(self):
        """
        Calculates and returns the current area of the Square.

        Returns:
            int: The area of the Square.
        """
        return self.__size * self.__size
