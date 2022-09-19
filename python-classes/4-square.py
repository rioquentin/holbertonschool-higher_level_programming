#!/usr/bin/python3
''' Empty Class'''


class Square(object):
    '''Empty'''
 
    def __init__(self, size=0):
        '''defining size'''
        self.__size = size
    
    @property
    def size(self):
        '''setter'''
        return self.__size

    @size.setter
    def size(self, value):
        '''seting size'''

        if isinstance(value, int) is False:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value


    def area(self):
        '''Define size*size'''

        return self.__size * self.__size
