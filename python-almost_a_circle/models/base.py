#!/usr/bin/python3
'''File that contain Parent class'''


class Base:
    '''Main class with basics methods'''

    __nb_objects = 0

    def __init__(self, id=None):
        '''Constructor for base attributes'''

        if id is None:
            __nb_objects += 1
            self.id = __nb_objects
        else:
            self.id = id
