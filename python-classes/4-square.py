#!/usr/bin/python3
''' Empty Class'''


class Square:
    '''Empty'''
 
    def __init(self, size=0):
        '''defining size'''
        self.__size = size

    def size(self):
        '''setter'''
        return self.__size

    def size(self, value):
        '''seting size'''

        if isinstance(value, int) is False:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value


    def area(self):
        '''Define size*size'''

        return self.__size * self.__size
