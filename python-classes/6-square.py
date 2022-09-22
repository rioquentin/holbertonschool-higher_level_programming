#!/usr/bin/python3
''' Empty Class'''


class Square(object):
    '''Empty'''

    def __init__(self, size=0, position=(0, 0)):
        '''defining size'''
        self.__size = size
        self.position = position

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

    @property
    def position(self):
        '''getting position'''
        return self.__position

    @position.setter
    def position(self, value):
        '''setting position'''
        i = "position must be a tuple of 2 positive integers"
        if type(value) is not tuple or len(value) != 2:
            raise TypeError(i)
        for i in value:
            if type(i) is not int or i < 0:
                raise TypeError(i)
        self.__position = value

    def area(self):
        '''Define size*size'''

        return self.__size * self.__size

    def my_print(self):
        ''' func to print the square'''
        if self.__size != 0:
            for b in range(0, self.__position[1]):
                    print("")
            for i in range(0, self.__size):
                for z in range(0, self.__position[0]):
                    print(" ", end="")
                for x in range(0, self.__size):
                    print("{}".format("#"), end="")
                print("")
        else:
            print("")
