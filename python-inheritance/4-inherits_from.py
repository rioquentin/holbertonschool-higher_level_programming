#!/usr/bin/python3
'''Module'''


def inherits_from(obj, a_class):
    '''Func'''

    if issubclass(type(obj), a_class) is True:
        return True
    else:
        return False
