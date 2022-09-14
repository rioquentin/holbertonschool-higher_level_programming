#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    try:
        nl = []
        for i in range(0, list_length):
            try:
                result = format(my_list_1[i] // my_list_2[i], ".1f")
                nl.append(float(result))
            except ZeroDivisionError:
                print("division by 0")
                nl.append(0)
            except TypeError:
                print("wrong type")
                nl.append(0)
            except IndexError:
                print("out of range")
                nl.append(0)
    finally:
        return nl
