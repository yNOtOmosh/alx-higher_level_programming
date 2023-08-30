#!/usr/bin/python3
"""Define a Square."""

class Square:
    """
    This class represents a Square.

    It defines a Square by the size.

    Attributes:
        __size (int): The size of the Square.
    """
    def __init__(self, size=0):
        """
        Initializes a square size.

        Args:
            size (int, optional): The size of the square.

        Raises:
            TypeError: If size is naot an integer.
            ValueError: If size is less than 0.
        """
        self.size = size

    @property
    def size(self):
        """
        Get the size of the Square.

        Returns:
            int: The size of the Square.
        """
        return self.__size

    @size.setter
    def size(self,value):
        """
        Set the size of the Square.

        Args:
            value (int): The new size of Square.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >+0")

        self.__size = value

    def area(self):
        """
        Calculates and returns the current area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size * self.__size

    def my_print(self):
        """
        Prints the Square using the '#' character.

        If size is 0, prints an empty line.
        """
        if self.__size == 0:
            print("")
        else:
            for _ in range(self.__size):
                print("#" * self.__size)
