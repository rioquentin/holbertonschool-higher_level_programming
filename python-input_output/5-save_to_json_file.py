#!/usr/bin/python3
'''Module'''
import json


def save_to_json_file(my_obj, filename):
    '''func to put json repr in a file'''

    with open(filename, 'w') as f:
        json.dump(my_obj, f)
