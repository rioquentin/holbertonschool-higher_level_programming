#!/usr/bin/python3
''' all func'''


def text_indentation(text):
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
        elif h[x - 1] in ["?", ":", "."]:
            pass
        else:
            print(h[x], end="")
