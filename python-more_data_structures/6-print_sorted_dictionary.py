#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    sdict = sorted(a_dictionary.items())
    for i, x in sdict:
        print(i + ": " + str(x))
