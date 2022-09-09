#!/usr/bin/python3
islower = __import__('7-islower').islower
def uppercase(str):
    a = ord(i) - 32
    for i in str:
        print('{}'.format(chr(ord(i) if not islower(i) else a)), end='')
    print('')
