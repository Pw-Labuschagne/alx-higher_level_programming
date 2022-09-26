#!/usr/bin/python3
"""
This is a function that adds two integers

integer a + b

"""


def add_integer(a, b=98):
    """The addition of two integers
    Args:
        a (int/float): Fist argument
        b (98/int/float): Second argument
    Raises:
        TypeError: a must be an integer
        TypeError: b must be an integer
    Return:
        a + b
    """
    if ((not isinstance(a, int)) and (not isinstance(a, float))):
        raise TypeError("a must be an integer")
    if ((not isinstance(b, int)) and (not isinstance(b, float))):
        raise TypeError("b must be an integer")

    sum = int(a) + int(b)

    return(sum)
