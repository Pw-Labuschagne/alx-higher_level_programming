#!/usr/bin/python3
"""Subclass called square from rectangle"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Subclass of rectangle, now a square"""

    def __init__(self, size):
        """Initializes a square
        args:
            size (int) = size of square(sides)
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
