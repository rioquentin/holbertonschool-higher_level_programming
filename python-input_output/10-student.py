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
            l = []
            for i in attrs:
                l.append(i)
            return self.__dict__(l)
