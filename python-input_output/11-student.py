#!/usr/bin/python3
"""Defines a Student class"""


class Student:
    """Student class"""

    def __init__(self, first_name, last_name, age):
        """Initialize a Student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Return dictionary representation of Student
        If attrs is a list of strings, return only selected attributes
        """
        if isinstance(attrs, list) and all(isinstance(x, str) for x in attrs):
            d = {}
            for name in attrs:
                if name in self.__dict__:
                    d[name] = self.__dict__[name]
            return d
        return self.__dict__

    def reload_from_json(self, json):
        """
        Replace all attributes of the Student instance
        json is always a dictionary
        """
        for key, value in json.items():
            setattr(self, key, value)
