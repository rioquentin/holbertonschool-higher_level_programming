#!/usr/bin/python3
'''all the func'''


def add_integer(a, b=98):
    '''func to add'''

    if type(a) not in (int, float):
        raise TypeError("a must be an integer")
    elif type(b) not in (int, float):
        raise TypeError("b must be an integer")
    else:
        if type(b) is float:
            b = int(b)
        elif type(a) is float:
            a = int(a)
        return a + b
