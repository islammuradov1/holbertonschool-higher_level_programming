#!/usr/bin/python3
""" a function """


def inherits_from(obj, a_class):
    """ issubclass """
    return issubclass(type(obj), a_class) and not type(obj) is a_class
