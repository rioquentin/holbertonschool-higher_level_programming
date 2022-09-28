#!/usr/bin/python3
'''Module'''
import json
import sys
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file


def main(args):
    '''func'''

    f = load_from_json_file("add_item.json")
    for i in args:
        f.append(i)
    save_to_json_file(f, "add_item.json")

main(sys.argv[1:])
