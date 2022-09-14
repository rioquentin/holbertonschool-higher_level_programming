#!/usr/bin/python3
def uniq_add(my_list=[]):
    if my_list:
        ban = []
        result = 0
        for i in my_list:
            if i not in ban:
                ban.append(i)
        for x in ban:
            result += x
        return result
