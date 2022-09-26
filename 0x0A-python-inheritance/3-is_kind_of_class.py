#!/usr/bin/python3
"""Checks if an object is an instance of a class"""


def is_kind_of_class(obj, a_class):
    """Returns True if it is the same instance otherwise returns False"""
    if isinstance(obj, a_class):
        return True
    else:
        return False
