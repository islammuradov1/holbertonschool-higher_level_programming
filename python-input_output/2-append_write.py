#!/usr/bin/python3
'''
Module that reads text file
'''


def append_write(filename="", text=""):
    '''
    Function that reads file
    '''

    with open(filename, 'a', encoding='UTF8') as f:
        return f.write(text)
