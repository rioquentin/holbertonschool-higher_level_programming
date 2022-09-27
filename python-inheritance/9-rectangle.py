#!/usr/bin/python3
'''Module'''


BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    '''Class'''

    def __init__(self, width, height):
        '''Constructor'''
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def __str__(self):
        '''print str'''
        return ("[Rectangle] {}/{}".format(self.__width, self.__height))

    def area(self):
        '''area'''
        return self.__width * self.__height
