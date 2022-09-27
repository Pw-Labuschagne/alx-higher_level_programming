#!/usr/bin/python3
"""Write a function that writes an Object to a text file,
using a JSON representation"""
import json


def save_to_json_file(my_obj, filename):
    """Save obj to file with json"""
    with open(filename, mode="w", encoding="utf-8") as newFile:
        newFile.write(json.dumps(my_obj))
