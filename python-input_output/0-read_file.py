#!/usr/bin/python3
'''Func to read a text and print it to stdout'''


def read_file(filename=""):
    '''func'''

    with open(filename, encoding="utf-8") as f:
        r = f.read()
        print(r, end='')
