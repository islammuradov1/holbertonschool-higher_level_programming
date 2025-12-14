#!/usr/bin/python3

'''
Module writes a function that
returns JSON representation
'''


import json


def to_json_string(my_obj):
    '''
    JSON function
    '''

    return json.dumps(my_obj)
