#!/usr/bin/python3
'''
Module that reads text file
'''


def write_file(filename="", text=""):
    '''
    Function that reads file
    '''

    with open(filename, 'w', encoding='UTF8') as f:
        return f.write(text)
