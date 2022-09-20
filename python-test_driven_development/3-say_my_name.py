#!/usr/bin/python3

'''Func '''


def say_my_name(first_name, last_name=""):
    '''func to print'''

    if first_name == None and last_name == None:
        raise TypeError("missing two arguments")
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
