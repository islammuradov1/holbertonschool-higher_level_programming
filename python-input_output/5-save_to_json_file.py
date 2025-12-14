#!/usr/bin/python3
'''
Module that writes JSON representation
into the file
'''


import json


def save_to_json_file(my_obj, filename):
    '''
    Save to json file function
    '''

    with open(filename, 'w') as f:
        f.write(json.dumps(my_obj))
