#!/usr/bin/python3
'''Module'''
import json


def from_json_string(my_str):
    '''return object from json'''

    return json.load(my_str)
