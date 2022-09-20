#!/usr/bin/python3
''' all func'''


def print_square(size):
    ''' func to print a square'''

    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise TypeError("size must be >= 0")
    if type(size) is float and size < 0:
        raise TypeError("size must be an integer")

    for i in range(0, size):
        for x in range(0, size):
            print("#", end="")
        print("")
