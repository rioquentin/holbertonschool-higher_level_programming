#!/usr/bin/python3
''' all func'''


def text_indentation(text):
    if type(text) is not str:
        raise TypeError("text must be a string")

    for i in range(0, len(text)):
        if text[i] == "?":
            print(text[i])
            print("")
            i += 1
        elif text[i] == ":":
            print(text[i])
            print("")
            i += 1
        elif text[i] == ".":
            print(text[i])
            print("")
            i += 1
        else:
            print(text[i], end="")
