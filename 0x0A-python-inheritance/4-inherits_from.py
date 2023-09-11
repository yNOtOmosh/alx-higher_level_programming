#!/usr/bin/python3
"""Defines a check on inherited class."""

def inherits_from(obj, a_class):
    """
    Checks if an object is an instance of a clss inherited.

    Args:
        obj (object): The object oto check.
        a_class (class): The class to compare against.

    Returns:
        True: if object is an instance of inherited class.
        False: otherwise.
    """
    return issubclass(type(obj), a_class)
