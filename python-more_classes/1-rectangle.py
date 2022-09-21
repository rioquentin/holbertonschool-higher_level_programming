#!/usr/bin/python3
''' Empty Class'''


class Rectangle:
    '''Property of class rectangle'''

    def __init__(self, width=0, height=0):
        self.__height = height
        self.__width = width

    @property
    def width(self):
        '''getter'''
        return self.__width

    @width.setter
    def width(self, value):
        '''setter'''
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise TypeError("width must be >= 0")
        self.__width = value


    @property
    def height(self):
        '''getter'''
        return self.__height

    @height.setter
    def height(self, value):
        '''setter'''
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise TypeError("height must be >= 0")
        self.__height = value


