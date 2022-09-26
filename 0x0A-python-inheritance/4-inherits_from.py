#!/usr/bin/python3
"""Checks  if obj is a instance of a class"""


def inherits_from(obj, a_class):
    """Returns True if obj is inherited instance, returns False if otherwise"""
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    else:
        return False
