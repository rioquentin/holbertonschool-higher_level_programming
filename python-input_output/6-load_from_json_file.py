#!/usr/bin/python3
'''Module'''
import json


def load_from_json_file(filename):
    '''load a json repr from a file'''

    with open(filename, 'r') as f:
        return json.load(f)
