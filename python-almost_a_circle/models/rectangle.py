#!/usr/bin/python3
'''Child class of Base'''


from models.base import Base


class Rectangle(Base):
    '''Class that define a rectangle'''

    def __init__(self, width, height, x=0, y=0, id=None):
        '''Constructor For rectangles class'''

        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    # getter and setter for width parameter

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    # getter and setter for height parameter

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    # getter and setter for x parameter

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    # getter and setter for y parameter

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        '''Return the area of the instance'''

        return self.width * self.height

    def display(self):
        '''Print the rectangle with #'''
        for a in range(0, self.y):
            print('')
        for i in range(0, self.height):
            for b in range(0, self.x):
                print(' ', end='')
            for x in range(0, self.width):
                print("#", end='')
            print('')

    def __str__(self):
        '''Overwrite the str() method'''

        return("[Rectangle] ({}) {}/{} - {}/{}".format
               (self.id, self.x, self.y, self.width, self.height))

    def update(self, *args):
        '''method to update the rectangle'''

        if args[0]:
            self.id = args[0]
            if len(args) >= 2:
                self.width = args[1]
                if len(args) >= 3:
                    self.height = args[2]
                    if len(args) >= 4:
                        self.x = args[3]
                        if len(args) >= 5:
                            self.y = args[4]

