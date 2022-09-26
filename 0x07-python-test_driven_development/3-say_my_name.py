#!/usr/bin/python3
"""Fucntion to print name in format" My name is <first name> <last name>"""


def say_my_name(first_name, last_name=""):
    """Function defined to print name
    Args:
        first_name (string): First name
        last_name (string): Last name
    Raises:
        TypeError: first_name must be a string
        TypeError: last_name must be a string
    Return:
        My name is <first_name> <last_name>
    """

    if (not isinstance(first_name, str)):
        raise TypeError("first_name must be a string")
    if (not isinstance(last_name, str)):
        raise TypeError("last_name must be a string")

    print("My name is ", first_name, last_name)
