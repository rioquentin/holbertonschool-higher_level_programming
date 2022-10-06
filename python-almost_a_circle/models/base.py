#!/usr/bin/python3
'''File that contain Parent class'''


import json


class Base:
    '''Main class with basics methods'''

    __nb_objects = 0

    def __init__(self, id=None):
        '''Constructor for base attributes'''

        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        '''JSON str repr of argument'''

        if list_dictionaries is None:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    def save_to_file(cls, list_objs):
        '''save json string to a file'''

        with open(type(cls) + ".json", 'w+') as f:
            json.dump(to_json_string(list_objs), f)
