#!/usr/bin/python3
"""Defines a class Square."""
class Square:
    """Represents a square.

    It defines a square by its size.
    
    Attributes:
        --size (int): The size of the computer.
    """
    def __init__(self, size):
        """Intanalizes a square with a given size.

        Args:
            size (int):the size of the square
        """
        self.__size = size
