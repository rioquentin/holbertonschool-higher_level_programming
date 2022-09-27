#!/usr/bin/python3
'''Module'''


def is_kind_of_class(obj, a_class):
    '''Function'''

    if type(obj) is a_class:
        return True
    if issubclass(type(obj), a_class) is True:
        return True
    else:
        return False
