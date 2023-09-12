#!/usr/bin/python3
"""Defines a file reading function."""


def read_file(filename=""):
    """Prints the content of UFT8 text file in stdout."""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
