#!/usr/bin/python3
''' all func'''


def text_indentation(text):
    if type(text) is not str:
        raise TypeError("text must be a string")
    l = text.split()
    h = ""
    for i in l:
        if h == "":
            h += i
        else:
            h += " " + i
    for x in range(0, len(h)):
        if h[x] in ["?", ".", ":"]:
            print(h[x] + "\n")
        elif h[x - 1] in ["?", ":", "."] and h[x] == " ":
            pass
        else:
            print(h[x], end="")
