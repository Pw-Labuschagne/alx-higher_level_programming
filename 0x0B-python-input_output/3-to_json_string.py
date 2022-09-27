#!/usr/bin/python3
"""function that returns the JSON representation of an object (string)"""
import json


def to_json_string(my_obj):
    """Returns JSON rep of obj"""
    with open(my_obj, mode="w", encoding="utf-8") as j_man:
        return json.dumps(my_obj)
