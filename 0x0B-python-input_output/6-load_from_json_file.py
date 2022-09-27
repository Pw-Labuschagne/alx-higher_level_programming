#!/bin/usr/python3
"""Write a function that creates an Object from a “JSON file”"""
import json


def load_from_json_file(filename):
    """Makes obj from json file"""
    with open(filename, mode="r", encoding="utf-8") as j_man:
        data = json.load(j_man)
        return data

