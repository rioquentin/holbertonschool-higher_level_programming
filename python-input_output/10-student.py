#!/usr/bin/python3
'''MOdule'''


class Student:
    '''Class'''

    def __init__(self, first_name, last_name, age):
        '''constructor'''

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        '''to json'''
        if attrs == None:
            return self.__dict__
        else:
            a = {}
            for i in attrs:
                a.update({i:dict(self.__dict__).get(i)})
            return a

