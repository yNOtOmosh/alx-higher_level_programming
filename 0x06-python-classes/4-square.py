#!/usr/bin/python3
"""
Define a class Square.
"""
class Square:
    """Represents a Square."""

    def __init__(self, size=0):
        """
        Initializes a Square.

        Args:
            size (int, optional): The size of the Square.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        self.size = size

    @property
    def size(self):
        """
        Get the size of the Square.

        Returns:
            int: The size of the square.
        """
        return (self.__size)

    @size.setter
    def size(self, value):
        """
        Set the size of the square.

        Args:
            value (int): The new size for the square .

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    def area(self):
        """
        Calculates and returns the current area of the Square.

        Returns:
            int: The area of the square.
        """
        return (self.__size * self.__size)
