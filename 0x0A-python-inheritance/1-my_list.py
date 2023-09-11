#!/usr/bin/python3
"""Defines an inheritance of class MyList."""


class MyList(list):
    """
    MyList class inherits fromlist and adds a print_sorted method.

    Methods:
        print_sorted(): Prints the list in ascending order.
    """
    def print_sorted(self):
        """Prints the list in ascending order."""
        sorted_list = sorted(self)
        print(sorted_list)
