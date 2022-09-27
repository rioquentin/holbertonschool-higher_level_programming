#!/usr/bin/python3
'''Module'''


class Rectangle(BaseGeometry):
    '''Class'''

    def __init__(self, width, height):
        '''Constructor'''

        super().integer_validator(self, "width", width)
        super().integer_validator(self, "height", height)
        self.__width = width
        self.__height = height
