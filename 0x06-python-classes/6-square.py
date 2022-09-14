#!/usr/bin/python3
"""Defines a class known as Square"""


class Square:
    """Represents a square, no longer empty
    Attributes:
        __size (int): size of a side of the square
    """
    def __init__(self, size=0, position=(0, 0)):
        """initializes the square
        Args:
            size (int): Size of our Square
            position (int) (int): Position of new Square
        """
        self.size = size
        self.position = position

    def area(self):
        """calculates the Square's area
        Returns:
            The area of the Square
        """
        return (self.__size) ** 2

    @property
    def size(self):
        """getter of __size
        Returns:
            The size of the Square
        """
        return (self.__size)

    @size.setter
    def size(self, value):
        """setter of __size
        Args:
            value (int): The size of our Square
        Returns:
            None
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Get the position of Square"""
        return (self.__position)

    @position.setter
    def position(self, value):
        """Sets the position of our Square"""
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position =

    def my_print(self):
        """Prints our square"""
        if self.__size == 0:
            print()
            return
        [print() for i in range(0, self.__position[1])]
        for i in range(0, self.__size):
            [print(" ", end="") for j in range(0, self.__position[0])]
            [print("#", end="") for k in range(0, self.__size)]
            print()
