#!/usr/bin/python3
'''MOdule'''


class Student:
    '''Class'''

    def __init__(self, first_name, last_name, age):
        '''constructor'''

        self.first_name = first_name
        self.last_name = last_name

    def to_json(self):
        '''to json'''

        return self.__dict__
