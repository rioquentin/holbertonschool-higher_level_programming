#!/usr/bin/python3
islower = __import__('7-islower').islower
def uppercase(str):
    for i in str:
        print('{}'.format(chr(ord(i) if not islower(i) else (ord(i) - 32)),
            end='')
    print('')