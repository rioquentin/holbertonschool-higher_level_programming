#!/usr/bin/python3
'''Module'''


def write_file(filename="", text=""):
    '''Func'''

    with open(filename, encoding="utf-8") as f:
        return f.write(text)
