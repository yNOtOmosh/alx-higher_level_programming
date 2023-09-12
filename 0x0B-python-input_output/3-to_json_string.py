#!/usr/bin/python3
"""Defines JSON representation of a string."""
import json


def to_json_string(my_obj):
    """Return the JSON representation of a string."""
    return json.dumps(my_obj)
