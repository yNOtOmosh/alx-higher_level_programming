#!/usr/bin/python3
"""Defines a check of class and inherited class."""


def is_kind_of_class(obj, a_class):
    """
    Checks if object is an instance or inherited instance of a class.

    Args:
        obj (object): The object to check.
        a_class (class): The class to compare against.

    Return:
        True: if object is an instance or inherited instance of a class.
        False: otherwise.
    """
    return isinstance(obj, a_class)
