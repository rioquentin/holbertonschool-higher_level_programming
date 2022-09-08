#!/usr/bin/python3
islower = __import__('7-islower').islower
_print = __import__('func')._print
def uppercase(str):
    for i in str:
        if islower(i) == 1:
            _print(i)
        else:
            print('{}'.format(i), end='')
    print("")
