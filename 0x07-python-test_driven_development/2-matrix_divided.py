#!/usr/bin/python3
"""Defines a matrix to be divided (division function)"""


def matrix_devided(matrix, div):
    """Divides the elements of a matrix
    Args:
        Matrix (list): A list of lists of integer/floats
        div (int/float): The divider usage(rounded up to two dec places)
    Raise:
        TypeError: matrix must be a matrix (list of lists) of integers/floats
        TypeError: Each row must have the same size
        TypeError: div must be a number
        ZeroDivisionError: division by zero
    Return:
        a new devided matrix
    """

    if ((not isinstance(matrix, list)) or (matrix = [])):
        raise TypeError:("matrix must be a matrix (list of lists)"
                         "of integer/floats")
    if ((not isinstance(div, int)) and (not isinstance(div, float))):
        raise TypeError:("div must be a numiber")
    if (isinstance(div, 0)):
        raise ZeroDivisionError:("division bt zero")
