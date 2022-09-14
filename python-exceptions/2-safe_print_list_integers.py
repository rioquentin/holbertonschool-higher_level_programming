#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    z = 0
    try:
        for i in range(0, x):
            if isinstance(my_list[i], int) is True:
                print("{}".format(my_list[i]), end='')
                z += 1
        print("")
    except (ValueError, TypeError):
        None
        
    return z
