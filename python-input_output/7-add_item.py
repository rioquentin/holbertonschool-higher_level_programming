#!/usr/bin/python3
'''Module'''


import sys
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file


f = load_from_json_file("add_item.json")
for i in range(1, len(sys.argv)):
    f.append(sys.argv[i])
save_to_json_file(f, "add_item.json")
