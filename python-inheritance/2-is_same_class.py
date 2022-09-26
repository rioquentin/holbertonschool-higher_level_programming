#!/usr/bin/python3
''' all func'''

def is_same_class(obj, a_class):
    ''' check if obj is instance of a-class'''

    if type(obj) is not in [int, float, object]:
        return False
    if isinstance(obj, a_class) == True:
        return True
    else:
        return False
