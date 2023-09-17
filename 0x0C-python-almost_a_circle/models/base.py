#!/usr/bin/python3
"""Defines the base class."""
import json
import csv
import turtle


class Base:
    """
    Represents the base model.

    Private class attributes:
        __nb_objects (int): Number of instatiated Bases.
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initializes a new base.

        Args:
            id (int): The identity of the new Base.
        """

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Return the JSON serialization of a list of dictionaries.

        Args:
        list_dictionaries (list): A list of dictionaries.
        """

        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

