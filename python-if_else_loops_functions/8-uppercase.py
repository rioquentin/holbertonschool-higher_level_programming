#!/usr/bin/python3
islower = __import__('7-islower').islower
def uppercase(str):
    for i in range(0, 2):
        if islower(str[i]) == 1:
            a = ord(str[i])
            print(a)
            b = a - 32
            print(b)
            c = chr(b)
            print(c)
            # print(chr(ord(str[i]) - 32), end='')
        else:
            print(str[i], end='')
