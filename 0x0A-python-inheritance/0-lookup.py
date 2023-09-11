#!/usr/bin/python3
"""Defines attribute lookup function."""


def lookup(obj):
    """Return a list of available attributes."""
    return (dir(obj))
