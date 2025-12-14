#!/usr/bin/python3

'''
Module that does everything for JSON
'''


import sys
import json


filename = "add_item.json"


def save_to_json_file(my_obj, filename):
    '''
    Save to json file function
    '''

    with open(filename, 'w') as f:
        f.write(json.dumps(my_obj))


def load_from_json_file(filename):
    '''
    Save to json file function
    '''

    with open(filename, 'r') as f:
        obj = f.read()
        my_list = json.loads(obj)
        return my_list


try:
    my_list = load_from_json_file(filename)
except FileNotFoundError:
    my_list = []

my_list.extend(sys.argv[1:])

save_to_json_file(my_list, filename)
