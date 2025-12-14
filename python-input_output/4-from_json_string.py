#!/usr/bin/python3

'''
Module writes a function that
returns opposite of JSON representation
'''


import json


def from_json_string(my_str):
    '''
    JSON function
    '''

    return json.loads(my_str)
