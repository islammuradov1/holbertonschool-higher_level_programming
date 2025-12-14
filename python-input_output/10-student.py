#!/usr/bin/python3

'''
Module that writes a Student Class
'''


class Student:
    '''
    A student class
    '''

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if isinstance(attrs, list) and all(isinstance(x, str) for x in attrs):
            d = {}
            for name in attrs:
                if name in self.__dict__:
                    d[name] = self.__dict__[name]
            return d
        return self.__dict__
