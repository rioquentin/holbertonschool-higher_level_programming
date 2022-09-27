#!/usr/bin/python3
'''Module'''


class BaseGeometry:
    '''Class'''

    def area(self):
        '''Method to get area'''

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        '''Check Value'''

        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))

        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

class Rectangle(BaseGeometry):
    '''Class'''

    def __init__(self, width, height):
        '''Constructor'''

        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height
