#!/usr/bin/python3

'''Module'''

BaseGeometry = __import__('7-base_geometry').BaseGeometry

class Rectangle(BaseGeometry):
    '''Class'''

    def __init__(self, width, height):
        '''Constructor'''

        super().integer_validator(self, "width", width)
        super().integer_validator(self, "height", height)
        self.__width = width
        self.__height = height
