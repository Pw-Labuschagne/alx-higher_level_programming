#!/usr/bin/python3
"""An inherited class"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Inherited from BaseGeomerty"""

    def __init__(self, width, height):
        """Instance of BaseGeometry
        Args:
            width (int) = Width of rectangle
            height (int) = Height of rectangle
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
