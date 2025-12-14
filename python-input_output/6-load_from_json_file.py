#!/usr/bin/python3
'''
Module that writes opposite of JSON representation
into the file
'''


import json


def load_from_json_file(filename):
    '''
    Save to json file function
    '''

    with open(filename, 'r') as f:
        obj = f.read()
        my_list = json.loads(obj)
        return my_list
