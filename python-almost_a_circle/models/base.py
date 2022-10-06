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

    @classmethod
    def save_to_file(cls, list_objs):
        '''save json string to a file'''
        new = []
        name = cls.__name__ + ".json"
        if list_objs is not None:
            for i in list_objs:
                new.append(i.to_dictionary())
        json_string = cls.to_json_string(new)
        with open(name, 'w+') as f:
            f.write(json_string)

    @staticmethod
    def from_json_string(json_string):
        ''' load a json string'''
        if json_string is Not None or json_string:
            return json.loads(json_string)
        else:
            return []
