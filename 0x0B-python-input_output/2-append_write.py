#!/usr/bin/python3
"""Defines a function that appends a file."""


def append_write(filename="", text=""):
    """Appends a string to the end of a UFT8 text file.

    Args:
        filename (str): The name of the file to append to.
        text (str): The string to append a file.

    Returns:
        The number of characters appended.
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
