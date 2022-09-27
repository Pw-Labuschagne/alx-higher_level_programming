#!/usr/bin/python3
"""script that adds all arguments to a Python list,
and then save them to a file"""
import json
from sys import argv
if __name__ == "__main__":
    save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
    load_from_json_file = __import__('6-load_from_json_file').\
        load_from_json_file

all_args = []

try:
    all_args = load_from_json_file("add_item.json")
except FileNotFoundError:

    for i in range(1, len(argv)):
        all_args.append(argv[i])

    save_to_json_file(all_args, "add_item.json")
