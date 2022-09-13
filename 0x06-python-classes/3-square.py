#!/usr/bin/python3
"""With this instance we will return the area of the Square"""


class Square:
    """The attributes of the Square"""

    def __intit(self, size=0):
        """The square as before takes the values
        Args:
            size (int): size of a side of the square
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

    def area(self):
        """Now the magic comes, calculating the area of square
        Returns:
            Area of the Square
        """

        return (self.__size) ** 2
