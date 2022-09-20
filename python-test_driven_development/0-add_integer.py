#!/usr/bin/python3
'''all the func'''


def add_integer(a, b=98):
    '''func to add'''

    if type(a) not in [int, float] or a != a:
        raise TypeError("a must be an integer")
    elif type(b) not in [int, float] or b != b:
        raise TypeError("b must be an integer")
    else:
        if type(b) is float:
            b = int(b)
        if type(a) is float:
            a = int(a)
    return a + b
