#!/usr/bin/python3
"""Now we take our Square size and give it some value"""


class Square:
    """The Square size will be initialize"""
    def __init__(self, size=0):
        """initializes the square
        Args:
            size (int): size of the square
        Returns:
            None
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        else:
            if size < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = size
