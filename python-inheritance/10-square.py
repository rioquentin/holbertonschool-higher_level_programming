#!/usr/bin/python3
'''module'''


Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    '''class for square'''

    def __init__(self, size):
        '''constructor for the square'''
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        return self.__size * self.__size
