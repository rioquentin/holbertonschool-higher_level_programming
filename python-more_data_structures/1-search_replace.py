#!/usr/bin/python3
def search_replace(my_list, search, replace):
    if my_list and search and replace:
        return [replace if item == search else
                item for item in my_list]
    else:
        return my_list
