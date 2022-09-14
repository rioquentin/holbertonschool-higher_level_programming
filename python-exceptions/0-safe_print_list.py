#!/usr/bin/python3
def str_len(a):
    for i in a:
        j+=1
    return j

def safe_print_list(my_list=[], x=0):
    z = 0
    try:
        for i in range(0, x + 1):
            print(my_list[i], end='')
            z += 1
        print("")
    except:
        print("")
    return z
