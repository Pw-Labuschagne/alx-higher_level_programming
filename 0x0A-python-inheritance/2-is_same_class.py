#!/usr/bin/python3
"""Function that checks if two objects are excatly the same"""


def is_same_class(obj, a_class):
    """Checks if and instance is of the specified class"""
    if type(obj) is a_class:
        return True
    else:
        return False
