#!/usr/bin/python3
''' all func'''

def is_same_class(obj, a_class):
    ''' check if obj is instance of a-class'''

    if isinstance(obj, a_class) == True:
        return True
    else:
        return False
