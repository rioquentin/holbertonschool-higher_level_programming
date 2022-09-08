#!/usr/bin/python3
islower = __import__('7-islower').islower
def uppercase(str):
    for i in str:
        if islower(i) == 1:
            print(chr(ord(i) - 32), end='')
        else:
            print('{}'.format(i), end='')
