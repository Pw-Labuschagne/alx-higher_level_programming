#!/usr/bin/python3
"""With this instance we will return the area of the Square"""


class Square:
    """Still the empty class that defines a Square"""

    def __init__(self, size=0):
        """Args:
            size (int) : size of our Square
        """

        if isinstance(size, int) is False:
            raise TypeError('size must be an integer')

        elif size < 0:
            raise ValueError('size must be >= 0')

        self.__size = size

    def area(self):
        """Returns area of Square
            Returns :
                int: area
        """
        return self.__size * self.__size
