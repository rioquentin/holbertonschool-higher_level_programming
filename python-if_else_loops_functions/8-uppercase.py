#!/usr/bin/python3
islower = __import__('7-islower').islower
def uppercase(str):
    for i in range(0, (len(str) + 1)):
        if islower(str[i]) == 1:
            print(chr(ord(str[i]) - 32), end='')
        else:
            print(str[i], end='')
