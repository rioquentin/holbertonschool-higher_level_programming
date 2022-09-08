#!/usr/bin/python3
islower = __import__('7-islower').islower
def _print(c):
    print(chr(ord(c) - 32), end='')

def uppercase(str):
    for i in str:
        if islower(i) == 1:
            _print(i)
        else:
            print('{}'.format(i), end='')
    print("")
