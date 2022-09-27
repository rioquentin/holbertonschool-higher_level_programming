#!/usr/bin/python3
'''module'''


class Square(Rectangle):
    '''class for square'''

    def __init__(self, size):
        '''constructor for the square'''
        if size >= 0:
            self.__size = size

            def area(self):
                return self.__size * self.__size

